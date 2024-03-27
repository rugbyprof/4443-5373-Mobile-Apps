## Location App Code


|   #   | Name                                 | Description                                        |
| :---: | :----------------------------------- | :------------------------------------------------- |
|   1   | [api.py](api.py)                     | Griffins latest version of his api that uses mysql |
|   2   | [candyStore.sql](candyStore.sql)     | Sql file with mysql db schema                      |
|   3   | [location-app.zip](location-app.zip) | The location app with a working register screen    |
|   4   | [mysqlDb.py](mysqlDb.py)             | Latest mysqldb class to interface with mysql db    |



## Location App

- The zip archive in this folder is my react project with the `node_modules` folder removed.
- To rebuild this project just follow the steps below.


### Rebuild React / Expo Go Project

1. **Unzip the Project**: First, they'll need to unzip the archive you've shared to extract the project folder.

2. **Navigate to the Project Directory**: Using a terminal or command prompt, they should change directory (`cd`) into the project folder they've just unzipped.

3. **Install Dependencies**: Instead of `npm install` (which is also perfectly valid), they can use the Expo CLI command which is slightly more tailored for Expo projects. If they haven't already, they should install Expo CLI globally using:
   ```bash
   npm install -g expo-cli
   ```
   Then, within the project directory, they should run:
   ```bash
   expo install
   ```
   This command is similar to `npm install` but is aware of the Expo ecosystem and will install the correct versions of libraries that are compatible with the version of the Expo SDK you're using.

4. **Start the Project**: Once all dependencies are installed, they can start the project by running:
   ```bash
   expo start
   ```
   This will launch Expo Developer Tools in a web browser, and they'll see a QR code they can scan with the Expo Go app on their iOS or Android device to run the app directly on their phone. Alternatively, they can use Android or iOS simulators/emulators to run the app.

5. **View the App**: By scanning the QR code with the Expo Go app (available in the App Store/Google Play) on their device, they can view and interact with the project you've shared.

