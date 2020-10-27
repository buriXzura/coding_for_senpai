import { Component, OnInit } from '@angular/core';
import { FileService } from '../service/file.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-file-list',
  templateUrl: './file-list.component.html',
  styleUrls: ['./file-list.component.css']
})
export class FileListComponent implements OnInit {


  constructor(private fileService: FileService) { }

  ngOnInit(): void {
  }


}
