import { Injectable } from '@angular/core';
import { Observable, of, throwError } from 'rxjs';
import { CanActivate, Router, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';
import { AuthService } from './auth.service';

@Injectable()
export class AuthGuardService implements CanActivate {

  routeURL: string;

  constructor(private authService: AuthService, private router: Router) {
    this.routeURL = this.router.url;
  }

  canActivate( route: ActivatedRouteSnapshot, state: RouterStateSnapshot):
  Observable<boolean>|Promise<boolean>|boolean {

      return new Promise((resolve, reject) => {
        if(!this.authService.authorized) {
          this.routeURL = '/login';
          this.router.navigate(['/login'], {queryParams: {return: 'login'}});
          return resolve(false);
        } else {
          this.routeURL = this.router.url;
          return resolve(true);
        }
      });
    }
}
