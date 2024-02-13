## Mongo Users

Securing MongoDB by enabling authentication and allowing external connections in a secure manner involves several steps. Read through the steps below to add a user to your DB, and then force it to require username and password.

### Step 1: Enable Authentication in MongoDB

1. **Edit the MongoDB Configuration File**:
   Open the MongoDB configuration file (`mongod.conf`), usually found in `/etc/mongod.conf` or `/etc/mongodb.conf`, depending on your installation.

   ```bash
   sudo nano /etc/mongod.conf
   ```

2. **Enable Security Settings**:
   In the configuration file, look for the `security` section and enable authorization:

   ```yaml
   security:
     authorization: "enabled"
   ```

3. **Restart MongoDB**:
   Apply the changes by restarting the MongoDB service.

   ```bash
   sudo systemctl restart mongod
   ```

### Step 2: Create an Admin User

1. **Access the MongoDB Shell**:
   Access the MongoDB command line interface by running:

   ```bash
   mongo
   ```

2. **Switch to the admin Database**:
   MongoDB uses the `admin` database to store system-wide information. Switch to it by running:

   ```mongo
   use admin
   ```

3. **Create the Admin User**:
   Create a user with administrative privileges. Replace `yourAdminUser` and `yourAdminPassword` with your desired username and password.

   ```mongo
   db.createUser({
     user: "yourAdminUser",
     pwd: "yourAdminPassword",
     roles: [{ role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase"]
   })
   ```

### Step 3: Connect to MongoDB Using Credentials

Once authentication is enabled and you've created an admin user, you can connect to MongoDB using these credentials. From the command line, you can connect like this:

```bash
mongo -u yourAdminUser -p yourAdminPassword --authenticationDatabase admin
```

### Step 4: Enable External Connections

1. **Configure MongoDB to Listen on All Interfaces**:
   Edit the MongoDB configuration file again (`/etc/mongod.conf`) and find the `net` section. Change the `bindIp` value to `0.0.0.0` to allow connections from any IP address. Be aware that this can expose your database to the internet, so ensure you have proper firewall rules and network security in place.

   ```yaml
   net:
     port: 27017
     bindIp: 0.0.0.0
   ```

2. **Restart MongoDB**:
   Restart the MongoDB service to apply the changes.

   ```bash
   sudo systemctl restart mongod
   ```

## Optional

### Step 5: Secure External Connections

For securing external connections, it's recommended to use a VPN or an SSH tunnel rather than exposing MongoDB directly to the internet. Here's a basic overview of setting up an SSH tunnel:

1. **Create an SSH Tunnel**:
   This command sets up an SSH tunnel from your local machine to the MongoDB server, making the server's MongoDB instance accessible locally on port 27018.

   ```bash
   ssh -L 27018:localhost:27017 yourServerUser@yourMongoDbServer -f -N
   ```

2. **Connect to MongoDB Through the Tunnel**:
   Now, you can connect to MongoDB as if it was running on your local machine, but the connection is securely tunneled to the server.

   ```bash
   mongo -u yourAdminUser -p yourAdminPassword --port 27018 --authenticationDatabase admin
   ```

This SSH tunnel approach allows you to keep MongoDB bound to localhost on the server (enhancing security) while still accessing it externally through a secure channel.

### Additional Security Measures

- **Firewall Configuration**: Ensure your firewall is configured to only allow connections to MongoDB (default port 27017) from trusted IP addresses, or better yet, keep it bound to `127.0.0.1` and use SSH tunnels or VPNs for external access.
- **Regularly Update MongoDB**: Keep your MongoDB server updated to the latest stable version to ensure you have the latest security patches.
- **Backup Regularly**: Regularly backup your MongoDB data to recover from any potential data loss scenarios.

These steps will significantly enhance the security of your MongoDB installation while enabling authenticated and secure external connections.

