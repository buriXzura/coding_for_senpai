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
* @brief <brief description of upload function>
* @param type:<formData ka type daalna idhar> formData <formData kya hai?>
* @return type:<return type daalna idhar> <kya return ho raha?>
*/
function upload(formData){
}
public upload(formData) {
  return this.http.post<any>(`${this.DJANGO_SERVER}/file/upload`, formData);
}

/*!
* @brief <brief description of DownloadResults function>
* @return type:<return type daalna idhar> <kya return ho raha?>
*/
function DownloadResults(){
}
public DownloadResults() {
  return this.http.get(`${this.DJANGO_SERVER}/file/results/download/${this.session}`, {responseType: 'arraybuffer'});
}

/*!
* @brief <brief description of list function>
* @return type:<return type daalna idhar> <kya return ho raha?>
*/
function list(){
}
public list() {
  return this.http.get(`${this.DJANGO_SERVER}/file/list/${this.session}`);
}

/*!
* @brief <brief description of delete function>
* @param type:<id ka type daalna idhar> id <id kya hai?>
* @return type:<return type daalna idhar> <kya return ho raha?>
*/
function delete(id){
}
public delete(id) {
  return this.http.delete(`${this.DJANGO_SERVER}/file/delete/${id}`);
}

/*!
* @brief <brief description of deleteall function>
* @return type:<return type daalna idhar> <kya return ho raha?>
*/
function deleteall(){
}
public deleteall() {
  return this.http.delete(`${this.DJANGO_SERVER}/file/deleteall/${this.session}`);
}

/*!
* @brief <brief description of delete1 function>
* @return type:<return type daalna idhar> <kya return ho raha?>
*/
function delete1(){
}
public delete1() {
  return this.http.delete(`${this.DJANGO_SERVER}/file/stub/delete/${this.session}`);
}

/*!
* @brief <brief description of deleteResults function>
* @return type:<return type daalna idhar> <kya return ho raha?>
*/
function deleteResults(){
}
public deleteResults() {
  return this.http.delete(`${this.DJANGO_SERVER}/file/results/delete/${this.session}`);
}

/*!
* @brief <brief description of List1 function>
* @return type:<return type daalna idhar> <kya return ho raha?>
*/
function List1(){
}
public List1() {
  return this.http.get<Blob[]>(`${this.DJANGO_SERVER}/file/stub/list/${this.session}`);
}

/*!
* @brief <brief description of resultsList function>
* @return type:<return type daalna idhar> <kya return ho raha?>
*/
function resultsList(){
}
public resultsList() {
  return this.http.get<Blob[]>(`${this.DJANGO_SERVER}/file/results/list/${this.session}`);
}

/*!
* @brief <brief description of generate function>
* @param type:boolean cpp defines whether the files to be processed are cpp files or not
* @return type:<return type daalna idhar> <kya return ho raha?>
*/
function generate(cpp){
}
public generate(cpp: boolean) {
  if(cpp) return this.http.get(`${this.DJANGO_SERVER}/file/results/generate/true/${this.session}`);
  else return this.http.get(`${this.DJANGO_SERVER}/file/results/generate/false/${this.session}`);
}

/*!
* @brief <brief description of getImage function>
* @return type:Observable<Blob> <kya return ho raha?>
*/
function getImage(){
}
public getImage(): Observable<Blob> {
  return this.http.get(`${this.DJANGO_SERVER}/file/plots/show/${this.session}`, {responseType: 'blob'});
}

/*!
* @brief <brief description of getMarkers function>
* @return type:<return type daalna idhar> <kya return ho raha?>
*/
function getMarkers(){
}
public getMarkers() {
  return this.http.get(`${this.DJANGO_SERVER}/file/plots/marker/${this.session}`, {responseType: 'text' as 'json'});
}

/*!
* @brief <brief description of getHeat function>
* @return type:Observable<Blob> <kya return ho raha?>
*/
function getHeat(){
}
public getHeat(): Observable<Blob> {
  return this.http.get(`${this.DJANGO_SERVER}/file/plots/heat/${this.session}`, {responseType: 'blob'});
}

/*!
* @brief <brief description of sendList function>
* @param type:<formData ka type daalna idhar> formData <formData kya hai?>
* @return type:<return type daalna idhar> <kya return ho raha?>
*/
function sendList(formData){
}
public sendList(formData) {
  return this.http.post<any>(`${this.DJANGO_SERVER}/file/plots/list/${this.session}`, formData);
}

/*!
* @brief <brief description of someplot function>
* @return type:<return type daalna idhar> <kya return ho raha?>
*/
function someplot(){
}
public someplot() {
  return this.http.get(`${this.DJANGO_SERVER}/file/plots/some/${this.session}`, {responseType: 'blob'});
}

/*!
* @brief <brief description of deleteplots function>
* @return type:<return type daalna idhar> <kya return ho raha?>
*/
function deleteplots(){
}
public deleteplots() {
  return this.http.delete(`${this.DJANGO_SERVER}/file/plots/delete/${this.session}`);
}
