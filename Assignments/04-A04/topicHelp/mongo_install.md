To install MongoDB on Ubuntu, you can follow these steps:

1. **Import MongoDB Repository**: MongoDB provides official repositories for Ubuntu. Import the public key used by the package management system:

```bash
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
```

2. **Add MongoDB Repository**: Add the MongoDB repository to the package management system:

```bash
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu $(lsb_release -cs)/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
```

3. **Update Repository**: Update the package database:

```bash
sudo apt update
```

4. **Install MongoDB**: Install the MongoDB packages:

```bash
sudo apt install mongodb-org
```

This command installs several packages, including the MongoDB server (`mongod`) and the MongoDB client (`mongo`).

5. **Start MongoDB Service**: Start the MongoDB service:

```bash
sudo systemctl start mongod
```

6. **Enable MongoDB Service**: Enable MongoDB to start on system boot:

```bash
sudo systemctl enable mongod
```

7. **Verify MongoDB Installation**: Check the status of the MongoDB service to ensure that it's running:

```bash
sudo systemctl status mongod
```

You should see output indicating that the service is active and running.

That's it! MongoDB should now be installed and running on your Ubuntu system. You can access the MongoDB shell by typing `mongo` in your terminal.
