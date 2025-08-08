from fastapi import FastAPI, Query
from request import fetch_species_data

app = FastAPI()

@app.get("/hello")
def read_hello():
    return {"message": "hello"}

@app.get("/species")
def get_species(search: str = Query(...)):
    print("I got: " + search)
    return { "data": fetch_species_data(search)}
