from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import pymysql.cursors
import uvicorn
from mysqlDb import MysqlDb
from pydantic import BaseModel
from typing import Optional
import hashlib

"""
ApiInfo:
"""


class Candy(BaseModel):
    name: str
    description: str
    category_id: str
    price: float
    image: str


class Category(BaseModel):
    category_id: int
    name: str
    candies: Optional[list[Candy]] = None


class User(BaseModel):
    first_name: str
    last_name: str
    username: Optional[str] = None
    email: str
    password: str


class Login(BaseModel):
    username: Optional[str] = None
    email: str
    password: str


db_config = {
    "host": "localhost",
    # "user": "candyUser",
    # "password": "sweetsweetcandybaby",
    "user": "admin",
    "password": "1922MidWesternState!!123",
    "db": "CandyStore",  # Replace with your actual database name
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor,
}


def check_Exists(table, key, value):
    global conn
    query = f"SELECT * FROM '{table}' WHERE '{key}' = ''{value}'';"
    print(query)

    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
            return cursor.rowcount
    finally:
        conn.close()
        return 0


# Initialize the FastAPI app
app = FastAPI()

# Setup logging
# logger = setup_logging()


# Instantiate the database helper
db = MysqlDb()


@app.get("/")
async def docs_redirect():
    """Api's base route that displays the information created above in the ApiInfo section."""
    stuff = db.get_max_id("users", "user_id")
    # for k, v in stuff.items():
    #     print(f"{k} : {v}")
    print(stuff)
    return RedirectResponse(url="/docs")


@app.post("/register", tags=["User"])
def post_user(user: User):
    """
        Insert a new user into the database.
    ```
    {
      "first_name": "angel",
      "last_name": "badillo",
      "username": "",
      "email": "angel@badill.com",
      "password": "passwrodpasswrodpasswrod"
    }
    ```
    """
    max_user_id = db.get_max_id("users", "user_id")
    print(f"max user id: {max_user_id}")
    print(f"user: {user}")
    user_id = max_user_id + 1
    encrypeted = hashlib.sha256(user.password.encode()).hexdigest()

    query = f"INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `username`, `email`, `password`) VALUES ('{user_id}', '{user.first_name}', '{user.last_name}', '{user.username}', '{user.email}', '{encrypeted}');"
    # query = f"INSERT INTO Album (AlbumID, Title, ArtistID, Genre, ReleaseDate) VALUES ('{album_id}', '{album.title}', '{album.artist_id}', '{album.genre}', '{album.release_date}');"
    print(query)
    response = db.run_query(query, True)

    return response


@app.post("/login", tags=["User"])
def post_login(login: Login):
    """
        Insert a new user into the database.
    ```
    {
      "username": "lucygirl",
      "password": "lucy"
    }
    or
       {
      "email": "lucy@bob.com",
      "password": "lucy"
    }
    angel@badill.com
    passwordpasswordpassword

    hash_result = hashlib.sha256('lucy'.encode()).hexdigest() = dc99e9aa86fab83a062cff5e0808391757071a3d5dbb942802d5f923aaead3b4
    SELECT SHA2('lucy', 256); = 'dc99e9aa86fab83a062cff5e0808391757071a3d5dbb942802d5f923aaead3b4'
    UPDATE `users` SET `password` = SHA2('bob', 256) WHERE `user_id` = 52;
    ```
    """
    info = dict(login)
    email = info.get("email", None)
    username = info.get("username", None)
    password = info.get("password", None)

    password = hashlib.sha256(password.encode()).hexdigest()

    if email:
        user_exists = db.exists("users", "email", email)
    else:
        user_exists = db.exists("users", "username", username)

    if user_exists:
        query = f"SELECT password FROM `users` WHERE `email` = '{email}' OR `username` = '{username}';"
        print(query)
        response = db.run_query(query, False)
        print(response)

        print(f"inpassword: {password} == {response['data'][0]['password']}")
        if response["success"] and response["data"][0]["password"] == password:
            return {"success": True}

    return {"success": False}


if __name__ == "__main__":
    # gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:main --bind 0.0.0.0:8000 --keyfile=./key.pem --certfile=./cert.pem

    # uvicorn.run("api:app", host="kidsinvans.fun", port=8080, log_level="debug", reload=True)

    uvicorn.run(
        "api:app",
        host="0.0.0.0",  # Use 0.0.0.0 to bind to all network interfaces
        # port=443,  # Standard HTTPS port
        port=7373,  # Standard HTTPS port
        log_level="debug",
        # ssl_keyfile="/etc/letsencrypt/archive/sendmessage.live/privkey1.pem",
        # ssl_certfile="/etc/letsencrypt/archive/sendmessage.live/fullchain1.pem",
        reload=True,
    )


# @app.get("/")
# async def docs_redirect():
#     """Api's base route that displays the information created above in the ApiInfo section."""
#     return RedirectResponse(url="/docs")


# @app.get("/test_exists")
# def test_exists(table: str, key: str, value: str):
#     """Fetch a single artist by their ID, or all artists if no ID is provided."""
#     result = check_Exists(table, key, value)

#     if result > 0:
#         return f"'{key}' '{value}' exists in '{table}'"
#     else:
#         return f"'{key}' '{value}' does not exist in '{table}'"


# # Define routes for each table
# @app.get("/albums/'{album_id}'", tags=["Album"])
# def get_album(album_id: int = None):
#     """Fetch a single album by its ID, or all albums if no ID is provided."""
#     if album_id:
#         album = db.fetch_by_id("Album", album_id)
#         if album:
#             return album
#         raise HTTPException(status_code=404, detail="Album not found")
#     return db.fetch_all("Album")


# @app.get("/artists/", tags=["Artist"])
# def get_artist(artist_id: int = None):
#     """Fetch a single artist by their ID, or all artists if no ID is provided."""
#     if artist_id:
#         artist = db.fetch_by_id("Artist", "ArtistID", artist_id)
#         if artist:
#             return artist
#         raise HTTPException(status_code=404, detail="Artist not found")
#     return db.fetch_all("Artist")


# @app.get("/playlists/'{playlist_id}'", tags=["Playlist"])
# def get_playlist(playlist_id: int = None):
#     """Fetch a single playlist by its ID, or all playlists if no ID is provided."""
#     if playlist_id:
#         playlist = db.fetch_by_id("Playlist", playlist_id)
#         if playlist:
#             return playlist
#         raise HTTPException(status_code=404, detail="Playlist not found")
#     return db.fetch_all("Playlist")


# @app.get("/tracks/'{track_id}'", tags=["Track"])
# def get_track(track_id: int = None):
#     """Fetch a single track by its ID, or all tracks if no ID is provided."""
#     if track_id:
#         track = db.fetch_by_id("Track", track_id)
#         if track:
#             return track
#         raise HTTPException(status_code=404, detail="Track not found")
#     return db.fetch_all("Track")


# @app.get("/users/", tags=["User"])
# def get_user(user_id: int = None):
#     """Fetch a single user by their ID, or all users if no ID is provided."""
#     if user_id:
#         user = db.fetch_by_id("User", user_id)
#         if user:
#             return user
#         raise HTTPException(status_code=404, detail="User not found")
#     return db.fetch_all("User")


# #########################
# # POST METHODS
# #########################


# @app.post("/album", tags=["Album"])
# def post_album(self, album: Album, data):
#     """Insert a new album into the database."""
#     max_album_id = self.get_max_id("Album", "AlbumID")
#     album_id = max_album_id + 1
#     query = f"INSERT INTO Album (AlbumID, Title, ArtistID, Genre, ReleaseDate) VALUES ('{album_id}', '{album.title}', '{album.artist_id}', '{album.genre}', '{album.release_date}');"
#     self.cursor.execute(query)
#     self.connection.commit()
#     # print("Album inserted successfully!")
#     if self.cursor.rowcount > 0:
#         return {"success": True}
#     else:
#         return {"success": False}
#     # return db.post_data("Album", data)


# @app.post("/track", tags=["Track"])
# def insert_track(self, track: Track):
#     # check for artist and check for album
#     artist_exists = conn.fetch_by_id("Artist", "ArtistID", track.artist_id)
#     album_exists = conn.fetch_by_id("Album", "AlbumID", track.album_id)
#     max_track_id = self.get_max_id("Track", "TrackID")
#     track_id = max_track_id + 1

#     query = f"INSERT INTO Track (TrackID, Title, ArtistID, AlbumID, Duration, ReleaseDate) VALUES ('{track.title}', '{track_id}', '{track.album_id}', '{track.duration}', '{track.release_date}');"
#     self.cursor.execute(query)
#     self.connection.commit()
#     print("Track inserted successfully!")
#     if self.cursor.rowcount > 0:
#         return {"success": True}
#     else:
#         return {"success": False}


# # @app.post("/artist", tags=["Artist"])
# # def insert_artist(artist: Artist):
# #     max_artist_id = self.get_max_id("Artist", "ArtistID")
# #     artist_id = max_artist_id + 1
# #     query = f"INSERT INTO Artist (ArtistID, Name, Genre) VALUES ('{artist_id}', '{artist.name}', '{artist.genre}');"
# #     print(query)
# #     self.cursor.execute(query)
# #     self.connection.commit()
# #     if self.cursor.rowcount > 0:
# #         return {"success": True}
# #     else:
# #         return {"success": False}


# @app.post("/artist", tags=["Artist"])
# def insert_artist(artist: Artist):

#     max_artist_id = db.get_max_id("Artist", "ArtistID")
#     artist_id = max_artist_id + 1

#     artist = {
#         "ArtistID": artist_id,
#         "Name": artist.name,
#         "Genre": artist.genre,
#     }

#     _, success = db.post_data("Artist", artist)

#     return {"success": success}


# @app.post("/playlist", tags=["Playlist"])
# def insert_playlist(playlist: Playlist):
#     max_playlist_id = db.get_max_id("Playlist", "PlaylistID")
#     play_list_id = max_playlist_id + 1
#     query = f"INSERT INTO Playlist (PlaylistID ,UserID, Title, Genre) VALUES ('{play_list_id}', '{playlist.artist_id}', '{playlist.name}', '{playlist.genre}');"
