/*!
* @file index.js
* @brief Login/authentication/user database server. API endpoint: http://localhost:10101/
*/

//! Importing the express library
const express = require('express');

//! Importing the cors library
const cors = require('cors');

//! Importing the body-parser library
const bodyParser = require('body-parser');

//! Importing the express-bearer-token library
const bearerToken = require('express-bearer-token');

//! Defining the path for accessing API methods
const profile = require('./profile');

//! Defining the port for this server
const port = process.env.PORT || 10101;

//! Setting up the expressJS app using imported libraries
const app = express()
  .use(cors())
  .use(bodyParser.json())
  .use(bearerToken());

/*!
* @brief Directing the server to profile.js for accessing API methods
*/
app.use('/', profile);

app.listen(port, () => {
  console.log(`Express server listening on port ${port}`);
});
