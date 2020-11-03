import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { ProfileComponent } from './profile/profile.component';
import { ChngpswdComponent } from './chngpswd/chngpswd.component';
import { HomeComponent } from './home/home.component';
import { UploadComponent } from './upload/upload.component';
import { MainComponent } from './main/main.component';
import { AuthGuardService } from './auth-guard.service';

const routes: Routes = [
  { path: '', component: LoginComponent },
  { path: 'login', component: LoginComponent},
  { path: 'register', component: RegisterComponent },
  { path: 'upload', component: UploadComponent, canActivate: [AuthGuardService]},
  { path: 'profile', component: ProfileComponent, canActivate: [AuthGuardService]},
  { path: 'chngpswd', component: ChngpswdComponent, canActivate: [AuthGuardService]},
  { path: 'home', component: HomeComponent, canActivate: [AuthGuardService]},
  { path: 'main', component: MainComponent, canActivate: [AuthGuardService]},
  { path: '**', redirectTo: '' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
