## Install Mongo

Installing MongoDB on Ubuntu is pretty easy. By default, MongoDB binds to localhost (127.0.0.1), which means it can only be accessed from the machine it's installed on, which is a little safer than opening yet another port in our firewall. 

https://www.digitalocean.com/community/tutorials/how-to-install-mongodb-on-ubuntu-20-04


## Steps

### 1. Add MongoDB 

Adds the repository and gpg key


```bash
wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc |  gpg --dearmor | sudo tee /usr/share/keyrings/mongodb.gpg > /dev/null
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list

```


### 2. Update Package Index and Install MongoDB

Update your local package index, then install MongoDB as usual:

```bash
sudo apt-get update
sudo apt-get install -y mongodb-org
```

### 3. Start MongoDB Service

After installation, start MongoDB and enable it to start on boot:

```bash
sudo systemctl start mongod
```

### 4. Verify MongoDB Installation

Check the status of the MongoDB service to ensure it's running:

```bash
sudo systemctl status mongod
```

If MongoDB doesn't start or you encounter issues, you might need to run `sudo systemctl daemon-reload` first.

### 5. Enable MongoDB to Start on Boot
To ensure MongoDB starts when your system boots, use the `enable` command:

```bash
sudo systemctl enable mongod
```

### Ensuring Localhost Access Only
By default, MongoDB binds to 127.0.0.1 (localhost), which restricts access to the local machine only. To verify this, check the MongoDB configuration file, typically located at `/etc/mongod.conf`. Look for the `net` section and ensure `bindIp` includes 127.0.0.1:

```yaml
net:
  port: 27017
  bindIp: 127.0.0.1
```

If you've modified this setting or if it includes other IP addresses, ensure it's set only to `127.0.0.1` to restrict access to localhost.

### 6. Accessing MongoDB
To start using MongoDB, you can enter the MongoDB shell by typing:

```bash
mongosh
```

This connects to the MongoDB instance running on localhost by default.


## VSCode Access

### For MongoDB:

1. Connect to your server via the SSH plugin in VScode. 

2. Install **MongoDB for VS Code**:
   - **Name**: MongoDB for VS Code
   - **Publisher**: MongoDB Inc.

   This extension provides an intuitive interface for connecting to MongoDB and working with MongoDB Atlas. You can write MongoDB queries and commands with rich IntelliSense, explore your schemas, and even export MongoDB Playground scripts to Node.js.

   #### How to Use:
   - **Install the Extension**: Look for "MongoDB for VS Code" in the Extensions view (`Ctrl+Shift+X`) and install it.
   - **Connect to Your Database**: You can connect to your MongoDB instance by adding a new connection string in the MongoDB view. Use your MongoDB URI to connect.
   - **Explore and Interact**: The extension allows you to explore collections and documents, run MongoDB commands in a playground, and even visualize your query results.


## Mongo With Python

You'll need to use the `pymongo` package, which is the official MongoDB driver for Python. If you haven't installed `pymongo` yet, you can do so by running `pip install pymongo` in your terminal.

Here's a simple script that creates a collection (if it doesn't already exist) and then adds the provided document to this collection:

```python
from pymongo import MongoClient

# Document to be inserted
document = {
    "id": 1,
    "first_name": "Thia",
    "last_name": "Sapsforde",
    "email": "tsapsforde0@cbslocal.com"
}

# Connect to the MongoDB server (defaults to localhost:27017)
client = MongoClient('localhost', 27017)

# Select the database, if it doesn't exist, it will be created when the first document is inserted
db = client['my_database']

# Select the collection, similar to the database, it will be created on the first insert
collection = db['my_collection']

# Insert the document into the collection
insert_result = collection.insert_one(document)

# Print the ID of the inserted document
print(f'Document inserted with ID: {insert_result.inserted_id}')
```

### Key Points:

- `MongoClient('localhost', 27017)`: This line creates a connection to the MongoDB server running on localhost at the default port (27017). You can adjust the host and port as necessary for your MongoDB server setup.
- `client['my_database']`: This selects the database `my_database`. If this database doesn't exist, MongoDB will create it when you insert the first document.
- `db['my_collection']`: This selects the collection `my_collection` within the database. Similar to the database, the collection will be created upon the first document insertion if it doesn't already exist.
- `collection.insert_one(document)`: This line inserts the document into the collection. The `insert_one` method returns an `InsertOneResult` object, which contains the ID of the inserted document.

Here's an example that demonstrates how to insert a list of documents into a MongoDB collection:

```python
from pymongo import MongoClient

# List of documents to be inserted
documents = [
    {"id": 1, "first_name": "Thia", "last_name": "Sapsforde", "email": "tsapsforde0@cbslocal.com"},
    {"id": 2, "first_name": "John", "last_name": "Doe", "email": "johndoe@example.com"},
    {"id": 3, "first_name": "Jane", "last_name": "Doe", "email": "janedoe@example.com"},
    # Add more documents as needed
]

# Connect to the MongoDB server (defaults to localhost:27017)
client = MongoClient('localhost', 27017)

# Select the database. It will be created if it doesn't exist yet
db = client['my_database']

# Select the collection. It will be created on the first insert
collection = db['my_collection']

# Insert the list of documents into the collection
insert_result = collection.insert_many(documents)

# Print the IDs of the inserted documents
print(f'Documents inserted with IDs: {insert_result.inserted_ids}')
```

### Key Points:

- `insert_many(documents)`: This method takes a list of document dictionaries and inserts them into the collection. The method returns an `InsertManyResult` object, which contains the IDs of all inserted documents.
- `insert_result.inserted_ids`: This attribute of the `InsertManyResult` object contains a list of the `_id` values of the inserted documents.
- The list `documents` can contain any number of document dictionaries you wish to insert. Just make sure each dictionary in the list represents a valid document that you want to store in your MongoDB collection.


# NOT TESTED

## Mongo Web Admin


### 1. **mongo-express**

**mongo-express** is a web-based MongoDB admin interface written with Node.js, Express, and Bootstrap3. It's designed to be lightweight and easy to use.

#### Installing mongo-express:

Since mongo-express is a Node.js application, you'll need Node.js and npm (Node.js package manager) installed on your system. Here's how you can set up mongo-express:

1. **Install Node.js and npm:**
   If Node.js and npm aren't already installed, you can install them with:

   ```bash
   sudo apt update
   sudo apt install nodejs npm
   ```

2. **Install mongo-express:**
   You can install mongo-express globally using npm:

   ```bash
   sudo npm install -g mongo-express
   ```

3. **Configure mongo-express:**
   After installation, you can configure mongo-express by editing its config file. By default, mongo-express looks for a config file in `/etc/mongo-express/`, or you can copy the default config file from the installation directory and modify it according to your needs:

   ```bash
   sudo mkdir /etc/mongo-express
   sudo cp /usr/lib/node_modules/mongo-express/config.default.js /etc/mongo-express/config.js
   sudo nano /etc/mongo-express/config.js
   ```

   Make sure to set the MongoDB URI to your local MongoDB instance, and configure any other settings like authentication as needed.

4. **Run mongo-express:**
   You can start mongo-express with the following command, specifying the path to your configuration file:

   ```bash
   mongo-express -c /etc/mongo-express/config.js
   ```

   By default, mongo-express will start on port 8081. You can access it by navigating to `http://localhost:8081` in your web browser.

### 2. **AdminMongo**

**AdminMongo** is another web-based tool that provides a management interface for MongoDB. It's also built with Node.js and offers a simple, user-friendly UI to manage your MongoDB databases.

#### Installing AdminMongo:

The installation process for AdminMongo is similar to mongo-express, as it's also a Node.js application.

1. **Clone the AdminMongo repository:**
   First, clone the AdminMongo GitHub repository to your local machine:

   ```bash
   git clone https://github.com/mrvautin/adminMongo.git
   cd adminMongo
   ```

2. **Install dependencies:**
   Inside the `adminMongo` directory, install the necessary Node.js dependencies:

   ```bash
   npm install
   ```

3. **Start AdminMongo:**
   Once the dependencies are installed, you can start AdminMongo with:

   ```bash
   npm start
   ```

   AdminMongo listens on port 1234 by default, so you can access it by going to `http://localhost:1234` in your web browser.

### Security Considerations:
When deploying web-based admin tools, especially in a production environment, it's crucial to ensure secure access. Consider using reverse proxies, SSL/TLS encryption, and authentication mechanisms to protect your admin interfaces.
