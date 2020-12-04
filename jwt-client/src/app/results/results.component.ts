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
  iscpp = false;

  Files: Blob[]=[];
  imageToShow: any;
  Heat: any;
  Text: any;
  TextURL: any;

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
    var blob = new Blob([data],{type: 'text/csv'});
    //var url = window.URL.createObjectURL(blob);
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
    this.fileService.generate(this.iscpp)
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
  } 

  isImageLoading = true;
  getImageFromService() {
    
    this.isImageLoading = true;
    this.fileService.getImage().subscribe(data => {
      this.createImageFromBlob(data);
      this.getMarkersFromService();
      this.isImageLoading = false;
    }, error => {
      console.log(error);
      this.isImageLoading = false;
    });
  }

  createMarkers(data) {
    var blob = new Blob([data],{type: 'text/txt'})
    var url = window.URL.createObjectURL(blob);
    //url=url.substring(5)
    this.TextURL = this.domSanitizer.bypassSecurityTrustResourceUrl(url)
  }

  getMarkersFromService() {
    this.fileService.getMarkers().subscribe(data =>{
      this.createMarkers(data);
      this.Text=data;
      this.getHeatFromService();
    }, error => {
      console.log(error);
    });
  }


  createHeat(image: Blob) {
    var blob = new Blob([image],{type: 'image/png'})
    var url = window.URL.createObjectURL(blob);
    //url=url.substring(5)
    this.Heat = this.domSanitizer.bypassSecurityTrustUrl(url)
  }

  getHeatFromService() {
    this.fileService.getHeat().subscribe(data =>{
      this.createHeat(data);
    }, error => {
      console.log(error);
    });
  }

  toggle() {
    this.iscpp = !this.iscpp;
  }

//downLoadFile(data: any) {
  //var blob = new Blob([data],{type: 'text/*'});
  //var url = window.URL.createObjectURL(blob);
  //saveAs(blob,"results.csv");
  //window.open(url);
//}
 
}
