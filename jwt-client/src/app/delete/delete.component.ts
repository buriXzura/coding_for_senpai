import { Component, OnInit } from '@angular/core';
import { FileService } from '../service/file.service';


@Component({
  selector: 'app-delete',
  templateUrl: './delete.component.html',
  styleUrls: ['./delete.component.css']
})
export class DeleteComponent implements OnInit {

  Files: Blob[];

  constructor(private fileService: FileService) { }

  ngOnInit(): void {
    this.fileService.list()
      .subscribe( files => this.Files=files )
  }

  delete(file) {
    const index = this.Files.indexOf(file);
    this.fileService.delete(file.id)
      .subscribe(
        () => this.Files.splice(index,1)
      )
  }

  deleteall() {
    this.fileService.deleteall()
      .subscribe(
        () => this.Files.splice(0,this.Files.length)
      )
  }

  name(file){
    return file.split('/').pop()
  }

}
