## Assignment 3 - Create Server & Run Api
#### Due: 02-22-2024 (Thu @ 11 or 4)


### Overview:

This assignment is about creating a cloud server, doing a little bit of system administration, and then getting the FastApi code discussed in class. All the steps below are there to help you: create, configure, install, and run all of the things you need to run your own API in the cloud.

### Command History

- This a list of most of the commands we used during lecture to help you perform the same stask on your server.
- Command History From Class [HERE](./history.md)

-----

### DIGITAL OCEAN TUTORIALS:

<a href="https://www.digitalocean.com/community/tutorials"><img src="https://upload.wikimedia.org/wikipedia/commons/f/ff/DigitalOcean_logo.svg" width="100"></a>


### 1. [Sign up](https://cloud.digitalocean.com/registrations/new) for Digital Ocean.

This will cost you around $6.00 + tax for the entire month. 

><sub>Note:Some students were having trouble with a 1GB server, so you should probably realize that if you run mongoDB and try and connect with VsCode, you may have issues and need to upgrade to a 2GB droplet</sub>
-----

### 2. Wsl On Windows

WSL on windows gives you access to a linux terminal with Ubuntu running. This is not 100% necessary but it will streamline many of the tasks you must perform by giving you a linux based virtual machine making it easier to perform certain tasks like ssh'ing into your droplet. Anything done on linux can be done on windows, but ... it's like you have to trick windows into making it happen. Trust me, learn how to use your linux shell, and you will be a better developer.

To get WSL workin on Windows, there are a few docs that microsoft provides:

- **Basic getting it working**
  - [How to install Linux on Windows with WSL](https://learn.microsoft.com/en-us/windows/wsl/install)
- An advanced dev environment setup. We won't need all of the included items in this tutorial, but I thought many were interesting for us to consider (like Docker containers). Again, this is just an interesting page for windows users, but I only need you to get WSL working.
  - [Set up a WSL development environment](https://learn.microsoft.com/en-us/windows/wsl/setup/environment)

- **Basic Linux Commands**
  - [Linux Command Line Primer](https://www.digitalocean.com/community/tutorials/a-linux-command-line-primer)

-----

### 3. Generating SSH Keys

I placed a walkthrough and explanation in this folder in the first link below, however both of them show you kind of the same thing with slightly different explanations. You won't really need to generate ssh keys on your DO droplet, since it just needs your public key placed in `known-hosts` you will generate using WSL terminal.

- [Generating SSH Keys](./ssh-keys.md)
- [Digital Ocean Version](https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server)

-----

### 4. Creating a new Droplet

- This tutorial is for someone who registered with Digital Ocean already.
- Don't worry about messing anything up, since you can destroy and recreate the droplet in no time at all.
- Also, I can help through zoom or office hours if need be.

[Droplet Tutorial](https://docs.digitalocean.com/products/droplets/how-to/create/).

**IMPORTANT**
- The IP address that is assigned to your "droplet", is your only connection to your server.
- You choose your own root password.
- You need both **`IP address`** & **`password`** to access your new server (for now).


-----

### 5. Server Setup

[Initial Server Setup](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-22-04)

- Logging in as root
- Creating Users
- Privileges
- Firewall

-----

### 6. SSHing Into Your Server

[SSH Tutorial](https://docs.digitalocean.com/products/droplets/how-to/connect-with-ssh/)
- This tutorial is about connecting to your server with console.

-----

### 7. Me Accessing Your Server

- Add my public key to: `authorized_keys` in the `/root/.ssh` folder.

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINnp5TGdQdQ+p4j6MAa2S2xWeoQCFmLd9H10S/UPBYed terry.griffin@msutexas.edu
```

- Here's the commands you need to run after copying the above key onto your clipboard.
```bash
ssh root@your.ip.address
cd .ssh 
nano authorized_keys
# at this point the file is open in nano and you simple paste my key on the first blank line.
# use ctrl-x to exit
#    hit y when it asks yes / no
#    hit enter to keep same filename
```

- Finally add your ip address to our class roster (far right column);
- https://docs.google.com/spreadsheets/d/1Ho6uAP-2KbAX4f_sv9KdA5Eszz7feF5p0I5YRFrXcfQ/edit?usp=sharing
- Just the ip address (e.g. 123.45.67.89 NOT http://123.45.67.89) 

-----

### 8. Package Management:

Updating your packages after login:

```bash
# update the package repositories
$ sudo apt-get update

# actually update any out of data packages
$ sudo apt-get upgrade -y 

```

### 9. Python

- Install Python3 (if not already installed)

- Check if Python 3 is installed by typing `python3 --version` in your terminal. If it's installed, you should see the Python version number. If not, install Python 3 by running:

```bash
sudo apt install python3
```

### 10. UFW

Enable your firewall (which is not enabled by default). Port 22 is open at droplet creation, otherwise you wouldn't be able to SSH into the server. But we will use UFW (Uncomplicated Fire Wall) to open up ports for SSH (port 22), HTTPS (port 443), and a range of ports from 8080 to 8085. I'll also show you how to check if these ports are open and how to see which services are listening on these ports.

First, enable UFW. This command starts the firewall and ensures it starts on boot:

```sh
sudo ufw enable
```

#### Allow SSH (Port 22)

To allow SSH connections (important if you're configuring a remote server to ensure you don't lock yourself out):

```sh
sudo ufw allow ssh
```
Or:
```sh
sudo ufw allow 22
```

#### Allow HTTPS (Port 443)

To allow HTTPS traffic:

```sh
sudo ufw allow https
```
Or:
```sh
sudo ufw allow 443
```

#### Allow Ports 8080 to 8085

To allow a range of ports (8080 to 8085) for both TCP and UDP traffic (adjust according to your specific needs, but most web services use TCP):

```sh
sudo ufw allow 8080:8085/tcp
sudo ufw allow 8080:8085/udp
```

#### Check Status

To check the status of UFW and see which rules are active (including ports):

```sh
sudo ufw status
```
Or for a more detailed view:
```sh
sudo ufw status verbose
```

#### Check Listening Services

To see which services are listening on which ports, you can use the `ss` or `netstat` commands. For simplicity and clearer output, `ss` is usually preferred:

```sh
sudo ss -tulnp
```

- `-t` for TCP
- `-u` for UDP
- `-l` for listening sockets
- `-n` for showing numerical addresses instead of trying to determine symbolic host, port, or user names
- `-p` for process name

This command will show you a list of all listening ports and the corresponding addresses. To filter this list to find specific ports or services, you can use `grep`, for example:

```sh
sudo ss -tulnp | grep ':22'
```

This command would show you if anything is listening on port 22 (SSH), and you can adjust the port number in the `grep` command to check other ports.

Remember, managing firewall settings and opening ports can expose your system to security risks if not done cautiously. Ensure you only open the ports you need for your applications and always use secure, authenticated, and encrypted protocols to protect your data in transit.


### 10. Run the Api

- Make sure you can run the basic api that we made in class together. Files and instructions are [here](./api_files/README.md)
- This instance for `A03` should listen on port `8083`.
- I will log in to start it, it doesn't have to registered with the servers systemctl.


## Checklist

1. Create a cloud based server preferably through digital ocean.
2. Update and upgrade all packages after login. I shouldn't see any security updates needed when I log in.
3. Enable the `UFW` firewall with the following ports open: 22, 80, 443, 8080-8085
4. Upload the api_files folder and ensure you can run python and the basic code that I provided. Instructions on uploading, ensuring python is setup, and running the api is all included here: [api_files](./README.md). 
5. Add my ssh key so I can login to your server.
6. Add your IP address to the course roster. Make sure it does not contain anything but the ip address itself. If you have a domain name, add that to the column to the right.
7. Place the API code in a folder called `A03` in your root folder.
8. I will start the API when I log in to make sure it runs. 

[1]:  ../../Resources/01-icons/icons8-folder-24.png
[2]: ../../Resources/01-icons/DigitalOcean_logo.png
[9]:  ../../Resources/01-icons/icons8-markdown-24.png





