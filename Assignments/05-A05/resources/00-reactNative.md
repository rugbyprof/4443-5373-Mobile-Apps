Let's walk through creating a basic React Native app with a landing page, intending to add a login and registration page later. We'll use `react-native-paper` for UI components. Here's a step-by-step guide:

### Step 1: Create a New React Native App

First, you'll create a new React Native app using the React Native CLI. Open your terminal and run:

```bash
npx react-native init PaperApp
```

This command creates a new React Native project called `PaperApp`. Once the process completes, navigate into your project directory:

```bash
cd PaperApp
```

### Step 2: Install React Native Paper

Now, install `react-native-paper` and its peer dependencies. You'll also need `react-native-vector-icons` for icons in `react-native-paper`.

```bash
yarn add react-native-paper react-native-vector-icons
```

Or, if you prefer npm:

```bash
npm install react-native-paper react-native-vector-icons
```

### Step 3: Link Vector Icons (If Necessary)

For older versions of React Native (<= 0.59), you need to link `react-native-vector-icons`. If you're using a newer version, this step is not necessary as auto-linking is supported.

```bash
npx react-native link react-native-vector-icons
```

### Step 4: Create a Landing Page Component

Create a new file for the landing page. You might organize your project with a `screens` folder:

```bash
mkdir screens
touch screens/LandingPage.js
```

Now, edit `screens/LandingPage.js`:

```javascript
import React from 'react';
import { View, StyleSheet } from 'react-native';
import { Button, Text } from 'react-native-paper';

const LandingPage = ({ navigation }) => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Welcome to PaperApp!</Text>
      <Button icon="login" mode="contained" onPress={() => console.log('Login')}>
        Login
      </Button>
      <Button icon="account-plus" mode="contained" onPress={() => console.log('Register')}>
        Register
      </Button>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  title: {
    fontSize: 20,
    marginBottom: 20,
  },
});

export default LandingPage;
```

### Step 5: Use the Landing Page Component in App.js

Modify `App.js` to use the `LandingPage` component:

```javascript
import React from 'react';
import LandingPage from './screens/LandingPage';
import { Provider as PaperProvider } from 'react-native-paper';

const App = () => {
  return (
    <PaperProvider>
      <LandingPage />
    </PaperProvider>
  );
};

export default App;
```

The `PaperProvider` component wraps your app to provide theming and other context for `react-native-paper` components.

### Step 6: Run Your App

Now, you're ready to run your app. If you're developing for iOS:

```bash
npx react-native run-ios
```

For Android:

```bash
npx react-native run-android
```

Your app should now launch in the respective emulator/simulator or physical device, displaying the landing page with two buttons: "Login" and "Register".

These buttons don't do anything yet, but they're set up to integrate with your future login and registration pages. When you're ready to build those out, you'll add navigation logic, potentially using a library like React Navigation, and flesh out the Login and Register components similarly.



------


Using Expo to create your React Native app is a great choice, especially if you want a smoother setup and development experience. Expo provides a set of tools and services around React Native, simplifying the process of starting a project, developing it, and deploying it across various platforms. Here's how you can create a basic React Native app using Expo with a landing page, planning to add a login and registration page later:

### Step 1: Install the Expo CLI

First, you need to install the Expo CLI if you haven't already. Open your terminal and run:

```bash
npm install -g expo-cli
```

### Step 2: Initialize Your Expo Project

To create a new Expo project, use the following command:

```bash
expo init PaperApp
```

You'll be prompted to choose a template. For a basic JavaScript project, you can select the "blank" template. If you prefer TypeScript, you can choose the "blank (TypeScript)" template.

### Step 3: Navigate to Your Project and Start the Development Server

Once the setup is complete, navigate to your project directory:

```bash
cd PaperApp
```

Then, start the Expo development server:

```bash
expo start
```

### Step 4: Install React Native Paper

With your Expo project set up, you can now add React Native Paper:

```bash
expo install react-native-paper
```

### Step 5: Create a Landing Page

Create a `screens` folder and add a `LandingPage.js` file:

```bash
mkdir screens
touch screens/LandingPage.js
```

Add the following code to `LandingPage.js`:

```javascript
import React from 'react';
import { View, StyleSheet } from 'react-native';
import { Button, Text } from 'react-native-paper';

const LandingPage = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Welcome to PaperApp!</Text>
      <Button mode="contained" onPress={() => console.log('Login')}>
        Login
      </Button>
      <Button mode="contained" onPress={() => console.log('Register')}>
        Register
      </Button>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  title: {
    fontSize: 20,
    marginBottom: 20,
  },
});

export default LandingPage;
```

### Step 6: Use the Landing Page Component in App.js

Modify `App.js` (or `App.tsx` if you're using TypeScript) to use the `LandingPage` component:

```javascript
import React from 'react';
import LandingPage from './screens/LandingPage';
import { Provider as PaperProvider } from 'react-native-paper';

export default function App() {
  return (
    <PaperProvider>
      <LandingPage />
    </PaperProvider>
  );
}
```

### Step 7: Run Your App

With Expo, you can easily run your app on a physical device using the Expo Go app or on a simulator/emulator. Running `expo start` will open a developer tools page in your browser, and you can scan the QR code with the Expo Go app on your device or run the app in an emulator/simulator from the developer tools page.

This setup gives you a basic React Native app using Expo and React Native Paper, with a simple landing page and placeholders for your login and registration pages. As you expand your app, you can add navigation and other screens as needed.