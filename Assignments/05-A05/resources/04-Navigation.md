## Q

So the react navigation container only needs to be created once, in the `app.js` file for instance? Then I can access all pages registered using the "name" they were registered with?

## A

Yes, that's exactly right! The `NavigationContainer` should be set up once at the root of your app's component hierarchy, typically in your `App.js` (or `App.tsx` if you're using TypeScript) file. It acts as the container for your navigation context and state. Within this `NavigationContainer`, you define your navigators (such as stack navigators, tab navigators, drawer navigators, etc.) and the screens within those navigators.

Each screen is registered with a `name` and associated with a specific component via the `component` prop in the `Stack.Screen` component (if you're using a stack navigator as in your example). Once registered, you can navigate to those screens from anywhere in your app using the `name` you've assigned to them, as long as you have access to the navigation prop, which React Navigation automatically passes to screen components.

### Basic Structure

```jsx
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import LoginPage from './src/screens/LoginPage';
import RegistrationPage from './src/screens/RegistrationPage';
import HomePage from './src/screens/HomePage';
// Import other screens

const Stack = createNativeStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Login" component={LoginPage} />
        <Stack.Screen name="Register" component={RegistrationPage} />
        {/* Register other screens here */}
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;
```

### Navigating Between Screens

Anywhere in your app, as long as you have access to the `navigation` prop (which is automatically provided to your screen components), you can navigate between screens using the `navigate` method with the registered `name` of the screen you want to navigate to. For example, from the `LoginPage`, you can navigate to the `RegistrationPage` like so:

```jsx
navigation.navigate('Register');
```

### Key Points

- **Single `NavigationContainer`**: You only need one `NavigationContainer` at the top level of your app. It encapsulates all your navigation logic and state.
- **Screen Registration**: Screens are registered within navigators using a unique `name` and a component. This registration tells React Navigation about the screens you have in your app and how to navigate to them.
- **Navigation Prop**: React Navigation injects the `navigation` prop into every screen component registered within a navigator, enabling you to perform navigation actions.
- **Accessing Registered Screens**: You can navigate to any registered screen from anywhere in your app using its registered `name` via the `navigation` prop.

This setup provides a flexible and powerful system for managing navigation in React Native apps, allowing you to define complex navigation structures in a simple and declarative manner.

## Using Navigation

When you're using React Navigation's `createNativeStackNavigator()` in your React Native app, and you want to navigate between screens within the same folder or any part of your app, you navigate using the `name` prop you define for each `Stack.Screen`. The `component` prop of each `Stack.Screen` specifies which component should be rendered when navigating to that screen.

Given your setup, you have defined two screens within your `Stack.Navigator`:

- A "Login" screen that renders the `LoginPage` component.
- A "Register" screen that renders the `RegistrationPage` component.

To navigate between these screens, you use the navigation prop that React Navigation provides to your screen components. Here's how you can do it:

### Navigating from `LoginPage` to `RegistrationPage`

In your `LoginPage` component, when you want to navigate to the `RegistrationPage`, you would use something like this:

```jsx
// Inside your LoginPage component
navigation.navigate('Register');
```

### Example Usage in `LoginPage`

```jsx
import React from 'react';
import { View, Button } from 'react-native';

function LoginPage({ navigation }) {
  return (
    <View>
      {/* Other login logic and UI components */}
      <Button
        title="Go to Register"
        onPress={() => navigation.navigate('Register')}
      />
    </View>
  );
}

export default LoginPage;
```

### Navigating Back to `LoginPage` from `RegistrationPage`

Similarly, in your `RegistrationPage` component, if you want to navigate back to the `LoginPage` (or to any other screen), you use the `navigate` function from the navigation prop:

```jsx
// Inside your RegistrationPage component
navigation.navigate('Login');
```

### Example Usage in `RegistrationPage`

```jsx
import React from 'react';
import { View, Button } from 'react-native';

function RegistrationPage({ navigation }) {
  return (
    <View>
      {/* Other registration logic and UI components */}
      <Button
        title="Back to Login"
        onPress={() => navigation.navigate('Login')}
      />
    </View>
  );
}

export default RegistrationPage;
```

### Important Notes

- The `navigation` prop is automatically provided to all screen components by React Navigation, so you can use it directly as shown in the examples.
- The `name` prop you define for each `Stack.Screen` is used as the identifier for navigation actions. Ensure these names are unique within each navigator.
- React Navigation includes functionality to go back to the previous screen without needing to specify the screen name, via `navigation.goBack()` or using the back functionality built into the navigation header.

This approach allows you to create a navigational flow between different screens in your app, regardless of whether they're in the same folder or scattered across different locations in your project structure.