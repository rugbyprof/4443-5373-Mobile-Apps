import { Component } from '@angular/core';
import { Platform } from 'ionic-angular';
import { StatusBar } from '@ionic-native/status-bar';
import { SplashScreen } from '@ionic-native/splash-screen';

// Delete the ones that are not the start page later.
// import { WelcomePage } from '../pages/welcome/welcome';
// import { HomePage } from '../pages/home/home';
import { SignupPage } from '../pages/signup/signup';
import { MapPage } from '../pages/map/map'

@Component({
  templateUrl: 'app.html'
})
export class MyApp {
  rootPage:any = MapPage;

  constructor(platform: Platform, statusBar: StatusBar, splashScreen: SplashScreen) {
    platform.ready().then(() => {
      // Okay, so the platform is ready and our plugins are available.
      // Here you can do any higher level native things you might need.
      statusBar.styleDefault();
      splashScreen.hide();
    });
  }
}
