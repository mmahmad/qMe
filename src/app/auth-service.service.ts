import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthServiceService {

  constructor(private http: HttpClient) {}

  register_user(firstName: string, lastName: string, userEmail: string, userName: string, userPassword: string, phoneNumber: string ) {
    return this.http.post('localhost:5000/register',
    {
      fname: firstName,
      lname: lastName,
      email: userEmail,
      username: userName,
      password: userPassword,
      phone_number: phoneNumber
    });
  }
}
