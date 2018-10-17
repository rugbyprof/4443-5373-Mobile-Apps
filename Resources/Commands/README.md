### re-Install All Node Packages

- `npm install` Opens the `packages.json` file and installs all dependancies
- Copying a project or changing its location on disk can screw things up. Delete the `node_modules` folder then re-install everything.
  - `rm -rf node_modules`
  - `npm install`

### Deploy on IOS

- Add ios to your ionic project so you can deploy it on a device
  - `ionic cordova platform add ios`
- Create the necessary xCode project files so you can open up xCode with your phone plugged in and deploy
  - `ionic cordova run android --prod --release`
  
### Deploy on Android
- Add android to your ionic project so you can deploy it on a device
  - `ionic cordova platform add android`
- Create the necessary Android Studio project files so you can open up Android Studio with your phone plugged in and deploy
  - `ionic cordova run android --prod --release`
  
