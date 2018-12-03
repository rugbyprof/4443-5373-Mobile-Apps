## Commands to install dependancies

### Add Firbase to project
- ionic cordova plugin add cordova-plugin-firebase
- npm install --save @ionic-native/firebase
- npm install --save angularfire2 firebase firestore

### Add cloud messaging 
- ionic cordova plugin add cordova-plugin-fcm-with-dependecy-updated
- npm install --save @ionic-native/fcm

### Common core stuff
- npm install @angular/common
- npm install @angular/core
- https://angular.io/api/platform-browser
    - npm install @angular/platform-browser
    - npm install @angular/platform-browser-dynamic
- Fix a promise error between rxjs 5 and 6 ?
    - npm i rxjs@6 rxjs-compat@6 promise-polyfill --save
  
### Google maps and spatial queries
- geo fire spatial queries
    - npm install geofire --save
- angular google maps
    - npm install @agm/core --save 

### Mapbox 
    -npm install mapbox-gl --save

### Add IOS 
- ionic cordova platform add ios

- Make sure to choose "legacy build system" in project settings.

### Fix an xcode error
The sandbox is not in sync with the podfile.lock

https://stackoverflow.com/questions/31738339/the-sandbox-is-not-in-sync-with-the-podfile-lock-ios/35446801

PODS_ROOT = ${SRCROOT}/Pods
PODS_PODFILE_DIR_PATH = ${SRCROOT}/.

### Change Icon and Splash
- ionic cordova resources

mapbox:
pk.eyJ1IjoicnVnYnlwcm9mIiwiYSI6ImNpZ3M1aDZwbzAyMnF1c20xcnM4ZGowYWQifQ.s6ghscOu98he230FV1_72w