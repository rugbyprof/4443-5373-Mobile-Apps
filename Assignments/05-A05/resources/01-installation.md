## Q

So I've been messing arouond with react.js and creating scripts to help with installation and scaffolding of projects. I was using node with npm, however I think I want to switch to yarn as my package manager. Could you start my journey of getting help with react native by generating a list of items I need to install or download in order to start a solid dev environment for react native? Also, one goal is to automate the process for my students, so if there are several things to be done, maybe you could combine them into a script like format?

## A

Switching to Yarn as your package manager for React Native projects is a solid choice, especially if you value speed and consistency in your development workflow. Yarn caches every package it downloads, so it never needs to download it again. It also parallelizes operations to maximize resource utilization so install times are faster than ever.

To get a solid dev environment set up for React Native, especially if you're aiming for automation for your students, we'll cover the essentials. After the list, I'll sketch out a basic script that you can run with Yarn to kick things off. This will be particularly handy for getting your students up and running with minimal friction.

### Essentials to Install for React Native Development:

1. **Node.js and npm**: Yarn is an alternative to npm, but you still need Node.js installed to get Yarn. npm comes bundled with Node.js.
2. **Yarn**: As you've decided, Yarn will be your package manager.
3. **Watchman**: A file-watching service developed by Facebook for macOS and Linux. It helps in watching changes in the filesystem which is especially useful in development environments.
4. **Java Development Kit (JDK)**: React Native requires JDK for Android development. Oracle JDK or OpenJDK are both fine, but ensure it's version 11 or newer.
5. **Android Studio**: For Android development, this is essential for its SDK and emulator.
6. **Xcode**: For iOS development (only on macOS), necessary for its iOS Simulator and the entire iOS development ecosystem.
7. **React Native CLI**: The command-line tool that enables you to initialize, develop, and manage your React Native projects.
8. **Visual Studio Code or any preferred IDE**: VS Code is a popular choice among React Native developers, but any IDE or text editor will do.

### Automation Script:

Below is a basic bash script for macOS/Linux that you can customize and expand based on your specific needs. This script assumes that Node.js is already installed (as it's a prerequisite for Yarn). For Windows environments, the commands would need to be adapted for PowerShell or Command Prompt, or you could use WSL (Windows Subsystem for Linux) to run the script directly in a Linux environment.

## WSL INSTALL (windows)
```bash
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

# Setup Android Environment
echo "Please ensure you have Android Studio installed and configure the Android SDK and Android SDK Platform-tools"

echo "React Native dev environment setup script has finished."
```

Remember to make this script executable by running `chmod +x scriptname.sh` in the terminal. 

For Windows users, setting up the environment variables (especially for Android SDK) and managing JDK installations might require manual steps unless you're integrating with **WSL**.

This script doesn't cover Xcode (macOS only) and Visual Studio Code installation because Xcode is typically installed via the macOS App Store, and VS Code installation preferences can vary widely among developers. 

Automation for a development environment setup is a great way to lower the entry barrier for your students. You might need to tweak the script based on the operating system your students are using and the specific needs of your course. Hopefully, this gets you started on the right foot!

## Q

I agree that my windows users should use WSL when possible. However, I do have quite a few mac users.  What changes (besides from apt to brew) would we need to implement? I don't need a full response, but if you could only update the `Automation Script` that would be awesome!

Absolutely, Terry! For your macOS users, switching from `apt-get` to `brew` is the primary change, along with some macOS-specific adjustments. Here's an updated version of the script tailored for macOS, incorporating Homebrew and the installation steps for Watchman and other dependencies:


## MAC INSTALL
```bash
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

echo "React Native dev environment setup script for macOS has finished."
```

This script should cover the basics for getting a macOS environment up and ready for React Native development. Note that it includes an optional step for installing Android Studio via Homebrew. Students working on iOS apps would need to have Xcode installed, which they can download from the App Store. The command line tools for Xcode are essential for building iOS applications and are included in the script.

Adjustments may be necessary based on the specific setup or configuration you prefer, but this should give your macOS users a solid starting point!
