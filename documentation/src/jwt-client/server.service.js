/*!
* @file server.service.js
* @brief API endpoint: authentication server connection service for frontend. Actual implementation is in .ts; relevant parts transposed to .js only for documentation.
*/

//! type:String Defining the URL at which to access the authentication server
const baseUrl = 'http://localhost:10101';

/*!
* @brief Sets login status to true or false
* @param type:boolean loggedIn the state to which login is to be set
* @param type:string token (optional) if loggedIn is true, the corresponding token to be set for the current session
*/
function setLoggedIn(loggedIn, token) {
}

/*!
* @brief The main method to perform requests to the authentication server backend
* @param type:string method indicates whether to perform GET or POST to the authentication server
* @param type:string route indicates the route to be followed on the server corresponding to the desired function, e.g. '/register' for the registration function
* @param type:any data (optional) any data that is required to perform the request to the server successfully
* @return type:json the response from the server;  may be some user data or success/fail status of the request
*/
function request(method, route, data) {
}

/*!
* @brief Specifically performs GET requests to the authentication server backend
* @param type:string route indicates the route to be followed on the server corresponding to the desired function, e.g. '/profile' to retrieve profile data
* @param type:any data (optional) any data that is required to perform the GET request to the server successfully
* @return type:json the response from the server
*/
function get(route, data) {
}
