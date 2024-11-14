from src.app.repository.repository import get_user_token, get_package_by_id, get_my_packages
from src.app.worker.tasks import add_package_broker
from src.app.schemas.schemas import Package, SortPag
from src.app.logic.calc import unique_id
from fastapi import Depends, Request, APIRouter

post_router = APIRouter(
    prefix="/registrations",
    tags=["registration"],
)

get_router = APIRouter(
    prefix="/package",
    tags=["package"]
)


@post_router.get("/registration")
async def run_task(request: Request, package: Package = Depends()):
    token = get_user_token(request)
    data = package.model_dump()
    data["user_token"] = token
    id = unique_id()
    data["package_id"] = id
    add_package_broker.delay(data)
    return id


@get_router.get("/all")
async def get_my_package(request: Request, sort: SortPag = Depends()):
    res = await get_my_packages(request, sort)
    return res


@get_router.get("/id")
async def get_package(id_package: str):
    res = await get_package_by_id(id_package)
    return res
