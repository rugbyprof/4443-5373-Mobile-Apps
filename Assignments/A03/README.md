## Geolocation - Google Maps
### Due: Part 1 by October 10<sup>th</sup>

### Overview

This will be a multi-part project that will be based around user location. 
- Part 1 (Due Oct 10<sup>th</sup>)
  - Show users current location on a map, and save that location to a firestore collection.
- Part 2 (Due Oct 17<sup>th</sup>)
  - Add a user login / registration page.
  - Make user authenticate before starting the logging feature.
- Part 3 (Due TBD)
  - Add a configuration page that will let a user:
    - Pick how often location gets logged
    - (we will add more later) 
- Part 4 (Due TBD)
  - Multi-User broadcast location
- Part 5 (Due TBD)
  - Image upload with geo-tagged info for image.

You can work with a partner. It is possible to work in groups of 3, but I have to OK the group.

## Part 1

### Create a Firestore Collection

- Create a Firebase account (if you don't have one)
- Create a new project called `my-location` (you may have to change it a little to be unique)
- In your project, create two Cloud Firestore collections:
  - `users`
  - `locations`

Your `users` collection should only have 1 user right now:

```json
{
  "id": 100,
  "first": "your first name",
  "last":"your last name",
  "email":"your@email.com"
}
```

Your `locations` collection will store documents similar to :

```json
{
  "id": 100,
  "point":[33.90976, 98.500847],
  "time": "October 3, 2018 at 1:45:00 PM UTC-5"
}
```

### Geolocation Tutorial

- This [Geolocation Tutorial](https://www.joshmorony.com/ionic-2-how-to-use-google-maps-geolocation-video-tutorial/) will show you how to display a map, and add a map marker.
- You will have to get an [api key](https://developers.google.com/maps/documentation/javascript/get-api-key) from google.
- Put your my-locations project in your assignments folder on github.
- Delete your `node_modules` folder first.

## Part 2

### User Authentication

- This [Authentication Tutorial](https://medium.com/appseed-io/integrating-firebase-password-and-google-authentication-into-your-ionic-3-app-2421cee32db9) shows you how to authenticate with Firebase and Ionic. 
- Forms: https://robferguson.org/blog/2017/11/19/ionic-3-and-forms/
- Authentication: https://ionicthemes.com/tutorials/about/firebase-authentication-in-ionic-framework-apps

