import { Component, OnInit } from '@angular/core';
import { FileService } from '../service/file.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-file-list',
  templateUrl: './file-list.component.html',
  styleUrls: ['./file-list.component.css']
})
export class FileListComponent implements OnInit {

  public fileList$: Observable<string[]> = this.fileService.list();

  constructor(private fileService: FileService) { }

  ngOnInit(): void {
  }

  public download(fileName: string): void {
    this.fileService.download(fileName);
  }

  public remove(fileName: string): void {
    this.fileService.remove(fileName);
  }

}
