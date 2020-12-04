import { Component, OnInit } from '@angular/core';
import { FileService } from '../service/file.service';
import { FileUploader, FileLikeObject } from 'ng2-file-upload';
import { concat, from } from  'rxjs';
import { saveAs } from 'file-saver';
import { DomSanitizer } from '@angular/platform-browser'


@Component({
  selector: 'app-results',
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.css']
})
export class ResultsComponent implements OnInit {

  sss: string = "rahul/results";

  Files: Blob[]=[];
  imageToShow: any;

  constructor(private fileService: FileService,
      private domSanitizer: DomSanitizer,
    ) { }

  ngOnInit(): void {
    this.get_results();
    //this.getImageFromService();
  }


  get_results(){
    this.fileService.resultsList()
      .subscribe(
        files => this.Files=files
      )
  }

  downLoadFile(data: any) {
    var blob = new Blob([data],{type: 'text/txt'});
    var url = window.URL.createObjectURL(blob);
    saveAs(blob,"results.csv");
    //window.open(url);
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

  generate() {
    this.fileService.generate()
      .subscribe(
        () => this.get_results()
      )
  }

  PlotShow() {
    this.fileService.getImage()
      .subscribe(
      )
  }

  createImageFromBlob(image: Blob) {
    var blob = new Blob([image],{type: 'image/png'})
    var url = window.URL.createObjectURL(blob);
    //url=url.substring(5)
    this.imageToShow = this.domSanitizer.bypassSecurityTrustUrl(url)
    //alert(url)
    //window.open(url)
    /*
    let reader = new FileReader();
    reader.addEventListener("load", () => {
       this.imageToShow = reader.result;
    }, false);

    if (image) {
       reader.readAsDataURL(image);
    }*/
    //alert(this.imageToShow)
  } 

  isImageLoading = true;
  getImageFromService() {
    
    this.isImageLoading = true;
    this.fileService.getImage().subscribe(data => {
      this.createImageFromBlob(data);
      this.isImageLoading = false;
    }, error => {
      console.log(error);
      this.isImageLoading = false;
    });
  }
//downLoadFile(data: any) {
  //var blob = new Blob([data],{type: 'text/*'});
  //var url = window.URL.createObjectURL(blob);
  //saveAs(blob,"results.csv");
  //window.open(url);
//}
 
}
