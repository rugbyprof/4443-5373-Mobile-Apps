//https://angularfirebase.com/lessons/firestore-advanced-usage-angularfire/#2-Get-Observables-with-a-String
//https://www.joshmorony.com/dealing-with-asynchronous-code-in-ionic/

import { Injectable } from '@angular/core';
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

import * as firebase from 'firebase/app';

// export interface User {
//     email: string;
//     first: string;
//     last: string;
//     id: string;
// }

type CollectionPredicate<T> = string | AngularFirestoreCollection<T>;
type DocPredicate<T> = string | AngularFirestoreDocument<T>;


@Injectable()
export class FirebaseProvider {
    ///////////////////////////////////////////////////////////////////////////////////////////

    // usersCollection: AngularFirestoreCollection<User>;
    // usersObservable: Observable<User[]>;


    /**
     * 
     * Generic Data Types 
     * 
     */
    col<T>(ref: CollectionPredicate<T>, queryFn?): AngularFirestoreCollection<T> {
        return typeof ref === 'string' ? this.afs.collection<T>(ref, queryFn) : ref;
    }

    doc<T>(ref: DocPredicate<T>): AngularFirestoreDocument<T> {
        return typeof ref === 'string' ? this.afs.doc<T>(ref) : ref;
    }


    /**
     * 
     * @param afs : AngularFirestore reference
     */
    constructor(private afs: AngularFirestore) {
        console.log('Hello FirebaseProvider Provider');
        //this.loadFakeData();
        //this.addFriends();

        //this.inspectCol('users');

        // this.getUserDoc("0CDpAEQdbQwAHixAkmzP").then((res)=>{
        //     let result = {
        //         message:"getUserDoc",
        //         res:res
        //     }
        //     console.log(result);
        // });

        this.doc$('users/04G6WjXi56LKMhExzubL').subscribe( (res) => {
            let result = {
                "message":"called userdoc",
                res:res
            }
            console.log(result);
        });

    }


    // async getUserDoc(id : any){
    //     return await this.doc$('users/'+id);
    // }

    /**
     * first_name: Ronald
        last_name: Duplan
        email: rduplanrh@sina.com.cn
        gender: Male
        ip_address: 45.188.235.196
        lat: 31.6948
        lon: -106.3
        city: El Paso
        image: data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAKGSURBVDjLpVNLaBNBGP5mdpNsHptH25i+0toIRRAFD3rxqCjowaPtzYNYvIleehE8iHgTBO1BBCl4aG+CxZIeWqrFBxVEUXpIwZqmsWuyaZNusu9xdlPxcSp04GP/Heb75pv/QRhj2M+i2OcSbz1+Ny9F5OOVhhXd0W3qckMuGBweuNydw+G67f9dMBDHsprbleJKoSCmU4ns2MXhuGExIoWEf9TJ/zFpf1uGLbQMp3f0nqFTpW7nTNslz+bLKFZMaAbDWtVFUXWxvuWivO1CaTBUNAbLAdarJh68KKOmGVROZw9RzXBIKEDR1xNH/oOCrR0LmThBgJsJCgRB0QOQDBNU6yamX28i2RFHZzLke6JN3fYt5rpj6M/EMbusoNaw0BWjPjHIhRISgdrwyAq6OuPI9cVAdotHNd1pZ5MfzPXGkE5FMLVQ9AkeUeao8nhyrohEIuKfCYt/lVFrtR0Qnh3bsiGJLgb6kph5r2C9ovt4/lZBlu/JQQeU2b6z35kVm4YDz41p2thUG8hmZASDAZRVCa9W6n6jDGdTSHx8Cm3uIcxSAXpnL8oXrgLsjCdgM15bolQ5OS0jLAXgKQ4diGCAwyublp8APk/h5KUrCA0dQetTHl+XpnGU1ZioqaVvhmkPHu4Pk1iYEkId/1bvSYS0O2H55X2cGL0GaXUBWLyDSCKJg9lBHFuYdERz5+fa6euzqZAcjYohgYg8m5SXT+AqlBJQ/t6bG2ui1D0EnL/xp4Vv9yCp10Syl2HKnxWLp0Yu90e/z8Bo/UCT7zXqAlZWUdrTMEU6Mk++vFm0y3oYdSGAmkpQKBGHX/2I7HWcl0YGxjV1Y0xwyKAjsBJnTZzL23d/AbqhIfYa8w35AAAAAElFTkSuQmCC
        state: Texas
 
     */

    loadFakeData() {
        var data = require("/Users/griffin/Code/Courses/4443-Mobile-Apps/myApp/fb_data.json");
        for (var k in data) {
            if (data.hasOwnProperty(k)) {
                let d = data[k];
                console.log(d);
                let user = {
                    "first": d['first_name'],
                    "last": d['last_name'],
                    "email": d['email'],
                    "gender": d['gender'],
                    "ip_address": d['ip_address'],
                    "city": d['city'],
                    "state": d['state']
                };
                let location = {
                    'geopoint': this.geopoint(parseFloat(d['lat']), parseFloat(d['lon']))
                };


                this.add('users', user).then((res1) => {
                    this.add(res1.path + "/locations", location).then((res2) => {
                        let doc = {
                            'user_id': res1.id,
                            'loc_id': res2.id,
                            'geopoint': location.geopoint
                        };
                        this.add('locations', doc).then((res3) => {
                            console.log(res3);
                        });
                    })
                });
            }
        }
    }


    addFriends() {
        this.colWithIds$('users').subscribe((outer) => {
            for (var ok in outer) {
                if (outer.hasOwnProperty(ok)) {
                    let outer_data = outer[ok];
                    this.colWithIds$('users').subscribe((inner) => {
                        for (var ik in inner) {
                            if (inner.hasOwnProperty(ik)) {
                                let inner_data = outer[ik];
                                if(outer_data.city == inner_data.city){
                                    let doc = {
                                        id:inner_data.id
                                    }
                                    this.add(outer_data.path+ "/friends/"+outer_data.id , doc).then((res) => {
                                        let result = {
                                            res:res,
                                            message:"added friend",
                                            outer_city:outer_data.city,
                                            innier_city:inner_data.city
                                        }
                                        console.log(result);
                                    });
                                }
                            }
                        }
                    });
                }
            }
        });
    }

    ////////////////////////////////////////////////////////////////////////////////////////////
    //Firebase Class Methods
    ////////////////////////////////////////////////////////////////////////////////////////////

    doc$<T>(ref: DocPredicate<T>): Observable<T> {
        return this.doc(ref)
            .snapshotChanges()
            .pipe(
                map((doc: Action<DocumentSnapshotDoesNotExist | DocumentSnapshotExists<T>>) => {
                    return doc.payload.data() as T;
                }),
            );
    }

    col$<T>(ref: CollectionPredicate<T>, queryFn?): Observable<T[]> {
        return this.col(ref, queryFn)
            .snapshotChanges()
            .pipe(
                map((docs: DocumentChangeAction<T>[]) => {
                    return docs.map((a: DocumentChangeAction<T>) => a.payload.doc.data()) as T[];
                }),
            );
    }

    colWithIds$<T>(ref: CollectionPredicate<T>, queryFn?): Observable<any[]> {
        return this.col(ref, queryFn)
            .snapshotChanges()
            .pipe(
                map((actions: DocumentChangeAction<T>[]) => {
                    return actions.map((a: DocumentChangeAction<T>) => {
                        const data: Object = a.payload.doc.data() as T;
                        const id = a.payload.doc.id;
                        return { id, ...data };
                    });
                }),
            );
    }

    /// **************
    /// Write Data
    /// **************

    /// Firebase Server Timestamp
    get timestamp() {
        return firebase.firestore.FieldValue.serverTimestamp();
    }

    set<T>(ref: DocPredicate<T>, data: any): Promise<void> {
        const timestamp = this.timestamp;
        return this.doc(ref).set({
            ...data,
            updatedAt: timestamp,
            createdAt: timestamp,
        });
    }

    update<T>(ref: DocPredicate<T>, data: any): Promise<void> {
        return this.doc(ref).update({
            ...data,
            updatedAt: this.timestamp,
        });
    }

    delete<T>(ref: DocPredicate<T>): Promise<void> {
        return this.doc(ref).delete();
    }

    add<T>(ref: CollectionPredicate<T>, data): Promise<firebase.firestore.DocumentReference> {
        const timestamp = this.timestamp;
        return this.col(ref).add({
            ...data,
            updatedAt: timestamp,
            createdAt: timestamp,
        });
    }

    geopoint(lat: number, lng: number): firebase.firestore.GeoPoint {
        return new firebase.firestore.GeoPoint(lat, lng);
    }

    /// If doc exists update, otherwise set
    upsert<T>(ref: DocPredicate<T>, data: any): Promise<void> {
        const doc = this.doc(ref)
            .snapshotChanges()
            .pipe(take(1))
            .toPromise();

        return doc.then((snap: Action<DocumentSnapshotDoesNotExist | DocumentSnapshotExists<T>>) => {
            return snap.payload.exists ? this.update(ref, data) : this.set(ref, data);
        });
    }

    /// **************
    /// Inspect Data
    /// **************

    inspectDoc(ref: DocPredicate<any>): void {
        const tick = new Date().getTime();
        this.doc(ref)
            .snapshotChanges()
            .pipe(
                take(1),
                tap((d: Action<DocumentSnapshotDoesNotExist | DocumentSnapshotExists<any>>) => {
                    const tock = new Date().getTime() - tick;
                    console.log(`Loaded Document in ${tock}ms`, d);
                }),
            )
            .subscribe();
    }

    inspectCol(ref: CollectionPredicate<any>): void {
        const tick = new Date().getTime();
        this.col(ref)
            .snapshotChanges()
            .pipe(
                take(1),
                tap((c: DocumentChangeAction<any>[]) => {
                    const tock = new Date().getTime() - tick;
                    console.log(`Loaded Collection in ${tock}ms`, c);
                }),
            )
            .subscribe();
    }

    /// **************
    /// Create and read doc references
    /// **************

    /// create a reference between two documents
    connect(host: DocPredicate<any>, key: string, doc: DocPredicate<any>) {
        return this.doc(host).update({ [key]: this.doc(doc).ref });
    }

    // returns a documents references mapped to AngularFirestoreDocument
    docWithRefs$<T>(ref: DocPredicate<T>) {
        return this.doc$(ref).pipe(
            map((doc: T) => {
                for (const k of Object.keys(doc)) {
                    if (doc[k] instanceof firebase.firestore.DocumentReference) {
                        doc[k] = this.doc(doc[k].path);
                    }
                }
                return doc;
            }),
        );
    }

    /// **************
    /// Atomic batch example
    /// **************

    /// Just an example, you will need to customize this method.
    atomic() {
        const batch = firebase.firestore().batch();
        /// add your operations here

        const itemDoc = firebase.firestore().doc('items/myCoolItem');
        const userDoc = firebase.firestore().doc('users/userId');

        const currentTime = this.timestamp;

        batch.update(itemDoc, { timestamp: currentTime });
        batch.update(userDoc, { timestamp: currentTime });

        /// commit operations
        return batch.commit();
    }

    /**
     * Delete a collection, in batches of batchSize. Note that this does
     * not recursively delete subcollections of documents in the collection
     * from: https://github.com/AngularFirebase/80-delete-firestore-collections/blob/master/src/app/firestore.service.ts
     */
    deleteCollection(path: string, batchSize: number): Observable<any> {
        const source = this.deleteBatch(path, batchSize);

        // expand will call deleteBatch recursively until the collection is deleted
        return source.pipe(
            expand(val => this.deleteBatch(path, batchSize)),
            takeWhile(val => val > 0),
        );
    }

    // Detetes documents as batched transaction
    private deleteBatch(path: string, batchSize: number): Observable<any> {
        const colRef = this.afs.collection(path, ref => ref.orderBy('__name__').limit(batchSize));

        return colRef.snapshotChanges().pipe(
            take(1),
            mergeMap((snapshot: DocumentChangeAction<{}>[]) => {
                // Delete documents in a batch
                const batch = this.afs.firestore.batch();
                snapshot.forEach(doc => {
                    batch.delete(doc.payload.doc.ref);
                });

                return from(batch.commit()).pipe(map(() => snapshot.length));
            }),
        );
    }

}
