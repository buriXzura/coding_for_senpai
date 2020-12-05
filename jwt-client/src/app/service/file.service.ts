
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { FileLikeObject } from 'ng2-file-upload';
import { BehaviorSubject, Subject, Observable } from 'rxjs';
import {map} from 'rxjs/operators';

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

  public DownloadResults() {
    return this.http.get(`${this.DJANGO_SERVER}/file/results/download/${this.session}`, {responseType: 'arraybuffer'});
  }

  public list() {
    return this.http.get(`${this.DJANGO_SERVER}/file/list/${this.session}`);
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

  public generate(cpp: boolean) {
    if(cpp) return this.http.get(`${this.DJANGO_SERVER}/file/results/generate/true/${this.session}`);
    else return this.http.get(`${this.DJANGO_SERVER}/file/results/generate/false/${this.session}`);
  }

  public getImage(): Observable<Blob> {
    return this.http.get(`${this.DJANGO_SERVER}/file/plots/show/${this.session}`, {responseType: 'blob'});
  }

  public getMarkers() {
    return this.http.get(`${this.DJANGO_SERVER}/file/plots/marker/${this.session}`, {responseType: 'text' as 'json'});
  }

  public getHeat(): Observable<Blob> {
    return this.http.get(`${this.DJANGO_SERVER}/file/plots/heat/${this.session}`, {responseType: 'blob'});
  }

  public sendList(formData) {
    return this.http.post<any>(`${this.DJANGO_SERVER}/file/plots/list/${this.session}`, formData);
  }

  public someplot() {
    return this.http.get(`${this.DJANGO_SERVER}/file/plots/some/${this.session}`, {responseType: 'blob'});
  }

}
