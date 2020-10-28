const express = require('express');
const multer = require('multer');
const cors = require('cors');
const bodyParser = require('body-parser');
const bearerToken = require('express-bearer-token');
const profile = require('./profile');

const port = process.env.PORT || 10101;

const app = express()
  .use(cors())
  .use(bodyParser.json({limit: '50mb'}))
  .use(bearerToken());

app.use('/', profile);

app.listen(port, () => {
  console.log(`Express server listening on port ${port}`);
});

var fileExtension = require('file-extension');
const compression = require('compression');

const userFiles = './uploads/';
const fs = require('fs');

app.put('/files', (req, res) => {
 const file = req.body;
 const base64data = file.content.replace(/^data:.*,/, '');
 fs.writeFile(userFiles + file.name, base64data, 'base64', (err) => {
   if (err) {
     console.log(err);
     res.sendStatus(500);
   } else {
     res.set('Location', userFiles + file.name);
     res.status(200);
     res.send(file);
   }
 });
});

const path = require('path');

app.get('/files/**',(req, res) => {
const file = req.url.substring(28);
var fileLocation = path.join('./uploads',file);
res.download(fileLocation, file);
});

app.delete('/files/**', (req, res) => {
 const fileName = req.url.substring(32);
 var fileLocation = path.join('./uploads',fileName);
 fs.unlink(fileLocation, (err) => {
   if (err) {
     console.log(err);
     res.sendStatus(500);
   } else {
     res.status(204);
     res.send({});
   }
 });
});
