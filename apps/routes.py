from fastapi import APIRouter, Request, Form, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from passlib.context import CryptContext
from utils.variables import USER_INFO

router = APIRouter()
templates = Jinja2Templates(directory="templates")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@router.get("/about")
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@router.get("/personal")
def personal(request: Request):
    return templates.TemplateResponse("personal.html", {"request": request, "user": USER_INFO})

@router.get("/login")
def login_get(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "error": None})

@router.post("/login")
def login_post(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == USER_INFO["username"] and password == USER_INFO["password"]:
        response = RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
        return response
    return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})

@router.get("/skills")
def skills(request: Request):
    return templates.TemplateResponse("skills.html", {"request": request})

@router.get("/projects")
def projects(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request})

@router.get("/contact")
def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})
