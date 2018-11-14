import { Injectable } from '@angular/core';
import { Platform } from 'ionic-angular';
import {
  GoogleMaps, GoogleMap, GoogleMapsEvent,
  GoogleMapOptions, LocationService,
  Marker, ILatLng, GoogleMapsAnimation
} from '@ionic-native/google-maps';

/*
  Generated class for the MapProvider provider.
  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/
@Injectable()
export class MapProvider {
  public map: GoogleMap;
  private marker: Marker;

  constructor(private platform: Platform) {}

  attachMap(divId: string, coords: ILatLng = {lat: 0, lng: 0}) {
    return new Promise((resolve, reject) => {

      if (this.map) {
        this.map.setDiv(divId);

        this.map.animateCamera({
          target: coords,
          zoom: 15
        })
        .then(() => {
          this.marker.setPosition(coords);
          this.marker.setAnimation(GoogleMapsAnimation.DROP)
          resolve();
        });
        return;
      }

      let options: GoogleMapOptions = {
        controls: {
          compass: true,
          myLocation: true,
          myLocationButton: true,
          mapToolbar: true
        }
      };
      this.map = GoogleMaps.create(divId, options);
      this.map.one(GoogleMapsEvent.MAP_READY).then(() => {
        this.map.animateCamera({
          target: coords,
          zoom: 15
        })
        .then(() => {
          return this.map.addMarker({
              position: coords,
              animation: GoogleMapsAnimation.DROP
            });
        })
        .then((marker: Marker) => {
          this.marker = marker;
          resolve();
        });
      });
    });
  }

  detachMap() {
    this.map.setDiv();
  }

  getMyLocation() {
    return LocationService.getMyLocation();
  }


}