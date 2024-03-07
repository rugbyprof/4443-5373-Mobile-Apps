## Q

I've seen a lot of chatter about using Expo Go to develop apps instead of `react-native-cli`. Can you give me some additioonal information about `expo go` in both the windows world and the mac world, if we decide to go that route instead of using `react-native-cli`?

## A

Switching from `react-native-cli` to using Expo (specifically Expo Go for development) can indeed streamline the development process for React Native apps, both on Windows and macOS. Expo provides an abstraction layer on top of React Native, offering a set of tools and services that simplify the development, build, deployment, and iteration processes for your React Native applications.

### What is Expo Go?

Expo Go is a mobile app available for both Android and iOS devices that allows developers to quickly run and test their Expo projects on real devices without needing to compile the app locally. It's especially useful during the development phase, as it supports live reloading and hot reloading, making it easier to see changes in real-time.

### Benefits of Using Expo:

- **Ease of Use**: Expo abstracts away much of the complexity involved in configuring native code, making it easier for beginners to start with React Native development.
- **Cross-Platform**: Apps can be developed and tested on both iOS and Android using the same codebase.
- **Live Reloading**: Instantly view changes on your device or emulator without needing to rebuild your app.
- **Access to Native APIs**: Expo provides a rich set of APIs that cover most needs for mobile app development, from camera access to push notifications, without having to write any native code.
- **No Native Code Compilation Required**: With Expo Go, you don't need to compile your app to test it, which simplifies the setup for new developers and reduces the need for a complex development environment.

### Setting Up Expo for Development:

1. **Install Node.js**: Make sure Node.js is installed on your system.
2. **Install Expo CLI**: Use npm or Yarn to install the Expo CLI.
   - With npm: `npm install -g expo-cli`
   - With Yarn: `yarn global add expo-cli`
3. **Create a New Expo Project**: Run `expo init YourProjectName` to create a new Expo project.
4. **Start Your Project**: Navigate into your project directory and start the project with `expo start`. This will open a developer tools window in your browser.
5. **Install Expo Go on Your Mobile Device**: Download the Expo Go app from the App Store or Google Play Store on your mobile device.
6. **Test Your Project on Your Device**: Scan the QR code provided by Expo in the terminal or in your browser with the Expo Go app to open your project.

### Windows and macOS Considerations:

- **Windows**: Ensure you have an Android emulator set up or a physical device with Expo Go installed for testing. If you're using WSL (Windows Subsystem for Linux), the setup process is similar to that on a native Linux system.
- **macOS**: For iOS development, having a Mac is advantageous as it allows you to run the iOS Simulator directly from your development machine. For Android, you can use an emulator or a physical device.

### Expo vs. React Native CLI:

While Expo offers many conveniences and is great for getting started quickly, it's worth noting that it might limit your ability to use custom native modules that require linking. If your project requires specific native capabilities not supported by Expo, you may eventually need to "eject" to a bare workflow, which gives you full control over the native code but requires managing native dependencies yourself.

In summary, using Expo Go for development, whether on Windows or macOS, simplifies the initial setup and ongoing development process for React Native apps. It's an excellent choice for teaching purposes and for projects that can operate within the Expo ecosystem.