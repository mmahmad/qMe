import { Component } from '@angular/core';
import { Router } from '@angular/router';
// import { FormGroup, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'qMe';
  // form: FormGroup;

  // constructor(private fb: FormBuilder, private authService: AuthService, private router: Router) {
    // constructor(private fb: FormBuilder, private router: Router) {{}

// this.form = this.fb.group({
// email: ['', Validators.required],
// password: ['', Validators.required]
// });
// }

// login() {
//   const val = this.form.value;

//   if (val.email && val.password) {
//       this.authService.login(val.email, val.password)
//           .subscribe(
//               () => {
//                   console.log('User is logged in');
//                   this.router.navigateByUrl('/');
//               }
//           );
//   }
// }

}
