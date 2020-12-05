import { Component, OnInit } from '@angular/core';
import { FileUploader, FileLikeObject } from 'ng2-file-upload';
import { concat } from  'rxjs';
import { FileService } from '../service/file.service';
import { ServerService } from '../server.service';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css']
})
export class UploadComponent implements OnInit {

  public uploader: FileUploader = new FileUploader({ });
  public hasBaseDropZoneOver: boolean = false;
  temp: string = "rahul";

  constructor(
    private fileService: FileService, private server: ServerService,
    ) {}

  ngOnInit() : void {}

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
    this.server.request('GET', '/profile').subscribe((user: any) => {
      if (user) {
        this.temp = user.email;
        files.forEach((file) => {
          let formData = new FormData();
          formData.append('file', file.rawFile, file.name);
          formData.append('session',this.temp);
          requests.push(this.fileService.upload(formData));
        });
    
        concat(...requests).subscribe(
          (res) => {
            this.uploader.queue.shift();
            console.log(res);
          },
          (err) => {
            alert("Something went wrong TT__TT")
            console.log(err);
          }
        );
      }
    });
    
  }

}
