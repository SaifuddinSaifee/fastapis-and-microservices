
music_db = {
    "artists": {
        "1": {"name": "Radiohead", "genre": "Alternative"},
        "2": {"name": "ACDC", "genre": "Rock"},
        "3": {"name": "Queen", "genre": "Rock"},
        "4": {"name": "Bob Dylan", "genre": "Folk"},
        "5": {"name": "The Clash", "genre": "Punk"},
        "6": {"name": "Muse", "genre": "Rock"},
        "7": {"name": "Fleetwood Mac", "genre": "Rock"},
        "8": {"name": "The Doors", "genre": "Rock"},
        "9": {"name": "The Rolling Stones", "genre": "Rock"},
        "10": {"name": "Nirvana", "genre": "Grunge"}
    },
    "albums": {
        "1": {"artist_id": "1", "name": "OK Computer", "year": 1997, "genre": "Alternative"},
        "2": {"artist_id": "2", "name": "Love Rockets", "year": 1978, "genre": "Rock"},
        "3": {"artist_id": "2", "name": "Highway to Hell", "year": 1979, "genre": "Rock"},
        "4": {"artist_id": "3", "name": "A Night at the Opera", "year": 1975, "genre": "Rock"},
        "5": {"artist_id": "3", "name": "A Day at the Races", "year": 1976, "genre": "Rock"},
        "6": {"artist_id": "3", "name": "Sheer Heart Attack", "year": 1974, "genre": "Rock"},
        "7": {"artist_id": "4", "name": "Bob Dylan's Greatest Hits", "year": 1963, "genre": "Folk"},
        "8": {"artist_id": "4", "name": "The Times They Are a-Changin'", "year": 1970, "genre": "Folk"},
        "9": {"artist_id": "5", "name": "The Clash", "year": 1977, "genre": "Punk"},
        "10": {"artist_id": "6", "name": "Absolution", "year": 2001, "genre": "Rock"},
        "11": {"artist_id": "6", "name": "Black Holes and Revelations", "year": 2006, "genre": "Rock"},
        "12": {"artist_id": "7", "name": "Rumours", "year": 1977, "genre": "Rock"},
        "13": {"artist_id": "7", "name": "Their Greatest Hits", "year": 1970, "genre": "Rock"},
        "14": {"artist_id": "8", "name": "The Doors' Greatest Hits", "year": 1967, "genre": "Rock"},
        "15": {"artist_id": "9", "name": "Exile on Main Street", "year": 1972, "genre": "Rock"},
        "16": {"artist_id": "9", "name": "Goats Head Soup", "year": 1993, "genre": "Rock"},
        "17": {"artist_id": "10", "name": "Nevermind", "year": 1991, "genre": "Grunge"}
    },
    "tracks": {
        "1": {"album_id": "1", "name": "Burn", "duration": "4:09", "genre": "Alternative"},
        "2": {"album_id": "1", "name": "Creep", "duration": "4:24", "genre": "Alternative"},
        "3": {"album_id": "2", "name": "I'm Easy", "duration": "2:52", "genre": "Rock"},
        "4": {"album_id": "2", "name": "Let's Stick Together", "duration": "5:09", "genre": "Rock"},
        "5": {"album_id": "3", "name": "Another One Bites the Dust", "duration": "4:47", "genre": "Rock"},
        "6": {"album_id": "3", "name": "You're My Best Friend", "duration": "4:38", "genre": "Rock"},
        "7": {"album_id": "4", "name": "Blowin' in the Wind", "duration": "2:57", "genre": "Folk"},
        "8": {"album_id": "4", "name": "The Times They Are A-Changin'", "duration": "4:48", "genre": "Folk"},
        "9": {"album_id": "5", "name": "London Calling", "duration": "5:08", "genre": "Punk"},
        "10": {"album_id": "5", "name": "Straight to Hell", "duration": "2:39", "genre": "Punk"},
        "11": {"album_id": "6", "name": "Universal Monsters", "duration": "3:49", "genre": "Rock"},
        "12": {"album_id": "6", "name": "Planet of Numbers", "duration": "4:59", "genre": "Rock"},
        "13": {"album_id": "6", "name": "Supermassive Black Hole", "duration": "7:11", "genre": "Rock"},
        "14": {"album_id": "7", "name": "Little Red Rooster", "duration": "5:00", "genre": "Rock"},
        "15": {"album_id": "7", "name": "Rhiannon", "duration": "5:11", "genre": "Rock"},
        "16": {"album_id": "8", "name": "The Soundboard Demos", "duration": "1:12", "genre": "Rock"},
        "17": {"album_id": "8", "name": "The Last Temptation", "duration": "5:03", "genre": "Rock"},
        "18": {"album_id": "9", "name": "Sweet Emotion", "duration": "3:01", "genre": "Rock"},
        "19": {"album_id": "9", "name": "Moonage Daydream", "duration": "5:00", "genre": "Rock"},
        "20": {"album_id": "10", "name": "Smells Like Teen Spirit", "duration": "4:32", "genre": "Grunge"},
        "21": {"album_id": "10", "name": "Spellcheck", "duration": "2:27", "genre": "Grunge"}
    }
}


def get_artists_by_genre(genre: str) -> list[dict]:
    """
    Get information of all artists that play the specified genre.

    Args:
        genre (str): The genre of the artists.

    Returns:
        list[dict]: A list of dictionaries containing information of artists
                    that play the specified genre.
    """
    artists = []
    for artist_id, artist in music_db["artists"].items():
        if artist["genre"] == genre:
            artists.append(artist)
    return artists

print(get_artists_by_genre("Rock"))
