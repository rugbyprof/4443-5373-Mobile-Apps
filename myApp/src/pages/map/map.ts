import { IonicPage, NavController, NavParams } from 'ionic-angular';
import {
  GoogleMaps,
  GoogleMap,
  GoogleMapsEvent,
  GoogleMapOptions,
  CameraPosition,
  MarkerOptions,
  Marker,
  Environment
} from '@ionic-native/google-maps';
import { Component } from "@angular/core/";

@Component({
  selector: 'map_canvas',
  templateUrl: 'map.html'
})
export class MapPage {
  map: GoogleMap;
  constructor(public navCtrl: NavController) { }

  ionViewDidLoad() {
    this.loadMap();
  }

  loadMap() {

    // This code is necessary for browser
    Environment.setEnv({
      'API_KEY_FOR_BROWSER_RELEASE': 'AIzaSyAWdYXZRUjW4vYybrF3EI3EkNtqm1YbDGY',
      'API_KEY_FOR_BROWSER_DEBUG': 'AIzaSyAWdYXZRUjW4vYybrF3EI3EkNtqm1YbDGY'
    });

    let mapOptions: GoogleMapOptions = {
      camera: {
         target: {
           lat: 43.0741904,
           lng: -89.3809802
         },
         zoom: 18,
         tilt: 30
       }
    };

    this.map = GoogleMaps.create('map_canvas', mapOptions);

    let marker: Marker = this.map.addMarkerSync({
      title: 'Ionic',
      icon: 'blue',
      animation: 'DROP',
      position: {
        lat: 43.0741904,
        lng: -89.3809802
      }
    });
    marker.on(GoogleMapsEvent.MARKER_CLICK).subscribe(() => {
      alert('clicked');
    });
  }
}