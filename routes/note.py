from fastapi import FastAPI, APIRouter, Request
from config.db import conn
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import starlette.status as status


note = APIRouter()

templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    if request.method == "GET":
        docs = conn.notes.notes.find({})
        newDocs = []
        for doc in docs:
            newDocs.append({
                "id": doc["_id"],
                "title": doc["title"],
                "desc": doc["desc"],
                "important": doc["important"]
            })
        return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})


@note.post("/")
async def add_note(request: Request):
    form = await request.form()
    formdict = dict(form)
    formdict["important"] = True if formdict.get("important") == "on" else False
    note = conn.notes.notes.insert_one(formdict)
    return RedirectResponse('/', status_code=status.HTTP_302_FOUND)
