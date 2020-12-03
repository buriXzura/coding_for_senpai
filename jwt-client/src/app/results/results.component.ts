import { Component, OnInit } from '@angular/core';
import { FileService } from '../service/file.service';
import { FileUploader, FileLikeObject } from 'ng2-file-upload';
import { concat } from  'rxjs';
import { saveAs } from 'file-saver';

@Component({
  selector: 'app-results',
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.css']
})
export class ResultsComponent implements OnInit {

  sss: string = "rahul/results";

  Files: Blob[]=[];

  constructor(private fileService: FileService) { }

  ngOnInit(): void {
    this.get_results();
  }


  get_results(){
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
    this.fileService.DownloadResults()
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
