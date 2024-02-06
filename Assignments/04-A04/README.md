## Assignment 4 - Mongo DB
#### Due: 02-13-2024 (Tue @ 11 or 4)

## Files

|   #   | Name                                               | Description                                         |
| :---: | :------------------------------------------------- | :-------------------------------------------------- |
|   0   | [candyAPI](./candyAPI/README.md)                   | Folder with all the starter code.                   |
|   1   | [apiRouteHelp.md](./apiRouteHelp.md)               | Example route syntax plus other stuff               |
|   2   | [mongoDbsCollections.md](./mongoDbsCollections.md) | Talk about Mongo Dbs and Collections + more.        |
|   3   | [pymongoHelp.md](./pymongoHelp.md)                 | Pymongo snippets on various topics.                 |
|   4   | [registerApi.md](./registerApi.md)                 | Register your api with the server to keep it alive. |
|   5   | [restfulStyle.md](./restfulStyle.md)               | What is RESTful all about?                          |
|   6   | [securingMongo.md](./securingMongo.md)             | Secure mongo by adding users and require passwords. |






## Overview

Code you will need the following Python scripts:

- [api.py](./candyAPI/api.py) 
- [mongoDBInterface.py](./candyAPI/mongoDBInterface.py)
- [loadMongo.py](./candyAPI/loadMongo.py)

And the folder [categoryJson](./candyAPI/categoryJson/) that contains all the category files with each categories category data.

Using all of these files, we should now have what we need to:
1. Create our Mongo DB `candy_store` and the collection `candies` 
2. Load the `candies` collection (with [loadMongo.py](./candyAPI/loadMongo.py))
3. Start completing all api routes given the file [api.py](./candyAPI/api.py) and all of its route stubs. Those aren't necessarily everything you need, there will definitely need to be some tweaking.
4. Register your api with the server so it stays up and running. 

Ultimately the goal is to have your api located at: http://your.ip.address:8080 always up and available without worrying that you need to restart it all the time. 

## Specifics



