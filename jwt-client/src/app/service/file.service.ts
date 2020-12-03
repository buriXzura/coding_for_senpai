import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FileLikeObject } from 'ng2-file-upload';
import { BehaviorSubject, Subject, Observable } from 'rxjs';

@Injectable({
 providedIn: 'root'
})
export class FileService {
  DJANGO_SERVER: string = "http://127.0.0.1:8000";
  session: string = "rahul";
  constructor(private http: HttpClient) { }

  public upload(formData) {
    return this.http.post<any>(`${this.DJANGO_SERVER}/file/upload`, formData);
  }

  public download(formData) {
    return this.http.post<any>(`${this.DJANGO_SERVER}/file/download`, formData);
  }

  public list() {
    return this.http.get<Blob[]>(`${this.DJANGO_SERVER}/file/list/${this.session}`);
  }

  public delete(id) {
    return this.http.delete(`${this.DJANGO_SERVER}/file/delete/${id}`);
  }

  public deleteall() {
    return this.http.delete(`${this.DJANGO_SERVER}/file/deleteall/${this.session}`);
  }

  public delete1() {
    return this.http.delete(`${this.DJANGO_SERVER}/file/stub/delete/${this.session}`);
  }

  public deleteResults() {
    return this.http.delete(`${this.DJANGO_SERVER}/file/results/delete/${this.session}`);
  }

  public List1() {
    return this.http.get<Blob[]>(`${this.DJANGO_SERVER}/file/stub/list/${this.session}`);
  }

  public resultsList() {
    return this.http.get<Blob[]>(`${this.DJANGO_SERVER}/file/results/list/${this.session}`);
  }

}