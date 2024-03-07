## Q

I have a very simple react native app running using expo go. It is currently running in the iOS simulator I installed via xcode. It has what seems to be a single page created in `App.js` and prints some text to the page. 

I want to create extra pages (components) and organize my react app in a fashion that fits with current design trends. Some of the pages I want to create in this "native" app are: RegistrationPage, LoginPage, HomePage. If poossible I would like to create each page as a component, but I'm not to sure about react.js vs react native.


## A

Hey Terry! It's great to hear you're diving into React Native development with Expo Go. Organizing your app into components and pages is a solid approach for both maintainability and scalability. React Native uses the same design principles as React.js, so if you're familiar with React for the web, you'll find many concepts transfer over seamlessly, including components, state, props, and lifecycle methods.

For your app, creating separate components for `RegistrationPage`, `LoginPage`, and `HomePage` is definitely the way to go. This will not only help in organizing your code better but also make it easier to manage state and navigation between different screens.

### Creating Components

Each page in your React Native app can be created as a functional component. Here’s a basic structure for how you can define these components:

```jsx
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const LoginPage = () => {
  return (
    <View style={styles.container}>
      <Text>Login Page</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default LoginPage;
```

You can create similar components for `RegistrationPage` and `HomePage` by following the same structure.

### Organizing the App Structure

A common practice is to organize your components and screens into separate directories for clarity. For example:

```
/my-app
  /src
    /components
      // Shared components here
    /screens
      LoginPage.js
      RegistrationPage.js
      HomePage.js
  App.js
```

### Navigation

To navigate between these pages, you’ll want to use a navigation library like React Navigation, which is widely used in the React Native ecosystem and supports a variety of navigation patterns, such as stack navigation, tab navigation, and drawer navigation.

First, install React Navigation in your Expo project:

```bash
npm install -g expo-cli
```

```bash
npx expo install react-navigation react-native-screens react-native-safe-area-context
```

Then, install the Stack Navigator library:

```bash
npx expo install react-navigation-stack @react-navigation/native-stack
```

Here's how you can set up a simple stack navigator in your `App.js` to manage navigation between `LoginPage`, `RegistrationPage`, and `HomePage`:

```jsx
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import LoginPage from './src/screens/LoginPage';
import RegistrationPage from './src/screens/RegistrationPage';
import HomePage from './src/screens/HomePage';

const Stack = createNativeStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Login">
        <Stack.Screen name="Login" component={LoginPage} />
        <Stack.Screen name="Register" component={RegistrationPage} />
        <Stack.Screen name="Home" component={HomePage} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;
```

This setup uses a stack navigator for simple navigation between screens, where pushing a new screen onto the stack navigates to that screen, and popping it off returns you to the previous screen.

Remember, React Native and React share many concepts, so if you're comfortable with React.js, you'll likely get the hang of React Native quickly, especially with the help of Expo to smooth out the development experience. Keep exploring and experimenting with different components and navigation patterns, and you'll be building complex, well-structured apps in no time!



## Q

I'm having some issues getting `react-navigation` installed. I used the command: "expo install react-navigation react-native-screens react-native-safe-area-context" but it told me to use "npx expo install ...." which I did. Then I ran "npx expo install react-navigation-stack @react-navigation/native-stack". Then I run: "npm run ios". Are their some additional steps I need to perform? Clearing cache? Use different commands

## A

When setting up `react-navigation` in an Expo project, it's crucial to follow the installation steps carefully to ensure all dependencies are correctly installed and compatible with each other. Expo manages the installation of certain native modules a bit differently to ensure compatibility with its managed workflow, which is why you're prompted to use `npx expo install` for certain packages. Here's a step-by-step guide to help troubleshoot and ensure you've got everything set up correctly for `react-navigation`:

### 1. Install Core Navigation Packages

You've started correctly by installing the core navigation packages and dependencies. Just to recap, for a basic setup, you should install `react-navigation` along with some essential dependencies:

```sh
npx expo install react-native-screens react-native-safe-area-context
```

### 2. Install Navigation Stack

The command you used, `npx expo install react-navigation-stack @react-navigation/native-stack`, seems to mix up two different things:

- `react-navigation-stack` is a stack navigator for `react-navigation` 4.x and below.
- `@react-navigation/native-stack` is the native stack navigator for `react-navigation` 5.x and newer.

For most new projects, you should be using `react-navigation` 5.x or newer, which means you don't need `react-navigation-stack`. Instead, you should install `@react-navigation/native` and `@react-navigation/native-stack`:

```sh
npx expo install @react-navigation/native
npx expo install @react-navigation/native-stack
```

### 3. Ensure Compatibility

Make sure that the versions of `react-navigation` and its dependencies are compatible with each other and with the Expo SDK version you're using. The Expo documentation and the `react-navigation` installation guide are good resources for this.

### 4. Additional Dependencies

Depending on the features you're planning to use, you might need to install additional packages. For example, if you're using tabs or drawers in your navigation, you might need:

```sh
npx expo install @react-navigation/bottom-tabs
npx expo install @react-navigation/drawer
```

### 5. Clearing Cache (If Necessary)

Sometimes, after installing new packages or updating existing ones, you might need to clear your project's cache to ensure that your changes are reflected. You can do this by running:

```sh
expo start -c
```

This starts your project and clears the cache at the same time.

### 6. Update Your App's Entry Point

Ensure that your app's entry point (usually `App.js` or `App.tsx`) is correctly set up to use `react-navigation`. For `react-navigation` 5.x and newer, this involves wrapping your app's component tree in a `NavigationContainer`:

```jsx
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

const Stack = createNativeStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        {/* Your screens go here */}
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;
```

### Final Checks

- Double-check the documentation for `react-navigation` to ensure you haven't missed any steps specific to your use case.
- Review any error messages carefully; they can provide hints about what might be missing or misconfigured.

If you're still encountering issues after following these steps, consider checking the specific error messages you're getting for more clues, and ensure your Expo CLI and project SDK versions are up to date.

## Q

It tells me "The global expo-cli package has been deprecated." and it wants me to run: " npx expo start". Does this seem right?

## A

Yes, that message is correct and aligns with the recent changes made by the Expo team. The Expo CLI is no longer recommended to be installed globally due to the rapid pace of updates and changes. Instead, using `npx` to run Expo commands ensures that you're always using the latest version of the CLI without needing to manage global package updates manually.

When you see the message **"The global expo-cli package has been deprecated"**, it's advising you to avoid using a globally installed version of `expo-cli`. Instead, you should prefix your Expo commands with `npx`, like so:

```sh
npx expo start
```

This approach runs `expo-cli` directly using `npx`, which will temporarily download the most recent version of `expo-cli` if it's not already installed on your machine, or use the existing version if it's available. This ensures that you're always using the latest version for your project, helping to avoid potential issues caused by version discrepancies.

### Recommended Workflow

- **Starting the Project**: Use `npx expo start` to run your Expo project.
- **Installing Packages**: Use `npx expo install [package-name]` for installing packages to ensure compatibility with your Expo SDK version.
- **Upgrading Expo SDK**: Use `npx expo upgrade` to upgrade your project to the latest SDK.

### Benefits of Using `npx` with Expo

- **No Global Installs Required**: Reduces the need for global package installations, keeping your system cleaner.
- **Always Up-to-Date**: Ensures that you're using the most current version of `expo-cli` for project commands.
- **Project-specific CLI Version**: Helps to prevent conflicts between different projects that may require different versions of `expo-cli`.

### Action Steps

If you have `expo-cli` installed globally, it might be a good idea to uninstall it to prevent accidentally using an outdated version. You can uninstall the global `expo-cli` package using:

```sh
npm uninstall -g expo-cli
```

And then, simply use `npx` for all your Expo-related commands as suggested. This change is part of Expo's efforts to streamline the development process and ensure developers have access to the latest features and fixes.