import { Injectable } from '@angular/core';
import { HttpClientModule, HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthServiceService {

  constructor(private http: HttpClient) {}

//   login(email: string, password: string ) {
//     return this.http.post<User>('localhost:5000/auth', {email, password})
//         // this is just the HTTP call, 
//         // we still need to handle the reception of the token
//         .shareReplay();
// }
}
