## Dev Environment - Setting up a local dev environment
### Due: September 5<sup>th</sup> by classtime

## Required Packages

- Some version of a Linux Shell:
    - [Windows Version](https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/)
    - [Git Bash](https://git-scm.com/downloads)
- An Editor like Visual Studio Code:
    - https://code.visualstudio.com/
- Install NodeJS
    - https://nodejs.org/en/download/

## Getting Started

### Linux Shell
- Install a linux shell (see links above).

- Then using your shell, install [Node.js](https://nodejs.org/en/download/) for your platform. The Node Package Manager is included in the Node.js distribution. 

- Open a new terminal (command prompt) and check that `node` and `npm` (node package manager) actually exist. To test that you've got Node.js correctly installed on your computer, type `node --help` and you should see the usage documentation. Or type `which node` or `which npm` to see where they are installed. If you get `node not found` or `npm not found` then check your installation.

### IDE

- Install [Visual Studio Code](https://code.visualstudio.com/) and then install the following VS Code extensions (The links are just to make sure you get the correct extension, not needed to actually install):
    - Live Server https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer
    - Beautify https://marketplace.visualstudio.com/items?itemName=HookyQR.beautify
    - Code Runner https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner

**Installing extensions:**

<img src="https://cl.ly/c3c9733e5d5b/Screen%252520Recording%2525202018-08-29%252520at%25252008.33%252520PM.gif" width="600">

1. Click on the extensions button on the left.
2. Type in your search term in the text box.
3. Click `install`
4. Click `reload` (you can install multiple before re-loading).
    

## Basic Commands

- Open your terminal if its not open.
- Type `pwd` (print working directory). It tells you where you are (folder wise).
- Type `ls` to see your files. This is a short listing (not very helpful in my opinion).
- Type `ls -lah`. The `l` means long, the `a` means all, and the `h` means human readable (changes file size from bytes to K, M, and G). (Notice the `.` and the `..` at the top? Those are references to "here" (1 dot) and "parent" (2 dots).  Seems silly, but we use those in commands (you'll see).
- If you want to move around (change directories) type: `cd dir_name` . This will change your directory to `dir_name`.
- If you want to back out of a directory type: `cd ..` (See! We use them). The dotdot means "backup".
- If you want to refer to "your current directory", you can use the `.` . 
- To create a directory, type: `mkdir dir_name`.

**Also!**

- Remember your :arrow_up: and :arrow_down: arrows! These will step through your previous commands.
- Type `history` to see ALL the commands you've type EVER!

## Hello World App

Let's get started by creating a "Hello World" `Node.js` app.

Create an empty folder called "hello_world", navigate into it and open VS Code:

```bash
mkdir hello_world
cd hello_world
code .
```

> Note: `code .` means open VS Code in the current directory. (See I told you we use the . and .. ).

- VS Code is now open and your `hello_world` folder is loaded. 
- Create a file called `app.js` and put the following in it:

```js
var msg = 'Hello World';
console.log(msg);
```

- You can now run this code a couple of different ways.
    1. Since we installed `code runner` you can simply right click and choose `Run Code`. It should open up a mini terminal in your IDE and show the output.
    2. Or go back to your terminal and type `node app.js` to run it (the integrated terminal doesn't need code runner installed, but it does make it a little easier).
    
## Express Server App

Install the Express Generator by running the following from a terminal:

```bash
npm install -g express-generator
```

The `-g` switch installs the Express Generator globally on your machine so you can run it from anywhere.

We can now scaffold a new Express application called `myExpressApp` by running:

```bash
express myExpressApp
```

This creates a new folder called `myExpressApp` with the contents of your application. To install all of the application's dependencies (again shipped as NPM modules), go to the new folder and execute `npm install`:

```bash
cd myExpressApp
npm install
```

At this point, we should test that our application runs. The generated Express application has a `package.json` file which includes a `start` script to run `node ./bin/www`. This will start the Node.js application running.

From a terminal in the Express application folder, run:

```bash
npm start
```

The Node.js web server will start and you can browse to `http://localhost:3000` to see the running application.

## Helpful Links

- https://code.visualstudio.com/docs/nodejs/nodejs-tutorial
- https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/
- https://www.howtogeek.com/261449/how-to-install-linux-software-in-windows-10s-ubuntu-bash-shell/
  
