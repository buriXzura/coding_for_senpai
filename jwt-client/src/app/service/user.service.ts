import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FileLikeObject } from 'ng2-file-upload';
import { BehaviorSubject, Subject, Observable } from 'rxjs';

@Injectable({
 providedIn: 'root'
})
export class UserService {
  DJANGO_SERVER: string = "http://127.0.0.1:8000";
  session: string = "rahul";
  constructor(private http: HttpClient) { }

public DownloadFiles() {

    return this.http.get(`${this.DJANGO_SERVER}/file/results/download/${this.session}`, {responseType: 'arraybuffer'});


}
}

