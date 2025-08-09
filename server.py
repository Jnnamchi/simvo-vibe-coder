from fastapi import FastAPI, Query
from request import fetch_species_data
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent

@app.get("/hello")
def read_hello():
    return {"message": "hello"}

@app.get("/species")
def get_species(search: str = Query(...)):
    print("I got: " + search)
    return { "data": fetch_species_data(search)}

@app.get("/", response_class=FileResponse)
def return_site():
    # Serve the HTML file directly
    return FileResponse(BASE_DIR / "templates" / "index.html", media_type="text/html")