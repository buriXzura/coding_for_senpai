import { Component, OnInit, EventEmitter, Output } from '@angular/core';
import { FileService } from '../service/file.service';
import { ServerService } from '../server.service';

@Component({
  selector: 'app-delete',
  templateUrl: './delete.component.html',
  styleUrls: ['./delete.component.css']
})
export class DeleteComponent implements OnInit {

  Files: any=[];

  constructor(private fileService: FileService, private server: ServerService) { }

  ngOnInit(): void {
    this.server.request('GET', '/profile').subscribe((user: any) => {
      if (user) {
        this.fileService.get_session(user.email);
        this.fileService.list()
          .subscribe( files => {this.Files=files; this.createarray();} );
      }
    });
    
  }

  delete(file) {
    const index = this.Files.indexOf(file);
    this.fileService.delete(file.id)
      .subscribe(
        () => {this.Files.splice(index,1); this.createarray();}
      )
  }

  deleteall() {
    this.fileService.deleteall()
      .subscribe(
        () => {this.Files.splice(0,this.Files.length); this.createarray();}
      )
  }

  name(file){
    return file.split('/').pop()
  }

  allComplete=true;
  complete: boolean[];
  checked: number;

  createarray(){
    this.complete=new Array<boolean>(this.Files.length);
    for(let i=0 ; i<this.Files.length ; i++){
      this.complete[i]=true;
    }
    this.checked=this.Files.length;
    this.allComplete=true;
  }

  
  toggleall(){
    if(this.allComplete){
      for(let i=0 ; i<this.Files.length ; i++){
        this.complete[i]=false;
      }
      this.allComplete=false;
    }
    else{
      for(let i=0 ; i<this.Files.length ; i++){
        this.complete[i]=true;
      }
      this.allComplete=true;
    }
  }

  updatecheckall(index){
    if(this.complete[index]){
      this.complete[index]=false;
      if(this.allComplete){
        this.allComplete=false;
      }
      this.checked-=1;
    }
    else{
      this.complete[index]=true;
      this.checked+=1;
      if(this.checked==this.Files.length){
        this.allComplete=true;
      }
    }
  }

  @Output() allPlot = new EventEmitter();
  @Output() someplots = new EventEmitter<String[]>();

  
  
  listSelected(){
    if(this.allComplete) {
        this.allPlot.emit();
    }
    else {
      if (this.checked<=1){
        alert("Select more than 1 file.")
      }
      else{
        let lst = new Array<String>(this.checked);
        let j=0;

        for( let i = 0; i < this.Files.length; i++ ){
          if(this.complete[i]){
            lst[j++] = this.name(this.Files[i].file);
            //this.someplots.emit(this.Files[i]);
            //break;
          }
        }
        this.someplots.emit(lst);
      }
    }
  }

}
