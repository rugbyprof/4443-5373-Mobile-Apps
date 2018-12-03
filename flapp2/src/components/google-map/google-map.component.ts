import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'google-map',
  templateUrl: 'google-map.component.html'
})
export class GoogleMapComponent implements OnInit {

    lat: number;
    lng: number;


    constructor() { }

    ngOnInit() {
      this.getUserLocation()

    }

    private getUserLocation() {
     /// locate the user
     if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position => {
         this.lat = position.coords.latitude;
         this.lng = position.coords.longitude;
         console.log(this.lat);
         console.log(this.lng);
       });
     }
   }
 }