## Firebase Ionic Project

### General commands:

```sh
# Create project
ionic start firebase-proj blank
cd firebase-proj

# remove home folder
cd pages
rm -rf home
 
# Generate new homePage
cd ..
ionic generate page HomePage
ionic serve

# Generate data service
ionic generate provider Data

# Get ready to talk to firebase
npm install firebase angularfire2
npm i rxjs@6 rxjs-compat@6 promise-polyfill --save
```

### Create `firebase.ts`

```js
export const FIREBASE_CONFIG = {
    apiKey: "AIzaSyAfIBizSb0L3F_Yu2fycJZJZESxVkTnoeA",
    authDomain: "msu-candy-store.firebaseapp.com",
    databaseURL: "https://msu-candy-store.firebaseio.com",
    projectId: "msu-candy-store",
    storageBucket: "msu-candy-store.appspot.com",
    messagingSenderId: "100839463519"
} 
```

## Connect to Data Source

### Update `app.module.ts`

Add Imports

```js
import { AngularFireModule } from 'angularfire2';
import { AngularFireAuthModule } from 'angularfire2/auth'
import { FIREBASE_CONFIG } from './firebase'
import { AngularFirestoreModule } from 'angularfire2/firestore'
```

Update the imports array in your NGModel:

```js
  imports: [
    BrowserModule,
    IonicModule.forRoot(MyApp),
    AngularFireModule.initializeApp(FIREBASE_CONFIG),
    AngularFireAuthModule,
    AngularFirestoreModule
  ],
```



Lets fix our data service file, to get us some firestore data:

In ***data.ts***:

Add imports
  
```js
import { Injectable } from '@angular/core';
import { AngularFirestore } from 'angularfire2/firestore';
import {  map } from 'rxjs/operators';
```

Remove http client and add firestore

```js
constructor(public http: HttpClient) {
    console.log('Hello DataProvider Provider');
}
```


```js
constructor(private firestore: AngularFirestore) {
    console.log('Hello DataProvider Provider');
}
```

### Add functions

Add one of the following to your `class DataProvider` in `data.ts`:

- Just get everything:

```js
    async getAllCandyWithoutIDs() {
        console.log("Getting all the candy without id...")
        let candyCollection = this.firestore.collection<any>('candy');
        let candy = candyCollection.valueChanges().subscribe((candy) => console.log(candy));
    }
```

- Get everything WITH Id's:

```js
    async getAllCandyWithIDs() {
        console.log("Getting all the candy with id's...")
        let candyCollection = this.firestore.collection<any>('candy');

        let candy = candyCollection.snapshotChanges().pipe(map(actions => {
            return actions.map(action => {
                const id = action.payload.doc.id;
                const data = action.payload.doc.data();
                return { id, ...data };
            });
        }));
        candy.subscribe((candy) => console.log(candy));
    }
```

- Filter Candy on type:

```js
    async getCandyByType(candy_type: string) {
        console.log("Getting all the candy...")
        let candyCollection = this.firestore.collection<any>('candy', ref =>
            ref.where('type', '==', candy_type));

        let candy = candyCollection.snapshotChanges().pipe(map(actions => {
            return actions.map(action => {
                const id = action.payload.doc.id;
                const data = action.payload.doc.data();
                return { id, ...data };
            });
        }));
        candy.subscribe((candy) => console.log(candy));
    }
```

## Viewing the data

- We need to attach that service to one of our existing pages.

In ***home.ts***:

Add a new import:

```js
import { DataProvider } from '../../providers/data/data';
```

Inject your `DataProvider` class into the home pages constructor, and call it `data`.
```js
  constructor(public navCtrl: NavController, public navParams: NavParams, private data: DataProvider) {
  }
```

- Then call one of the methods in the class:

```js
  async getCandy() {
    console.log("getCandy()....")
    this.data.getAllCandyWithIDs();
  }
```

In ***home.html***:

Add this to your `<ion-content>` block:

```js
  <button style="margin-top: 50px;" block round ion-button (click)="getCandy()">Get Candy</button>
```