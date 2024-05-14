# Enum

from fastapi import FastAPI
from musicdb import music_db
from enum import Enum

app = FastAPI()

# Defining Enums
class DefineArtists(Enum):
    Radiohead = "Radiohead"
    ACDC = "ACDC"
    Queen = "Queen"
    Bob_Dylan = "Bob Dylan"
    The_Clash = "The Clash"
    Muse = "Muse"
    Fleetwood_Mac = "Fleetwood Mac"
    The_Doors = "The Doors"
    The_Rolling_Stones = "The Rolling Stones"
    Nirvana  = "Nirvana"

class DefineGenres(Enum):
    genre1 = "Rock"
    genre2 = "Pop"
    genre3 = "Jazz"
    genre4 = "Classic"
    genre5 = "Electronic"
    genre6 = "Alternative"
    genre7 = "Punk"
    genre8 = "Rap"
    genre9 = "Classical"
    genre10 = "Folk"
    

@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}

@app.get("/about/{something}")
async def about(something) -> str:
    return ("1" + something)

@app.get("/music/artists")
async def get_artists() -> dict[str, dict]:
    return music_db["artists"]

@app.get("/music/artists/{artist_id}")
async def get_artist(artist_id: str):
    return (music_db["artists"][artist_id])

@app.get("/music/artists/genre/{genre}")
async def get_artists_by_genre(genre: DefineGenres) -> list[dict]:
    artists = []
    for artist_id, artist in music_db["artists"].items():
        if artist["genre"] == genre.value:
            artists.append(artist)
    return artists
