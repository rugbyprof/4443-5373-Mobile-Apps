For your React Native course starting with a splash page, here's a step-by-step guide:

1. **Expo Go Installation & Setup**:
   - **Introduction**: Explain the benefits of using Expo for React Native development, including easier setup and testing on devices.
   - **Installation**: Guide them to install Expo CLI on their computer using npm or Yarn (`npm install -g expo-cli`).
   - **Project Creation**: Show how to create a new Expo project (`expo init MyNewProject`), choosing a template that suits your needs.
   - **Running the Project**: Teach them to start the development server (`expo start`) and use the Expo Go app on their devices to scan the QR code for real-time testing.

2. **Creating a Splash Page**:
   - **Basic Concepts**: Briefly introduce React components and JSX syntax.
   - **Splash Page Component**: Create a simple Splash component displaying a logo. Use `Image` and `View` components from React Native.
   - **Styling**: Explain basic styling in React Native using the `StyleSheet` object, focusing on aligning the logo center and setting appropriate background colors.
   - **Timing**: Discuss handling timing in JavaScript (`setTimeout`) to navigate from the Splash page to the next screen after a few seconds.

3. **Navigation**:
   - **Introduction to Navigation**: Introduce React Navigation library and its importance for navigating between different screens in a React Native app.
   - **Setup**: Show how to install React Navigation (`npm install @react-navigation/native`) and necessary dependencies for stack navigation (`npm install @react-navigation/stack react-native-screens react-native-safe-area-context`).
   - **Implementation**: Demonstrate creating a stack navigator and linking the Splash page to the next screen in the app.