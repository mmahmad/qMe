import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-register-user',
  templateUrl: './register-user.component.html',
  styleUrls: ['./register-user.component.scss']
})
export class RegisterUserComponent implements OnInit {

  user = {
    username: '',
    password: '',
    confirm_password: '',
    email: '',
    phone_number: ''
  };
  constructor() { }

  ngOnInit() {
  }

}
