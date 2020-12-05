import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { BehaviorSubject } from 'rxjs';
import { ServerService } from './server.service';
import { FileService } from './service/file.service';

@Injectable()
export class AuthService {
  private loggedIn = new BehaviorSubject<boolean>(false);
  private token: string;
  public authorized: boolean;

  get isLoggedIn() {
    return this.loggedIn.asObservable();
  }

  constructor(private router: Router, private server: ServerService, private fileService: FileService) {
    console.log('Auth Service');
    const userData = localStorage.getItem('user');
    this.authorized = false;
    if (userData) {
      console.log('Logged in from memory');
      const user = JSON.parse(userData);
      this.token = user.token;
      this.server.setLoggedIn(true, this.token);
      this.loggedIn.next(true);
      this.authorized = true;
    }
  }

  login(user) {
    if (user.email !== '' && user.password !== '' && user.orgpswd !== '' ) {
      return this.server.request('POST', '/login', {
        email: user.email,
        password: user.password,
        orgpswd: user.orgpswd
      }).subscribe((response: any) => {
        if (response.auth === true && response.token !== undefined) {
          this.token = response.token;
          this.server.setLoggedIn(true, this.token);
          this.loggedIn.next(true);
          this.authorized = true;
          const userData = {
            token: this.token,
          };
          localStorage.setItem('user', JSON.stringify(userData));
          this.router.navigateByUrl('/home');
        }
      },
      error => {return error;}
    );
    }
  }

  logout() {
    this.fileService.deleteall();
    this.fileService.delete1();
    this.fileService.deleteResults();
    this.fileService.deleteplots();

    this.server.setLoggedIn(false);
    delete this.token;

    this.loggedIn.next(false);
    this.authorized = false;
    localStorage.clear();
    this.router.navigate(['/']);
  }
}
