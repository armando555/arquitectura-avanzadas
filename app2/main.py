from fastapi import FastAPI, Request
from routers import renting_router
from database.engine import engine, SessionLocal
import config
from models.base import init
from sqladmin import Admin
from views import *
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import requests
import os
import json
from repository import renting_repository



HOST_BICYCLES = os.getenv('HOST_BICYCLES')


app = FastAPI(title=config.title)


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/map", response_class=HTMLResponse)
async def show_map(request: Request):
    if HOST_BICYCLES:
        host = HOST_BICYCLES
    else:
        host = "http://localhost:8001"
    db = SessionLocal()
    rentings = renting_repository.get_all(db)
    bicycles = []
    for renting in rentings:
        bicycle_id = renting.bicycle_id
        bicycle = requests.get(host+"/bicycles/"+str(bicycle_id))
        bicycle = bicycle.json()
        #print(bicycle)
        bicycles.append(bicycle)
    markers2 = []
    names = []
    for bicycle in bicycles:
        #print(bicycle["name"])
        marker = [bicycle["id"], bicycle["latitude"], bicycle["longitude"]]
        #print(marker)
        markers2.append(marker)
        names.append([bicycle["id"],bicycle["name"]])
        print(names)
    return templates.TemplateResponse("map.html", {"request": request, "markers": markers2, "names":names})

admin = Admin(app, engine)

admin.add_view(RentingAdmin)

app.include_router(renting_router.router)


#Initialize Data Model
init()

