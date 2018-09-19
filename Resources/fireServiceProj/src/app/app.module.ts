import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AngularFireModule } from 'angularfire2';
// import { AngularFireDatabaseModule } from 'angularfire2/database';
// import { AngularFireAuthModule } from 'angularfire2/auth';

import { AngularFirestoreModule } from 'angularfire2/firestore';


import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

import { AppComponent } from './app.component';
import { AppNavbarComponent } from './app-navbar/app-navbar.component';
import { GamesComponent } from './games/games.component';

var firebaseConfig = {
  apiKey: "AIzaSyD2HdwMX3IBLdTad8WeXxgyQJfTQayjzwk",
  authDomain: "video-games-f8e72.firebaseapp.com",
  databaseURL: "https://video-games-f8e72.firebaseio.com",
  projectId: "video-games-f8e72",
  storageBucket: "video-games-f8e72.appspot.com",
  messagingSenderId: "911053562452"
};

@NgModule({
  declarations: [
    AppComponent,
    AppNavbarComponent,
    GamesComponent
  ],
  imports: [
    BrowserModule,
    AngularFireModule.initializeApp(firebaseConfig),  // Add this
    AngularFirestoreModule,  
    NgbModule.forRoot()
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
