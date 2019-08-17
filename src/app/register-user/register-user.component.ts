import { Component, OnInit } from '@angular/core';
import { AuthServiceService } from '../auth-service.service';

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
  constructor(private authService: AuthServiceService) { }

  ngOnInit() {}

  registerUser() {
    this.authService.register_user('AbdulRahmen', 'Mustafa', 'test@gmail.com', 'armustafa', '12345', '6179094230')
    .subscribe(results => {
      console.log(results);
    }, err => {
      console.log(err);
    });
  }

}
