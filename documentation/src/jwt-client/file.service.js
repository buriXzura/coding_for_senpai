/*!
* @file file.service.js
* @brief API endpoint: file server connection service for frontend. Actual implementation is in .ts; relevant parts transposed to .js only for documentation.
*/

//! type:String Defining the URL at which to access the file server
const DJANGO_SERVER = "http://127.0.0.1:8000";

//! type:String stores the current session id using the user email id in order to ensure each user can accesses only their own files in the backend
var session;

/*!
* @brief Sets the current session id
* @param type:String ss the string to which the session id is to be set
*/
function get_session(ss){
}

/*!
* @brief updates the session with the email id retrieved from the server
* @param type:FormData formData information of the file to be uploaded and its contents
* @return type:FileLikeObject the data associated with registering of the file in the model
*/
function upload(formData){}

/*!
* @brief allows the user to download the result(.csv) file registered in the model
* @return type:arrayBuffer the contents of file
*/
function DownloadResults(){}

/*!
* @brief gets the list of files uploaded
* @return type:Object the list of files requested
*/
function list(){
}

/*!
* @brief deletes the file from the data base as well as from the backend
* @param type:number id the primary key of the file regitered in model
* @return type:object the status of delete request
*/
function delete(id){
}

/*!
* @brief deletes all the files wth a given session
* @return type:object the status of the delete request
*/
function deleteall(){
}

/*!
* @brief deletes the stub file provided (if any)
* @return type:object the status of the delete request
*/
function delete1(){
}

/*!
* @brief deleted the generated result file
* @return type:object the status of the delete request
*/
function deleteResults(){
}

/*!
* @brief provides the list of stub files (single/no file in our case)
* @return type:Object the list of files requested
*/
function List1(){
}

/*!
* @brief provides the result file's information
* @return type:Object the result file's associated data
*/
function resultsList(){
}

/*!
* @brief generates the result (.csv) file
* @param type:boolean cpp defines whether the files to be processed are cpp files or not
* @return type:Object the data associated with the generated file
*/
function generate(cpp){
}

/*!
* @brief requests the server to create plots and return the surface plot
* @return type:Observable<Blob> the contents of surfacePlot.png file
*/
function getImage(){
}

/*!
* @brief requests the server for markers.txt file
* @return type:JSON the contents of markers.txt file
*/
function getMarkers(){
}

/*!
* @brief requests the server for heatmap.png file
* @return type:Observable<Blob> the contents of heatmap.png file
*/
function getHeat(){
}

/*!
* @brief sends the list of files for which plots are requested to the server and asks for the computation
* @param type:FormData formData the list of the concerned files
* @return type:Object status of the request
*/
function sendList(formData){
}

/*!
* @brief requests the server for surfacePlot.png file
* @return type:Observable<Blob> the contents of surfacePlot.png file
*/
function someplot(){
}

/*!
* @brief requests the server to delete the plots and markers file
* @return type:Object status of the delete request
*/
function deleteplots(){
}
