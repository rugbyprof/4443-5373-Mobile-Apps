import { Injectable } from '@angular/core';
import { environment } from '../../../environment';
import {
  AngularFirestore,
  AngularFirestoreDocument,
  AngularFirestoreCollection,
  DocumentChangeAction,
  Action,
  DocumentSnapshotDoesNotExist,
  DocumentSnapshotExists,
} from 'angularfire2/firestore';
import { GeoJson } from './geoJson';
import * as mapboxgl from 'mapbox-gl';

@Injectable()
export class MapProvider {

  constructor(private db: AngularFirestore) {
    mapboxgl.accessToken = environment.mapbox.accessToken
  }


  getMarkers(): AngularFirestoreCollection<any> {
    return this.db.collection('/markers')
  }

  createMarker(data: any) {
    return this.db.collection('/markers')
                  .add(data);
  }

  removeMarker($key: string) {
    return this.db.doc('/markers/' + $key).delete();
  }

}