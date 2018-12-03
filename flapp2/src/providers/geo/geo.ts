import { Injectable } from '@angular/core';
import { AngularFireDatabase } from 'angularfire2/database';

import * as GeoFire from "geofire";
import { BehaviorSubject } from 'rxjs/BehaviorSubject'

@Injectable()
export class GeoProvider {

  dbRef: any;
  geoFire: any;

  hits = new BehaviorSubject([])

  constructor(private db: AngularFireDatabase) {
    /// Reference database location for GeoFire
    this.dbRef = this.db.list('/locations');
    this.geoFire = new GeoFire(this.dbRef.$ref);
    this.seedDatabase();
   }

   /// Adds GeoFire data to database
   setLocation(key:string, coords: Array<number>) {
     this.geoFire.set(key, coords)
         .then(_ => console.log('location updated'))
         .catch(err => console.log(err))
   }


   /// Queries database for nearby locations
   /// Maps results to the hits BehaviorSubject
   getLocations(radius: number, coords: Array<number>) {
    this.geoFire.query({
      center: coords,
      radius: radius
    })
    .on('key_entered', (key, location, distance) => {
      let hit = {
        location: location,
        distance: distance
      }

      let currentHits = this.hits.value
      currentHits.push(hit)
      this.hits.next(currentHits)
    })
   }

   private seedDatabase() {
    let dummyPoints = [
      [37.9, -122.1],
      [38.7, -122.2],
      [38.1, -122.3],
      [38.3, -122.0],
      [38.7, -122.1]
    ]
  
    dummyPoints.forEach((val, idx) => {
      let name = `dummy-location-${idx}`
      console.log(idx)
      this.geoFire.setLocation(name, val)
    })
  }

}