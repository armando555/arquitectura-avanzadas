from fastapi import FastAPI, Request
from routers import renting_router
from database.engine import engine
import config
from models.base import init
from sqladmin import Admin
from views import *
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse



app = FastAPI(title=config.title)


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/map", response_class=HTMLResponse)
async def show_map(request: Request):
    return templates.TemplateResponse("map.html", {"request": request, "id": "data"})

admin = Admin(app, engine)

admin.add_view(RentingAdmin)

app.include_router(renting_router.router)


#Initialize Data Model
init()

