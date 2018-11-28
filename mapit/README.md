ionic cordova plugin add cordova-plugin-geolocation
npm install --save @ionic-native/geolocation



npm install @ionic-native/google-maps @ionic-native/core
npm install --save @ionic-native/core@latest @ionic-native/google-maps@latest
npm install @types/googlemaps --save-dev

ionic cordova plugin add cordova-plugin-googlemaps \
 --variable API_KEY_FOR_ANDROID="AIzaSyCpjhYG_DHokGNgahlr9YcvT6mYFdOIhS4" \
 --variable API_KEY_FOR_IOS="AIzaSyCpjhYG_DHokGNgahlr9YcvT6mYFdOIhS4"

https://docs.google.com/presentation/d/e/2PACX-1vScoho1ensbR4qCI9AIuQN55BZVvK73pAjI7sumDvW3CrxxHnrmpXWUjx2-8CpFibqU1EjLKCRhuthJ/pub?start=false&loop=false&delayms=3000&slide=id.g282d0a7bfd_0_107