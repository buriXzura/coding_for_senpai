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

  public list() {
    return this.http.get<Blob[]>(`${this.DJANGO_SERVER}/file/list/${this.session}`);
  }

  public delete(id) {
    return this.http.delete(`${this.DJANGO_SERVER}/file/delete/${id}`);
  }

  public deleteall() {
    return this.http.delete(`${this.DJANGO_SERVER}/file/deleteall/${this.session}`);
  }

  public deleteStub() {
    return this.http.delete(`${this.DJANGO_SERVER}/file/stub/delete/${this.session}`);
  }

  public stubList() {
    return this.http.get<Blob[]>(`${this.DJANGO_SERVER}/file/stub/list/${this.session}`);
  }

}