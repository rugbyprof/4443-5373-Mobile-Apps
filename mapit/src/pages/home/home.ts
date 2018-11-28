import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { FirebaseProvider } from '../../providers/firebase/firebase';
import { LocationProvider } from '../../providers/location/location';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {

  userData = {
    "username": "",
    "password": "",
    "first": "",
    "last": "",
    "email": ""
  };
  userLocation: any;

  constructor(public navCtrl: NavController, public db: FirebaseProvider, public location: LocationProvider) {
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

}
