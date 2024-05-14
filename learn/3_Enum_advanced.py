# PyDantic Base Model

from fastapi import FastAPI, HTTPException
from musicdb import music_db
from schema import DefineGenres, DefineArtists

app = FastAPI()

@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}

@app.get("/about/{something}")
async def about(something) -> str:
    return ("1" + something)

@app.get("/music/artists")
async def get_artists() -> list[DefineArtists]:
    return [
        DefineArtists(**artist) for artist in music_db["artists"].values()
    ]

@app.get("/music/artists/{artist_id}")
async def get_artist(artist_id: str) -> DefineArtists:
    if artist_id not in music_db["artists"]:
        raise HTTPException(status_code=404, detail=f"Artist {artist_id} not found")
    artist = music_db["artists"][artist_id]
    return DefineArtists(**artist)

@app.get("/music/artists/genre/{genre}")
async def get_artists_by_genre(genre: DefineGenres) -> list[dict]:
    artists = []
    for artist_id, artist in music_db["artists"].items():
        if artist["genre"] == genre.value:
            artists.append(artist)
    return artists
