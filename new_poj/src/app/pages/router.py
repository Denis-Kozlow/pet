from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/delivery",
    tags=["home"],
)


tempplates = Jinja2Templates(directory="src/app/templates")


@router.get("/home")
def get_search_template(request: Request):
    return tempplates.TemplateResponse("home.html", {"request": request})


@router.get("/registration")
def get_search_template(request: Request):
    return tempplates.TemplateResponse("registration.html", {"request": request})


@router.get("/all")
def all_package(request: Request):
    return tempplates.TemplateResponse("getall.html", {"request": request})


@router.get("/id")
def all_package(request: Request):
    return tempplates.TemplateResponse("id.html", {"request": request})
