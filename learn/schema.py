from enum import Enum
from pydantic import BaseModel

class DefineArtists(BaseModel):
    name: str
    genre: str



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