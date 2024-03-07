#!/bin/bash

# Check for Homebrew, install if we don't have it
if test ! $(which brew); then
  echo "Installing homebrew..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Update Homebrew
echo "Updating Homebrew..."
brew update

# Install Yarn
echo "Installing Yarn..."
brew install yarn

# Install Watchman
echo "Installing Watchman..."
brew install watchman

# Install JDK (version 11 or newer)
echo "Installing JDK..."
brew install --cask adoptopenjdk/openjdk/adoptopenjdk11

# React Native CLI
echo "Installing React Native CLI..."
yarn global add react-native-cli

# Setup Android Development Environment
echo "Please ensure you have Android Studio installed and configure the Android SDK and Android SDK Platform-tools via Android Studio"

echo "Optionally, you can install Android Studio via brew as well, using:"
echo "brew install --cask android-studio"

# Setup iOS Development Environment
echo "Installing Xcode Command Line Tools..."
xcode-select --install

echo "Installing Expo Go..."
yarn global add expo-cli

echo "Installing Cocoa Pods in mac..."
sudo gem install -n /usr/local/bin cocoapods -v 1.8.4

echo "React Native dev environment setup script for macOS has finished."