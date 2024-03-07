#!/bin/bash

# Update and Upgrade your system
echo "Updating and upgrading your system..."
sudo apt-get update && sudo apt-get upgrade -y

# Install Yarn
echo "Installing Yarn..."
npm install --global yarn

# Install Watchman
echo "Installing Watchman..."
sudo apt-get install watchman

# Install JDK (version 11 or newer)
echo "Installing JDK..."
sudo apt-get install openjdk-11-jdk

# Install Android Studio dependencies
echo "Installing Android Studio dependencies..."
sudo apt-get install libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 libbz2-1.0:i386

# Install React Native CLI
echo "Installing React Native CLI..."
yarn global add react-native-cli

echo "Installing Expo Go..."
yarn global add expo-cli

# Setup Android Environment
echo "Please ensure you have Android Studio installed and configure the Android SDK and Android SDK Platform-tools"

echo "React Native dev environment setup script has finished."
