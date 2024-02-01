## Assignment 3 - Create your own server.
#### Due: 02-04-2024 (Sun @ 11:59)

I know the class is **TTh**, but I want it done by end of weekend.

#### Command History

- Command History From Class [HERE](./history.md)

-----

#### DIGITAL OCEAN TUTORIALS:

<a href="https://www.digitalocean.com/community/tutorials"><img src="https://upload.wikimedia.org/wikipedia/commons/f/ff/DigitalOcean_logo.svg" width="100"></a>


#### 1. [Sign up](https://cloud.digitalocean.com/registrations/new) for Digital Ocean.

This will cost you around $6.00 + tax for the entire month. 

-----

#### 2. Wsl On Windows

To get WSL workin on Windows, there are a few docs that microsoft provides:

- Basic getting it working: 
  - [How to install Linux on Windows with WSL](https://learn.microsoft.com/en-us/windows/wsl/install)
- An advanced dev environment setup. We won't need all of the included items in this tutorial, but I thought many were interesting for us to consider (like Docker containers). Again, this is just an interesting page for windows users, but I only need you to get WSL working.
  - [Set up a WSL development environment](https://learn.microsoft.com/en-us/windows/wsl/setup/environment)

- **Basic Linux Commands**
  - [Linux Command Line Primer](https://www.digitalocean.com/community/tutorials/a-linux-command-line-primer)

-----

#### 3. Generating SSH Keys

I placed a walkthrough and explanation in this folder in the first link below, however both of them show you kind of the same thing with slightly different explanations. You won't really need to generate ssh keys on your DO droplet, since it just needs your public key placed in `known-hosts` you will generate using WSL terminal.

- [Generating SSH Keys](./ssh-keys.md)
- [Digital Ocean Version](https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server)

-----

#### 4. Creating a new Droplet

- This tutorial is for someone who registered with Digital Ocean already.
- Don't worry about messing anything up, since you can destroy and recreate the droplet in no time at all.
- Also, I can help through zoom or office hours if need be.

[Droplet Tutorial](https://docs.digitalocean.com/products/droplets/how-to/create/).

**IMPORTANT**
- The IP address that is assigned to your "droplet", is your only connection to your server.
- You choose your own root password.
- You need both **`IP address`** & **`password`** to access your new server (for now).


-----

#### 5. Server Setup

[Initial Server Setup](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-22-04)

- Logging in as root
- Creating Users
- Privileges
- Firewall

-----

#### 6. SSHing Into Your Server

[SSH Tutorial](https://docs.digitalocean.com/products/droplets/how-to/connect-with-ssh/)
- This tutorial is about connecting to your server with console.

-----

#### 7. Me Accessing Your Server

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

#### 8. Package Management:

Updating your packages after login:

```bash
# update the package repositories
$ sudo apt-get update

# actually update any out of data packages
$ sudo apt-get upgrade -y 

```

[1]:  ../../Resources/01-icons/icons8-folder-24.png
[2]: ../../Resources/01-icons/DigitalOcean_logo.png
[9]:  ../../Resources/01-icons/icons8-markdown-24.png


