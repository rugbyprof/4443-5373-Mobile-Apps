## Assignment 4 - Mongo DB
#### Due: 02-20-2024 (Tue @ 11 or 4)

## Files

|   #   | Name                   | Description                                    |
| :---: | :--------------------- | :--------------------------------------------- |
|   1   | [candyAPI](candyAPI)   | Necessary code to load and run your api.       |
|   2   | [topicHelp](topicHelp) | Different files to help with different topics. |



## Basic Overview

You are going to:
1. Populate MongoDB:
   - Upload the code to populate the mongo db on your own server. Code is [HERE](./candyAPI/).
2. Create New Routes: 
   - Get a copy of the mongoDb interface class to help you with managing mongoDB via Fastapi and PyMongo. Code is [HERE](./candyAPI/mongoDBInterface.py) and edit the routes in [api.py](./candyAPI/api.py) to be tailored to our candy database.
3. Register API:
   - Register your api with your server so that it will always be up and running.  

### Populate MongoDB

***Upload relevant files to your own server.***

There are three ways to make this happen.

#### 1.Drag N Drop

If you have the files downloaded, you can simple drag and drop them to your vscode instance that is connected to your server.

#### 2. Git Clone

1. Connect to your server via terminal. 
2. Run `git clone https://github.com/rugbyprof/4443-5373-Mobile-Apps.git`
3. Change to the directory where you want your code to go.
4. Then copy the appropriate folder using a command like: 
   
```bash
cp -r 4443-5373-Mobile-Apps/Assignments/04-A04/candyAPI .
# This command means "copy recursively the folder canyAPI to `here` (wherever you currently are)"
```
<sup>1.The -r means recursive. This is necessary with folders.
<sup>2. Notice the `.` after the path, that means "here". 

#### 3. Rsync

Also if you already have them downloaded, you can use rsync to upload them. Here's a basic example of how to use `rsync` to upload a folder from your local machine to a remote server:

```sh
rsync -avz /path/to/local/folder/ username@remote_host:/path/to/remote/folder/
```

Explanation of the options:

- `-a`: This stands for "archive mode," which ensures that symbolic links, devices, attributes, permissions, ownerships, etc., are preserved in the transfer.
- `-v`: This enables verbose mode, which provides detailed information about the file transfer process.
- `-z`: This option enables compression during the transfer, which can speed up the transfer of large files over the network. It doesn't compress the files on the disk; it only compresses the data during the transfer.

```sh
rsync -avz /path/to/local/folder/ username@remote_host:/path/to/remote/folder/
```
><sup>**Note the trailing slashes (`/`) after the folder paths. In `rsync`, including a trailing slash on the source directory means "copy the contents of this directory," as opposed to "copy the directory by name."**</sup>

### Create New Routes

***Load Mongo DB***

1. Now that you have the files copied onto your server, you can run `loadMongo.py` to create your "candy_store" db and the "candies" collection.  
2. Make sure you are in the `candyAPI` folder. Then run:

```bash
python3 loadMongo.py
```
><sup>Or however you run python on your server</sup>

***Updating Routes***

We need routes that will do basic querying of our mongo `candy store`. Below is a list of necessary queries.

1. Get all candies.
2. Get a list of categories.
3. Get candies in a specific category.
4. Get candies with a key word in the description.
5. Get candies with a key word in the name.
6. Get candies by price range.
7. Get candy with with a specified ID.
8. Get a candy image.
9. Update a candies price. 
10. Update a candies { ....... }
11. Delete a candy.

### Register Api

Use the help [HERE](./topicHelp/registerApi.md) to get your api registered with your server to keep it alive.


### Requirements

- Create a folder called `A04` in your Assignments folder AND on your server under the root folder.
- Place your mongo classes and api code in that folder. 
- This instance of the API should be up and running if I goto http://your.ip.address:8080
- I should be able to run all of the specified routes from above.


