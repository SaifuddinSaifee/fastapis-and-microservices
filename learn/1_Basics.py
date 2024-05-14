# This is a fast api comprehensive CRUD tutorial

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}

@app.get("/about/{something}")
async def about(something) -> str:
    return ("1" + something)
