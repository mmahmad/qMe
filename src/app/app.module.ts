import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { FormsModule } from '@angular/forms';
import { LoginComponent } from './login/login.component';

import { RouterModule, Routes } from '@angular/router';
import { RegisterCompanyComponent } from './register-company/register-company.component';
import { RegisterEmployeeComponent } from './register-employee/register-employee.component';
import { RegisterUserComponent } from './register-user/register-user.component';

import { HttpClientModule } from '@angular/common/http';

const appRoutes: Routes = [
  { path: 'login/', component: LoginComponent },
  // { path: 'hero/:id',      component: HeroDetailComponent },
  // {
  //   path: 'heroes',
  //   component: HeroListComponent,
  //   data: { title: 'Heroes List' }
  // },
  // { path: '',
  //   redirectTo: '/',
  //   pathMatch: 'full'
  // },
  { path: '**', component: AppComponent }
];

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegisterCompanyComponent,
    RegisterEmployeeComponent,
    RegisterUserComponent
  ],
  imports: [
    RouterModule.forRoot(
      appRoutes,
      { enableTracing: true } // <-- debugging purposes only
    ),
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
