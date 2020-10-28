import { Injectable } from '@angular/core';
import { BehaviorSubject, Subject, Observable } from 'rxjs';
import { finalize } from 'rxjs/operators';
import { HttpClient } from '@angular/common/http';
import { saveAs } from 'file-saver';

const baseUrl = 'http://localhost:10101';

@Injectable({
 providedIn: 'root'
})
export class FileService {
 private fileList: string[] = new Array<string>();
 private fileList$: Subject<string[]> = new Subject<string[]>();
 private displayLoader$: Subject<boolean> = new BehaviorSubject<boolean>(false);

 constructor(private http: HttpClient) { }

 public isLoading(): Observable<boolean> {
   return this.displayLoader$;
 }

 public upload(fileName: string, fileContent: string): void {
   this.displayLoader$.next(true);
   this.http.put(baseUrl + '/files', {name: fileName, content: fileContent})
   .pipe(finalize(() => this.displayLoader$.next(false)))
   .subscribe(res => {
     this.fileList.push(fileName);
     this.fileList$.next(this.fileList);
   }, error => {
     this.displayLoader$.next(false);
   });
 }

 public download(fileName: string): void {
   this.http.get(baseUrl + '/files/${fileName}', {params: {file: fileName}, responseType: 'blob'}).subscribe(
     res => {
       saveAs(res,fileName);
   });
 }

 public remove(fileName: string): void {
   this.http.delete(baseUrl + '/files/${fileName}', {params: {fileName: fileName}}).subscribe(() => {
     this.fileList.splice(this.fileList.findIndex(name => name === fileName), 1);
     this.fileList$.next(this.fileList);
   });
 }

 public list(): Observable<string[]> {
   return this.fileList$;
 }

 private addFileToList(fileName: string): void {
   this.fileList.push(fileName);
   this.fileList$.next(this.fileList);
 }
}
