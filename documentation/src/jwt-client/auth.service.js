/*!
* @file auth.service.js
* @brief Authentication service for frontend. Actual implementation is in .ts; relevant parts transposed to .js only for documentation.
*/

/*!
* @brief Checks if the current session is authenticated
* @return type:Observable indication of whether user is logged in or not
*/
function isLoggedIn() {
}

/*!
 *  @brief Authenticates and ogs the user in if the passwords entered are valid
 *  @param type:userData user userData entered in form on login page
 *  @return error if login fails, else reroutes user to homepage
 */
function login(user) {
}

/*!
* @brief Deletes the authentication JWT and logs the current user out
*/
function logout() {
}
