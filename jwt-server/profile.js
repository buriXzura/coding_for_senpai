const express = require('express');
const bcrypt = require('bcryptjs');
const sqlite3 = require('sqlite3').verbose();
const nJwt = require('njwt');
const config = require('./config');

const db = new sqlite3.Database('userinfo.db');

db.serialize(() => {
  db.exec('PRAGMA foreign_keys = ON;');
  db.run("CREATE TABLE IF NOT EXISTS org (oname TEXT PRIMARY KEY, opassword TEXT)");
  db.run("INSERT OR IGNORE INTO org (oname, opassword) VALUES (?,?), (?,?), (?,?)", ["iitbadmin","solar","iitbteacher","sso","iitbstudent","captcha"]);
  db.run("UPDATE org" + " SET opassword = ?" + " WHERE oname = ?", ["happy", "iitbadmin"]);
  db.run("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT UNIQUE, password TEXT, orgname TEXT, FOREIGN KEY (orgname) REFERENCES org(oname))");
});

const router = express.Router();

router.post('/register', function(req, res) {
  var hashedPassword = bcrypt.hashSync(req.body.password, 8);

  db.run("INSERT INTO users (name, email, password, orgname) "
        + "VALUES (?, ?, ?, ?)", req.body.name, req.body.email, hashedPassword, req.body.orgname,
  function (err) {
    if (err) return res.status(500).send("An error occurred during registration");

    res.status(200).send({ status: 'ok' });
  });
});

router.post('/login', function(req, res) {
  db.get("SELECT users.id, users.name, users.email, users.password, org.opassword FROM users INNER JOIN org ON org.oname=users.orgname WHERE users.email=?",
  req.body.email, function (err, user) {
    if (err) return res.status(500).send({status: 'Server error', err:err});
    if (!user) return res.status(404).send('User not found');

    if (!bcrypt.compareSync(req.body.password, user.password)) {
      return res.status(401).send({ auth: false, token: null });
    }

    if(user.opassword!=req.body.orgpswd) {
      return res.status(401).send({ auth: false, token: null });
    }

    var jwt = nJwt.create({ id: user.id }, config.secret);
    jwt.setExpiration(new Date().getTime() + (24*60*60*1000));

    res.status(200).send({ auth: true, token: jwt.compact() });
  });
});

const jwtAuth = require('./auth');

router.get('/profile', jwtAuth, function(req, res, next) {
  db.get("SELECT id, name, email, orgname FROM users WHERE id=?", req.userId, function (err, user) {
    if (err) {
      return res.status(500).send("There was a problem finding the user.");
    }
    if (!user) {
      return res.status(404).send("No user found.");
    }
    res.status(200).send(user);
  });
});

router.post('/chngchk', jwtAuth, function(req,res,next) {
  db.get("SELECT password FROM users WHERE email=?",
  req.body.email, function (err, user) {
    if (err) return res.status(500).send({status: 'Server error', err:err});
    if (!user) return res.status(404).send('User not found');

    if (!bcrypt.compareSync(req.body.password, user.password)) {
      return res.status(401).send("Incorrect password");
    }
    res.status(200).send({ status: 'ok' });
  });
});

router.post('/chngpswd', jwtAuth, function(req,res,next) {
  var hashedPassword = bcrypt.hashSync(req.body.password, 8);

  db.get("UPDATE users" + " SET password = ?"
        + " WHERE email = ?", hashedPassword, req.body.email, function(err) {
    if (err) return res.status(500).send("An error occurred during changing password");

    res.status(200).send({ status: 'ok' });
  });
});

module.exports = router;
