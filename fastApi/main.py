from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")
def read_html_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/readme")
async def readme():
    return FileResponse("./README.md")

@app.get("/test", response_class=HTMLResponse)
async def test():
    html = read_html_file("base.html")
    return html