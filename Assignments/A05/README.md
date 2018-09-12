## IONIC - Getting Up and Running
#### Due: Monday, September 28<sup>th</sup> by classtime.

### Ionic CLI
- `npm install -g cordova ionic`

### Yarn

- Install yarn (optional right now)
- Run:
    - `yarn global add cordova ionic`

### IOS

- Run `xcode-select -p`
- if you see something like `/Applications/Xcode.app/Contents/Developer` then you should be good.
- if not, run `xcode-select --install` then verify you have something similar to the path above showing. 
- if the wrong path shows after your sure you have xcode and xcode command line tools installed, you can try to switch using `sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer`

### Android

- Install JDK 
    - https://docs.oracle.com/javase/8/docs/technotes/guides/install/install_overview.html
- Install Android SDK
    - https://developer.android.com/studio/install
    - Android API level 22 is required to run ionic apps 
    - Android studio provides an SDK manager

- Add To Path
    - Windows
        1. Go to Computer Properties
        2. Advanced system settings
        3. Environment Variables and find PATH
        4. Append the path of tools and platform-tools directories to the end of your PATH variable.
   - OSX 
        - Edit .bash_profile
        - export PATH=${PATH}:/Development/android-sdk/platform-tools:/Development/android-sdk/tools

### Create and Run an Ionic App

- `ionic start <name> <template> [options]` (example create line)
- `ionic serve`   (after changing into an ionic project folder, will run your project)
- `ionic cordova platform --help` (help on adding an emulator)
- `ionic cordova build ios` (add ios as an emulator)
- `ionic cordova build android` (add android as an emulator)


### Crash Course

- https://ionicframework.com/getting-started
