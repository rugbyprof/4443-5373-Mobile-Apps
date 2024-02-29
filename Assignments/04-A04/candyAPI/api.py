# Libraries for FastAPI
from fastapi import FastAPI, Query, Path, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, Response,  FileResponse
from mongoManager import MongoManager
from pydantic import BaseModel
from pymongo import MongoClient
from typing import List
import base64
import json
import uvicorn
import os
from random import shuffle
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)


class Person(BaseModel):
    first: str
    last: str 
    email: str
    password: str 

"""
           _____ _____   _____ _   _ ______ ____
     /\   |  __ \_   _| |_   _| \ | |  ____/ __ \
    /  \  | |__) || |     | | |  \| | |__ | |  | |
   / /\ \ |  ___/ | |     | | | . ` |  __|| |  | |
  / ____ \| |    _| |_   _| |_| |\  | |   | |__| |
 /_/    \_\_|   |_____| |_____|_| \_|_|    \____/

The `description` is the information that gets displayed when the api is accessed from a browser and loads the base route.
Also the instance of `app` below description has info that gets displayed as well when the base route is accessed.
"""

description = """🤡
(This description is totally satirical and does not represent the views of any real person alive or deceased. 
And even though the topic is totally macabre, I would love to make anyone who abuses children very much deceased.
However, the shock factor of my stupid candy store keeps you listening to my lectures. If anyone is truly offended
please publicly or privately message me and I will take it down immediately.)🤡


## Description:
Sweet Nostalgia Candies brings you a delightful journey through time with its extensive collection of 
candies. From the vibrant, trendy flavors of today to the cherished, classic treats of yesteryear, 
our store is a haven for candy lovers of all ages (but mostly kids). Step into a world where every shelf and corner 
is adorned with jars and boxes filled with colors and tastes that evoke memories and create new ones. 
Whether you're seeking a rare, retro candy from your childhood or the latest sugary creation, Sweet 
Nostalgia Candies is your destination. Indulge in our handpicked selection and experience a sweet 
escape into the world of confectionery wonders! And don't worry! We will watch your kids!! (😉)

#### Contact Information:

- **Address:** 101 Candy Lane, Alcatraz Federal Penitentiary, San Francisco, CA 94123.
- **Phone:** (123) 968-7378 [or (123 you-perv)]
- **Email:** perv@kidsinvans.com
- **Website:** www.kidsinvans.fun

"""

# Needed for CORS
# origins = ["*"]


# This is the `app` instance which passes in a series of keyword arguments
# configuring this instance of the api. The URL's are obviously fake.
app = FastAPI(
    title="KidsInVans.Fun🤡",
    description=description,
    version="0.0.1",
    terms_of_service="http://www.kidsinvans.fun/worldleterms/",
    contact={
        "name": "KidsInVans.Fun",
        "url": "http://www.kidsinvans.fun/worldle/contact/",
        "email": "perv@www.kidsinvans.fun",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

# Needed for CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

"""
  _      ____   _____          _         _____ _                _____ _____ ______  _____
 | |    / __ \ / ____|   /\   | |       / ____| |        /\    / ____/ ____|  ____|/ ____|
 | |   | |  | | |       /  \  | |      | |    | |       /  \  | (___| (___ | |__  | (___
 | |   | |  | | |      / /\ \ | |      | |    | |      / /\ \  \___ \\___ \|  __|  \___ \
 | |___| |__| | |____ / ____ \| |____  | |____| |____ / ____ \ ____) |___) | |____ ____) |
 |______\____/ \_____/_/    \_\______|  \_____|______/_/    \_\_____/_____/|______|_____/

This is where you will add code to load all the countries and not just countries. Below is a single
instance of the class `CountryReader` that loads countries. There are 6 other continents to load or
maybe you create your own country file, which would be great. But try to implement a class that 
organizes your ability to access a countries polygon data.
"""

mm = MongoManager(db='candy_store_2')
mm.setDb('candy_store_2')

"""
  _      ____   _____          _        __  __ ______ _______ _    _  ____  _____   _____
 | |    / __ \ / ____|   /\   | |      |  \/  |  ____|__   __| |  | |/ __ \|  __ \ / ____|
 | |   | |  | | |       /  \  | |      | \  / | |__     | |  | |__| | |  | | |  | | (___
 | |   | |  | | |      / /\ \ | |      | |\/| |  __|    | |  |  __  | |  | | |  | |\___ \
 | |___| |__| | |____ / ____ \| |____  | |  | | |____   | |  | |  | | |__| | |__| |____) |
 |______\____/ \_____/_/    \_\______| |_|  |_|______|  |_|  |_|  |_|\____/|_____/|_____/

This is where methods you write to help with any routes written below should go. Unless you have 
a module written that you include with statements above.  
"""



"""
  _____   ____  _    _ _______ ______  _____
 |  __ \ / __ \| |  | |__   __|  ____|/ ____|
 | |__) | |  | | |  | |  | |  | |__  | (___
 |  _  /| |  | | |  | |  | |  |  __|  \___ \
 | | \ \| |__| | |__| |  | |  | |____ ____) |
 |_|  \_\\____/ \____/   |_|  |______|_____/

 This is where your routes will be defined. Routes are just python functions that retrieve, save, 
 delete, and update data. How you make that happen is up to you.
"""


@app.get("/")
async def docs_redirect():
    """Api's base route that displays the information created above in the ApiInfo section."""
    return RedirectResponse(url="/docs")



@app.get("/candies")
def list_all_candies():
    """
    Retrieve a list of all candies available in the store.
    """
    mm.setCollection('candies')
    result = mm.get()
    return result


@app.get("/candies/category/{category}")
def candies_by_category(category: str):
    """
    Search for candies based on a query string (e.g., name, category, flavor).
    """
    mm.setCollection('candies')
    result = mm.get(
        query = {'category':category},
        filter = {"_id":0,"name":1,"price":1,"category":1})
    return result


@app.get("/candies/id/{id}")
def get_candy_by_id(
    id: str
):
    """
    Get detailed information about a specific candy.
    """
    mm.setCollection('candies')
    result = mm.get(
        query = {'_id':int(id)})
    return result

@app.get("/image/base64/{image_id}")
def get_image(image_id: str):
    mm.setCollection('images')
    base64_image = mm.get_image_from_mongodb(image_id)
    if not base64_image:
        raise HTTPException(status_code=404, detail="Image not found")

    # Decode the Base64 string
    image_bytes = base64.b64decode(base64_image)

    # Return the raw image bytes with the appropriate content type
    return Response(content=image_bytes, media_type="image/png")

@app.get("/image/")
def get_image(img_id:str):
    mm.setCollection('candies')
    result = mm.get(query = {'_id':int(img_id)})

    return FileResponse(result['data']['img_path'])

@app.post("/register")
def register(person: Person):
    """
    Add a new candy to the store's inventory.
    """
    mm.setCollection("users")
    person.password = hash_password(person.password)
    print(hash_password(person.password))
    mm.post(person.dict())
    

@app.post("/candies")
def add_new_candy():
    """
    Add a new candy to the store's inventory.
    """
    pass


@app.put("/candies/{candy_id}")
def update_candy_info(candy_id: int):
    """
    Update information about an existing candy.
    """
    pass


@app.delete("/candies/{candy_id}")
def delete_candy(candy_id: int):
    """
    Remove a candy from the store's inventory.
    """
    pass


@app.get("/categories")
def list_categories():
    """
    Get a list of candy categories (e.g., chocolates, gummies, hard candies).
    """
    pass


"""
This main block gets run when you invoke this file. How do you invoke this file?

        python api.py 

After it is running, copy paste this into a browser: http://127.0.0.1:8080 

You should see your api's base route!

Note:
    Notice the first param below: api:app 
    The left side (api) is the name of this file (api.py without the extension)
    The right side (app) is the bearingiable name of the FastApi instance declared at the top of the file.
"""
if __name__ == "__main__":
    #gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:main --bind 0.0.0.0:8000 --keyfile=./key.pem --certfile=./cert.pem

    # uvicorn.run("api:app", host="kidsinvans.fun", port=8080, log_level="debug", reload=True)

    uvicorn.run(
        "api:app",
        host="0.0.0.0",  # Use 0.0.0.0 to bind to all network interfaces
        #port=443,  # Standard HTTPS port
        port=8080,  # Standard HTTPS port
        log_level="debug",
        ssl_keyfile="/etc/letsencrypt/archive/kidsinvans.fun/privkey1.pem",
        ssl_certfile="/etc/letsencrypt/archive/kidsinvans.fun/fullchain1.pem",
        reload=True
    )
"""                                   ^
                                      |
CHANGE DOMAIN NAME                    |              

"""