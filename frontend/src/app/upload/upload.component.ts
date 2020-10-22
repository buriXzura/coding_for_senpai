import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { FileService } from '../service/file.service';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css']
})
export class UploadComponent implements OnInit {

  public formGroup = this.fb.group({
    file: [null, Validators.required]
  });
 
  private fileName;

  constructor(private fb: FormBuilder, private fileService: FileService) { }

  ngOnInit(): void {
  }

  public onFileChange(event) {
    const reader = new FileReader();
 
    if (event.target.files && event.target.files.length) {
      this.fileName = event.target.files[0].name;
      const [file] = event.target.files;
      reader.readAsDataURL(file);
     
      reader.onload = () => {
        this.formGroup.patchValue({
          file: reader.result
        });
      };
    } 
  }

  public onSubmit(): void {
    this.fileService.upload(this.fileName, this.formGroup.get('file').value);
  }
  
}