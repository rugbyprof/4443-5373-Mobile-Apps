## Assignment 4 - Mongo DB + FastApi
#### Due: 03-05-2024 (Tue @ 11 or 4)

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

### Testing API

- You should write a file called `apiTests.py` that would invoke each route necessary to show that they all work successfully. 
- I have a nice example of code and test calls [HERE](./topicHelp/apiTests.md) to help you automate some tests for all your routes.

## Registering Api

#### Step 1
- Create a virtual environment and install requirements.
- This will create a folder called `myvenv` in your project folder.
- Project folder for this example is: `/root/A04`

requirements.txt 
```txt
fastapi
uvicorn
rich
```

```bash
cd /root/A04
python3 -m venv myvenv
source myvenv/bin/activate #prompt will change with name of venv in front of it
pip install -r requirements.txt
```

#### Step 2

- Create a service file:
```bash
cd /etc/systemd/system   # change into system folder
nano A04.service    # create a service file
```

Add this code changing appropriate parts for your own script
```bash
 [Unit]
    Description=FastAPI app
    After=network.target

    [Service]
    User=root
    WorkingDirectory=/root/A04
    ExecStart=/root/A04/myvenv/bin/python /root/A04/api.py

    Restart=always

    [Install]
    WantedBy=multi-user.target
```
#### Step 3


Test the command from your service file, that starts your `api.py` to make sure it works:
```bash
$/root/A04/myvenv/bin/python /root/A04/api.py
```

#### Step 4

```bash
sudo systemctl daemon-reload  # register your changes
sudo systemctl enable A04     # register with system to start on reboot
sudo systemctl start A04      # use systemctl to start your app
sudo systemctl status A04     # check if it is really running

sudo systemctl stop A04       # this will stop it
sudo systemctl restart A04    # this will restart it
sudo systemctl disable A04    # this will stop it from restarting at boot
```

There are some other ways of registering your api [HERE](./topicHelp/registerApi.md).


## Requirements

- Create a folder called `A04` in your Assignments folder AND on your server under the root folder.
- Place your mongo classes and api code in that folder. 
- This instance of the API should be up and running if I goto http://your.ip.address:8084
- I should be able to run all of the specified routes from above.
- You should also provide python `test.py` file, that runs tests on all the routes within your project folder. Remember the helper file [HERE](./topicHelp/apiTests.md)


