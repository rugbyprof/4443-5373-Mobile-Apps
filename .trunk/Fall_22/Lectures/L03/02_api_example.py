"""This is a basic example of an api impleme implented with pythons
`FastApi`. 
"""
import uvicorn  # lib to run min server to listen on port
from fastapi import FastAPI  # fast api lib

app = FastAPI()  # instance of `FastApi` doesn't have to be
# called `app`


@app.get("/")
async def default():
    """ Base route that returns: {"result": "success"}
        URL: 
           http://localhost:1234

    """
    return {"result": "success"}


@app.get("/hello")
async def hello(fname: str = 'who are you?'):
    """ Hello route that takes in an example param (your name)
        URL: 
           http://localhost:1234/hello?fname=yourName
           
    """
    return {"hello": fname}


if __name__ == "__main__":
    #host="0.0.0.0" for running on server with domain name
    #or
    #host="ip.add.ress" for server ip
    uvicorn.run("sapi:app",
                host="127.0.0.1",
                port=1234,
                log_level="info",
                reload=True)
