import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { FirebaseProvider } from '../../providers/firebase/firebase';
import { LocationProvider } from '../../providers/location/location';
import { LoginPage } from '../login/login';
import { ToastController } from 'ionic-angular';


@IonicPage()
@Component({
  selector: 'page-signup',
  templateUrl: 'signup.html',
})
export class SignupPage {

  userData = {
    "username": "",
    "password": "",
    "first": "",
    "last": "",
    "email": ""
  };
  userLocation: any;

  constructor(public navCtrl: NavController, public db: FirebaseProvider, public location: LocationProvider, private toastCtrl: ToastController) {
    this.location.getPosition().then((data) => {
      let result = {
        message:"user location",
        page:"signup.ts",
        data:data,
      }
      console.log(result);
      this.userLocation = db.geopoint(data.coords.latitude, data.coords.longitude);
    });
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad SignupPage');
  }

  /**
   * Method: signup
   * Description: Adds a new user to firestore and also creates a subcollection with thier location
   * 
   */
  signUp() {
    this.db.add('users', this.userData).then((data) => {
      // data contains:
      // id: "Twryfmds9Ydll74rHRaT" (document id)
      // parent: CollectionReference (a parent reference)
      // path: "users/Twryfmds9Ydll74rHRaT" (path starting with highest level collection)
      let result = {
        message:"Signed up new user",
        data:data
      }

      // Add a subcollection to the new user with thier current location
      this.db.add(data.path + "/locations", this.userLocation).then((res) => {
        console.log(res);
        this.presentToast();
      })
    });
  }


  /**
   * Method: presentToast
   * Description: Shows a toast for 3 seconds confirming signup, then redirects to login page
   */
  presentToast() {
    let toast = this.toastCtrl.create({
      message: 'You successfully signed up. Redirecting to login page.',
      duration: 3000,
      position: 'top'
    });

    toast.onDidDismiss(() => {
      console.log('Dismissed toast');
      this.navCtrl.push(LoginPage, {}, { animate: true });
    });

    toast.present();
  }
}
