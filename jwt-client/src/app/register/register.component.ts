import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ServerService } from '../server.service';

@Component({
  selector: 'app-login',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  form: FormGroup;
  message: string;

  constructor(
    private fb: FormBuilder,
    private server: ServerService,
    private router: Router
  ) {}

  ngOnInit() {
    this.form = this.fb.group({
      email: ['', Validators.email],
      name: ['', Validators.required],
      orgname: ['', Validators.required],
      password: ['', Validators.compose([Validators.required, Validators.minLength(8)])],
      ckpassword: ['', Validators.compose([Validators.required, Validators.minLength(8)])]
    },);
    this.message = "";
  }

  onSubmit() {
    this.message = 'Submitting...';
    console.log('Submitting');
    if (!this.form.valid) {
      console.log('Information not valid. Please check that fields are correctly filled in.');
      this.message = 'Form not valid. Please check that fields are correctly filled in.';
      return;
    }

    else if((this.form.get('password').value)!=(this.form.get('ckpassword').value)) {
      this.message = 'Passwords do not match. Please try again.';
      return;
    }

    this.message = 'Form valid!';
    console.log('Form valid');
    const request = this.server.request('POST', '/register', {
      email: this.form.get('email').value,
      name: this.form.get('name').value,
      password: this.form.get('password').value,
      orgname: this.form.get('orgname').value
    });

    request.subscribe(
      data => {
        this.message = "Registration completed successfully!";
        setTimeout(() => {this.router.navigate(['/login']);},3000);
      },
      error => {this.message = "Please try again. The email you entered is already in use or the organisation you entered is not registered with us.";}
    );
  }
}
