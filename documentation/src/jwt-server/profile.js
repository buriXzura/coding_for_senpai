/*!
* @file profile.js
* @brief Method implementations for login/authentication server.
*/

//! Importing the express library
const express = require('express');

//! Importing the bcryptjs library
const bcrypt = require('bcryptjs');

//! Importing the sqlite3 library
const sqlite3 = require('sqlite3').verbose();

//! Importing the njwt library
const nJwt = require('njwt');

//! Defining the path for the config file
const config = require('./config');

//! Defining the path for the user information database
const db = new sqlite3.Database('userinfo.db');

//! Initializing/updating the database with user and organisation information
db.serialize(() => {
  /*!
  * @brief Initializing/updating the database with user and organisation info
  */
  db.exec('PRAGMA foreign_keys = ON;');
  db.run("CREATE TABLE IF NOT EXISTS org (oname TEXT PRIMARY KEY, opassword TEXT)");
  db.run("INSERT OR IGNORE INTO org (oname, opassword) VALUES (?,?), (?,?), (?,?)", ["iitbadmin","solar","iitbteacher","sso","iitbstudent","captcha"]);
  db.run("UPDATE org" + " SET opassword = ?" + " WHERE oname = ?", ["happy", "iitbadmin"]);
  db.run("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT UNIQUE, password TEXT, orgname TEXT, FOREIGN KEY (orgname) REFERENCES org(oname))");
});

//! Initializes the router for the server
const router = express.Router();

//! Method for registering a new user
router.post('/register', function(req, res) {

  //! Encrypying the input password for storage
  var hashedPassword = bcrypt.hashSync(req.body.password, 8);

  //! Inserting user info into the database
  db.run("INSERT INTO users (name, email, password, orgname) "
        + "VALUES (?, ?, ?, ?)", req.body.name, req.body.email, hashedPassword, req.body.orgname,
  function (err) {
    if (err) return res.status(500).send("An error occurred during registration");

    res.status(200).send({ status: 'ok' });
  });
});

//! Method for validating existing user login
router.post('/login', function(req, res) {

  //! Retrieving existing user pswd and organisation pswd from database corresponding to the input email id
  db.get("SELECT users.id, users.name, users.email, users.password, org.opassword FROM users INNER JOIN org ON org.oname=users.orgname WHERE users.email=?",

  req.body.email, function (err, user) {
    if (err) return res.status(500).send({status: 'Server error', err:err});
    if (!user) return res.status(404).send('User not found');

    //! Checking that input user pswd matches retrieved user pswd
    if (!bcrypt.compareSync(req.body.password, user.password)) {
      return res.status(401).send({ auth: false, token: null });
    }

    //! Checking that input org pswd matches retrieved org pswd
    if(user.opassword!=req.body.orgpswd) {
      return res.status(401).send({ auth: false, token: null });
    }

    //! Creating and sending a JWT
    var jwt = nJwt.create({ id: user.id }, config.secret);
    jwt.setExpiration(new Date().getTime() + (24*60*60*1000));
    res.status(200).send({ auth: true, token: jwt.compact() });
  });
});

//! Defining a variable to pass to methods which require authentication to be used
const jwtAuth = require('./auth');

//! Method for retrieving user data to display in the profile
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

//! Method for checking that input user pswd matches user pswd in the database (validating request to change password)
router.post('/chngchk', jwtAuth, function(req,res,next) {

  //! Retrieiving existing user pswd from database
  db.get("SELECT password FROM users WHERE email=?",
  req.body.email, function (err, user) {
    if (err) return res.status(500).send({status: 'Server error', err:err});
    if (!user) return res.status(404).send('User not found');

    //! Checking that input user pswd matches retrieved user pswd
    if (!bcrypt.compareSync(req.body.password, user.password)) {
      return res.status(401).send("Incorrect password");
    }
    res.status(200).send({ status: 'ok' });
  });
});

//! Method for updating user password
router.post('/chngpswd', jwtAuth, function(req,res,next) {
  var hashedPassword = bcrypt.hashSync(req.body.password, 8);

  db.get("UPDATE users" + " SET password = ?"
        + " WHERE email = ?", hashedPassword, req.body.email, function(err) {
    if (err) return res.status(500).send("An error occurred during changing password");

    res.status(200).send({ status: 'ok' });
  });
});

module.exports = router;
