import { Component, OnInit } from '@angular/core';
import { ServerService } from '../server.service';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { CanActivate, Router, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-chngpswd',
  templateUrl: './chngpswd.component.html',
  styleUrls: ['./chngpswd.component.css']
})
export class ChngpswdComponent implements OnInit {

  form: FormGroup;
  public chngInvalid: boolean;
  private formSubmitAttempt: boolean;
  email: string;
  message: string;

  constructor(private fb: FormBuilder, private server: ServerService,
    private authService: AuthService, private router: Router) { }

  ngOnInit() {
    this.form = this.fb.group({
      password: ['', Validators.required],
      newpswd: ['', Validators.compose([Validators.required, Validators.minLength(8)])],
      confpswd: ['', Validators.compose([Validators.required, Validators.minLength(8)])]
    },);
    this.message = "";
    this.server.request('GET', '/profile').subscribe((user: any) => {
      if (user) {
        this.email = user.email;
      }
    });
  }

  onSubmit() {

    this.message = 'Submitting...';

    if (!this.form.valid) {
      console.log('Information not valid. Please check that fields are correctly filled in.');
      this.message = 'Error. Please make sure the format of your input is correct.';
      return;
    }

    this.message = 'Form valid!';

    this.server.request('POST', '/chngchk', {
      email: this.email, password: this.form.get('password').value}).subscribe(data => {
      if (data) {

        this.message = "Current password verified. Continuing...";

        if(this.form.get('password').value==this.form.get('newpswd').value) {
          this.message = "Error. Please enter a new password that differs from your current password.";
          return;
        }

        if(this.form.get('newpswd').value!=this.form.get('confpswd').value) {
          this.message = "Error. Please make sure you have entered the new password correctly both times.";
          return;
        }

        this.server.request('POST', '/chngpswd', {
          email: this.email, password: this.form.get('newpswd').value}).subscribe( data => {
            if (data) {
              this.message = "Password change successful!";
              setTimeout(() => {this.router.navigate(['/profile']);},3000);
            }
          },
          error => {
            this.message = "Sorry, an error occured. Please try again later.";
            return;
          }
        );

      }},
      error => {
        this.message = "You have entered your current password incorrectly. Please try again.";
        return;
      }
    );

  }

}
