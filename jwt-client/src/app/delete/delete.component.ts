import { Component, OnInit } from '@angular/core';
import { FileService } from '../service/file.service';
import {ThemePalette} from '@angular/material/core';

export interface Task {
  completed: boolean;
  subtasks?: Task[];
}

@Component({
  selector: 'app-delete',
  templateUrl: './delete.component.html',
  styleUrls: ['./delete.component.css']
})
export class DeleteComponent implements OnInit {

  Files: Blob[]=[];

  constructor(private fileService: FileService) { }

  ngOnInit(): void {
    this.fileService.list()
      .subscribe( files => {this.Files=files; this.createarray();} );
    
    
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

  // task: Task = {
  //   completed: false,
  //   subtasks: [
  //     {completed: false},
  //     {completed: false},
  //     {completed: false}
  //   ]
  // };

  // allComplete: boolean = false;

  // updateAllComplete() {
  //   this.allComplete = this.task.subtasks != null && this.task.subtasks.every(t => t.completed);
  // }

  // someComplete(): boolean {
  //   if (this.task.subtasks == null) {
  //     return false;
  //   }
  //   return this.task.subtasks.filter(t => t.completed).length > 0 && !this.allComplete;
  // }

  // setAll(completed: boolean) {
  //   this.allComplete = completed;
  //   if (this.task.subtasks == null) {
  //     return;
  //   }
  //   this.task.subtasks.forEach(t => t.completed = completed);
  // }

}
