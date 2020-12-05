import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { CanActivate, Router, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  form: FormGroup;
  public loginInvalid: boolean;
  private formSubmitAttempt: boolean;
  message: string;

  constructor(private fb: FormBuilder, private authService: AuthService, private router: Router) {
  }

  ngOnInit() {
    if(this.authService.isLoggedIn) {this.authService.logout();}
    this.form = this.fb.group({
      email: ['', Validators.email],
      password: ['', Validators.required],
      orgpswd: ['', Validators.required]
    });
    this.message = "";
  }

  async onSubmit() {
    this.loginInvalid = false;
    this.formSubmitAttempt = false;
    if (this.form.valid) {
      try {
        await this.authService.login(this.form.value);
        this.loginInvalid = true;
      } catch (err) {
        this.loginInvalid = true;
      }
    } else {
      this.formSubmitAttempt = true;
      this.message = "Data entered has invalid format. Please try again.";
    }
    if(this.loginInvalid) {this.message = "Invalid email or password. Please try again.";}
  }

}
