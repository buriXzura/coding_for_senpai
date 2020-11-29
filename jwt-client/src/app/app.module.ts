import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RegisterComponent } from './register/register.component';
import { LoginComponent } from './login/login.component';
import { ProfileComponent } from './profile/profile.component';

import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FileUploadModule } from 'ng2-file-upload';
import { AuthService } from './auth.service';
import { AuthGuardService } from './auth-guard.service';
import { ChngpswdComponent } from './chngpswd/chngpswd.component';
import { HomeComponent } from './home/home.component';
import { UploadComponent } from './upload/upload.component';
import { DeleteComponent } from './delete/delete.component';
import { StubComponent } from './stub/stub.component';
import { MainComponent } from './main/main.component';
import { ResultsComponent } from './results/results.component';

@NgModule({
  declarations: [
    AppComponent,
    RegisterComponent,
    LoginComponent,
    ProfileComponent,
    ChngpswdComponent,
    HomeComponent,
    UploadComponent,
    DeleteComponent,
    StubComponent,
    MainComponent,
    ResultsComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    FileUploadModule,
    BrowserAnimationsModule
  ],
  providers: [AuthService, AuthGuardService],
  bootstrap: [AppComponent]
})
export class AppModule { }
