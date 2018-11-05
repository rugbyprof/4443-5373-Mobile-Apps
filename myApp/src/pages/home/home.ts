import { FirebaseProvider } from './../../providers/firebase/firebase';
import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import {
  AngularFirestore,
  AngularFirestoreDocument,
  AngularFirestoreCollection,
  DocumentChangeAction,
  Action,
  DocumentSnapshotDoesNotExist,
  DocumentSnapshotExists,
} from 'angularfire2/firestore';
import { Observable, from } from 'rxjs';
import { map, tap, take, switchMap, mergeMap, expand, takeWhile } from 'rxjs/operators';

export interface User {
  email: string;
  first: string;
  last: string;
  id: string;
}

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})

export class HomePage {

  usersDocument: AngularFirestoreDocument<User>;
  usersObservable: Observable<any[]>;
  collObservable: Observable<any[]>;

  constructor(public navCtrl: NavController, public db: FirebaseProvider) {

  }

  ngOnInit() {
    // Step 1: Make a reference

    // Load observable in order to use in html
    this.collObservable = this.db.colWithIds$('users');
    
    // Call subscribe on observable in order to view it immediately
    this.db.colWithIds$('users').subscribe((data) => {
      console.log(data); // This will work
    });

  }



  logout() {
    // Remove API token 
    // const root = this.app.getRootNav();
    // root.popToRoot();
  }
}