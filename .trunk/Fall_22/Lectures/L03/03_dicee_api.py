# from typing import Optional
# from pydantic import BaseModel
import uvicorn
# import json
# import copy
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

# from pydantic import BaseModel

# class Item(BaseModel):
#     question: str
#     answer: bool
#     position: int

import sys
import random
import math

description = """
Dicee API 🚀

## Random Dice Values 
"""

app = FastAPI(
    title="Simple Random Dice Vals",
    description=description,
    version="0.0.1",
    terms_of_service="http://killzonmbieswith.us/terms/",
    contact={
        "name": "Cha Cha Schwarzenegger",
        "url": "http://killzonmbieswith.us/contact/",
        "email": "chacha@killzonmbieswith.us",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)
"""
  ___  ___  _   _ _____ ___ ___ 
 | _ \/ _ \| | | |_   _| __/ __|
 |   / (_) | |_| | | | | _|\__ \
 |_|_\\___/ \___/  |_| |___|___/
                               
"""


@app.get("/")
async def docs_redirect():
    return RedirectResponse(url="/docs")


@app.get("/rand/")
async def myRand():
    """ 
    Description:
        Get a random number
    Params: 
        None
    Returns:
        json / 
        double : value between 0 and 1 
    """
    return {"success": True, "num": random.random()}


@app.get("/randInt/")
async def myRandInt(min: int = 0, max: int = pow(2, 30)):
    """ 
    Description:
        Get a random number
    Params: 
        (int) min :  min value default = 0
        (int) max :  max value default = 2^30
    Returns:
        json / 
        int val between 0 and 2^30
    """

    return {"success": True, "num": random.randint(min, max)}


@app.get("/seed/")
async def myRandSeed(seed: int = 0):
    """ 
    Description:
        Seed random number generator
    Params: 
        (int) seed : integer value to use as seed 
    Returns:
        bool : success = true
    """

    if seed == 0:
        seed = None

    random.seed(seed)

    return {"success": True}


if __name__ == "__main__":
    #host="0.0.0.0" for running on server with domain name
    #or
    #host="ip.add.ress" for server ip
    uvicorn.run("zapi:app",
                host="127.0.0.1",
                port=6767,
                log_level="info",
                reload=True)
