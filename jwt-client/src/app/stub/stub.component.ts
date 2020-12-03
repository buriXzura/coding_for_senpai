import { Component, OnInit } from '@angular/core';
import { FileService } from '../service/file.service';
import { FileUploader, FileLikeObject } from 'ng2-file-upload';
import { concat } from  'rxjs';

@Component({
  selector: 'app-stub',
  templateUrl: './stub.component.html',
  styleUrls: ['./stub.component.css']
})
export class StubComponent implements OnInit {

  public uploader: FileUploader = new FileUploader({ });
  public hasBaseDropZoneOver: boolean = false;
  sss: string = "rahul/stub";
  Filess: Blob[] = [];

  constructor(private fileService: FileService) { }

  ngOnInit(): void {
    this.get_stubs();
  }

  fileOverBase(event): void {
    this.hasBaseDropZoneOver = event;
  }

  getFiles(): FileLikeObject[] {
    return this.uploader.queue.map((fileItem) => {
      return fileItem.file;
    });
  }

  upload() {
    let files = this.getFiles();
    console.log(files);
    let requests = [];
    files.forEach((file) => {
      let formData = new FormData();
      formData.append('file', file.rawFile, file.name);
      formData.append('session',this.sss);
      requests.push(this.fileService.upload(formData));
    });
    
    concat(...requests).subscribe(
      (res) => {
      	this.uploader.queue.shift();
        console.log(res);
        this.get_stubs();
      },
      (err) => {
      	alert("Something went wrong TT__TT")
        console.log(err);
      }
    );
  }

  get_stubs(){
    this.fileService.List1()
      .subscribe(
        files => this.Filess=files
      )
  }

  delete(){
    this.fileService.delete1()
      .subscribe( () => this.Filess=[] )
  }

  name(file){
    return file.split('/').pop()
  }

}
