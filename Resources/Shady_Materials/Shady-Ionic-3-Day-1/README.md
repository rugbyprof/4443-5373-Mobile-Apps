# Ionic 3 Tutorial

## Installation 

### Windows

1. Install Node and NPM (find on google)
2. Add Node and NPM to PATH
3. Install Cordova
```shell
npm install -g cordova
```
4. Install Ionic CLI
```shell
npm install -g ionic
```

### Linux & MacOS

1. Install NVM (Node Package Manager)

```shell
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash

```
2. Restart Shell to load nvm
3. Install Node
```shell
nvm install node
nvm use node
```
3. Install Cordova
```shell
sudo npm install -g cordova
```
4. Install Ionic 
```shell
sudo npm install -g ionic
```

## Testing

### Ionic CLI 3.x.x
```shell
ionic start testApp blank
```

### Ionic CLI 4.x.x

```shell
ionic start testApp blank --type=angular
```

To run the app
```shell
ionic serve
```