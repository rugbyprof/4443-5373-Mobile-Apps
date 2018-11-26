// The Cloud Functions for Firebase SDK to create Cloud Functions and setup triggers.
const functions = require('firebase-functions');

// The Firebase Admin SDK to access the Firebase Realtime Database.
const admin = require('firebase-admin');

var serviceAccount = require('../serviceAccountKey.json');

// const firestore = new Firestore();
// const settings = {
//     timestampsInSnapshots: true
// };
// firestore.settings(settings);

//admin.initializeApp(functions.config().firebase);

admin.initializeApp({
    credential: admin.credential.cert(serviceAccount)
});

var db = admin.firestore();

// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//
// exports.helloWorld = functions.https.onRequest((request, response) => {
//  response.send("Hello from Firebase!");
// });

// var docRef = db.collection('people').doc('alovelace');

// var setAda = docRef.set({
//     first: 'Ada',
//     last: 'Lovelace',
//     born: 1815
// });

// var aTuringRef = db.collection('people').doc('aturing');

// var setAlan = aTuringRef.set({
//     'first': 'Alan',
//     'middle': 'Mathison',
//     'last': 'Turing',
//     'born': 1912
// });



loadFakeData('people');

function loadFakeData(colID) {
    var data = require("/Users/griffin/Code/Courses/4443-Mobile-Apps/firestore-admin/data.json");
    for (var k in data) {
        if (data.hasOwnProperty(k)) {
            let d = data[k];
            console.log(d);
            let user = {
                "id": d['id'],
                "first": d['first_name'],
                "last": d['last_name'],
                "email": d['email'],
                "gender": d['gender'],
                "ip_address": d['ip_address'],
                "city": d['city'],
                "state": d['state']
            };
            let location = {
                'geopoint': [parseFloat(d['lat']), parseFloat(d['lon'])]
            };
            let userID = user.id;
            let collRef = db.collection(colID);
            console.log(userID);
            collRef.doc(userID).set(user);

            
            // collRef.get().then((result_1) => {
            //     let locID = result_1.size + 1;
            //     collRef.collection("locations").doc(locID).set({
            //             'user_id': userID,
            //             'loc_id': locID,
            //             'geopoint': location.geopoint
            //     });
            // });
        }
    }
}

