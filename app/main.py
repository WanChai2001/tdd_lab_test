from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/callname/{name}")
def read_name(name: str = None):
    return {"Hello": name}

@app.post("/callname")
def post_name():
    name = "paween"
    return {"Hello": name}

handler = Mangum(app)
