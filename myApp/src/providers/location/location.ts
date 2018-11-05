import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Geolocation } from '@ionic-native/geolocation';

/*
  Generated class for the LocationProvider provider.

  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/
@Injectable()
export class LocationProvider {

  watch: any;
  position: any;

  constructor(private geolocation: Geolocation) {

    // Promise
    this.position = this.geolocation.getCurrentPosition({ maximumAge: 3000, timeout: 5000, enableHighAccuracy: true })

    // .then((resp) => {
    // });

    // Observable
    this.watch = this.geolocation.watchPosition();

    // watch.subscribe((data) => {
    //   this.deleteMarkers();
    //   let updatelocation = new google.maps.LatLng(data.coords.latitude,data.coords.longitude);
    //   let image = 'assets/imgs/blue-bike.png';
    //   this.addMarker(updatelocation,image);
    //   this.setMapOnAll(this.map);
    // });
  }

  getWatchable(){
    return this.watch;
  }

  getPosition(){
    return this.position;
  }

}
