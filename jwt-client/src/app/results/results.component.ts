import { Component, OnInit } from '@angular/core';
import { FileService } from '../service/file.service';
import { UserService } from '../service/user.service';
import { FileUploader, FileLikeObject } from 'ng2-file-upload';
import { concat } from  'rxjs';
import { saveAs } from 'file-saver';

@Component({
  selector: 'app-results',
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.css']
})
export class ResultsComponent implements OnInit {

  public uploader: FileUploader = new FileUploader({ });
  public hasBaseDropZoneOver: boolean = false;
  sss: string = "rahul/results";

  Files: Blob[]=[];

  constructor(private fileService: FileService,private userService: UserService) { }

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
    this.fileService.resultsList()
      .subscribe(
        files => this.Files=files
      )
  }
  downLoadFile(data: any) {
    var blob = new Blob([data],{type: 'text/*'});
    var url = window.URL.createObjectURL(blob);
    saveAs(blob,"results.csv");
    window.open(url);

}
  DownloadFile(){

    this.userService.DownloadFiles()
        .subscribe(
            (data) => this.downLoadFile(data)), // console.log(data),
            (error) => console.log("Error downloading the file."),
            () => console.info("OK");
}
  
  delete(){
    this.fileService.deleteResults()
      .subscribe( () => this.Files=[] )
  }

  name(file){
    return file.split('/').pop()
  }
 
}
