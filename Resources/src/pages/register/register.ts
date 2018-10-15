import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';

import { FormBuilder, FormGroup, FormControl } from '@angular/forms';

import { AuthService } from '../core/auth.service';

import { UserPage } from '../user/user';

import { AngularFirestore } from 'angularfire2/firestore';


@Component({
  selector: 'page-register',
  templateUrl: 'register.html'
})
export class RegisterPage {

  registerForm: FormGroup;
  errorMessage: string = '';
  successMessage: string = '';

  constructor(
    public navCtrl: NavController,
    public authService: AuthService,
    public formBuilder: FormBuilder,
    public firestore: AngularFirestore
  ) { }

  createUser(
    first:any,
    last:any,
    email: any
  ): Promise<void> {
    const id = this.firestore.createId();
    console.log(id);
    return this.firestore.doc(`users/${id}`).set({
      id,
      first,
      last,
      email
    });
  }

  ionViewWillLoad() {
    this.registerForm = this.formBuilder.group({
      first: new FormControl(),
      last: new FormControl(),
      email: new FormControl(),
      password: new FormControl()
    });
  }

  tryRegister(value) {
    this.authService.doRegister(value)
      .then(res => {
        this.errorMessage = "";
        console.log(value);
        this.createUser(value.first,value.last,value.email);
        this.successMessage = "Your account has been created. Please log in now.";
      }, err => {
        this.errorMessage = err.message;
        this.successMessage = "";
      })
  }

  tryFacebookLogin() {
    this.authService.doFacebookLogin()
      .then((res) => {
        this.navCtrl.push(UserPage);
      }, (err) => {
        this.errorMessage = err.message;
      });
  }

  tryGoogleLogin() {
    this.authService.doGoogleLogin()
      .then((res) => {
        this.navCtrl.push(UserPage);
      }, (err) => {
        this.errorMessage = err.message;
      });
  }

  tryTwitterLogin() {
    this.authService.doTwitterLogin()
      .then((res) => {
        this.navCtrl.push(UserPage);
      }, (err) => {
        this.errorMessage = err.message;
      });
  }

  goLoginPage() {
    this.navCtrl.pop();
  }

}
