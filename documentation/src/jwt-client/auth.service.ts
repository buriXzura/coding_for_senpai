/*!
* @file auth.service.ts
* @brief Authentication service for frontend.
*/

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

  //! Checks if the current session is authenticated
  get isLoggedIn() {
    /*!
    * @function Checks if the current session is authenticated
    * @return isLoggedIn(): Observable indicating whether user is logged in
    */
    return this.loggedIn.asObservable();
  }

  //! Initializes the authorization state
  constructor(private router: Router, private server: ServerService, private fileService: FileService) {

    //! user data retrieved from local storage
    console.log('Auth Service');
    const userData = localStorage.getItem('user');

    //! default authorization set to false
    this.authorized = false;

    //! if user data is present, set authorization/login status to true
    if (userData) {
      console.log('Logged in from memory');
      const user = JSON.parse(userData);
      //!retrieve the JWT from the user data and use it to set login status to true on the server
      this.token = user.token;
      this.server.setLoggedIn(true, this.token);
      this.loggedIn.next(true);
      this.authorized = true;
    }
  }

  //! Login method
  login(user) {
    /*!
    * @param userData user (in login()): user data entered on login page
    * @return login(): error if login fails, else reroutes user to homepage
    */

    //! if the form is not empty
    if (user.email !== '' && user.password !== '' && user.orgpswd !== '' ) {

      //! send user data to the server and catch the response
      return this.server.request('POST', '/login', {
        email: user.email,
        password: user.password,
        orgpswd: user.orgpswd
      }).subscribe((response: any) => {
        if (response.auth === true && response.token !== undefined) {

          //! if the response indicates the user is authorized,
          //! set the current session token to the returned token
          this.token = response.token;

          //! use the token to set login status to true on the server
          this.server.setLoggedIn(true, this.token);
          this.loggedIn.next(true);
          this.authorized = true;

          //! store the token into the userData
          const userData = {
            token: this.token,
          };
          localStorage.setItem('user', JSON.stringify(userData));

          //! navigate to the homepage
          this.router.navigateByUrl('/home');
        }
      },
      error => {return error;}
    );
    }
  }

  //! Logout method
  logout() {

    //! via the fileservice, delete all files uploaded/created on the file server
    //! during the current user's session
    this.fileService.deleteplots().subscribe(
        () => {this.fileService.deleteResults().subscribe(
              () => {this.fileService.delete1().subscribe(
                    () => {this.fileService.deleteall().subscribe(
                          () => {

                            //! set login status to false on the authentication server
                            this.server.setLoggedIn(false);

                            //! delete the current session token
                            delete this.token;
                            this.loggedIn.next(false);
                            this.authorized = false;

                            //! clear the local storage
                            localStorage.clear();

                            //! reroute the user to the login page
                            this.router.navigate(['/']);
                          })
                    })
              })
        });
    }

}
