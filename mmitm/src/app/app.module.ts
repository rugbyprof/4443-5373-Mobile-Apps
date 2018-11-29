import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouteReuseStrategy } from '@angular/router';

import { IonicModule, IonicRouteStrategy } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { Firebase } from '@ionic-native/firebase';

import { AngularFireModule } from 'angularfire2';
import { AngularFirestoreModule } from 'angularfire2/firestore';

const firebase = {
  apiKey: "AIzaSyCdh5VaHpfZclbdkqWw88CvL5sZwUrRUJ8",
  authDomain: "msu-location-logger.firebaseapp.com",
  databaseURL: "https://msu-location-logger.firebaseio.com",
  projectId: "msu-location-logger",
  storageBucket: "msu-location-logger.appspot.com",
  messagingSenderId: "823122992538"
 }
 

@NgModule({
  declarations: [AppComponent],
  entryComponents: [],
  imports: [
    BrowserModule, 
    IonicModule.forRoot(), 
    AngularFireModule.initializeApp(firebase), 
    AngularFirestoreModule,
    AppRoutingModule],
  providers: [
    StatusBar,
    Firebase,
    FcmProvider,
    SplashScreen,
    { provide: RouteReuseStrategy, useClass: IonicRouteStrategy }
  ],
  bootstrap: [AppComponent]
})
export class AppModule {}
