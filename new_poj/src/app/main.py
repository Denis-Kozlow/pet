from fastapi import FastAPI
from src.app.config.config import settings
from src.app.repository.orm import StartORM
from contextlib import asynccontextmanager
from starlette.middleware.sessions import SessionMiddleware
from src.app.pages.router import router as router_pages
from src.app.router.router import post_router, get_router
from fastapi.staticfiles import StaticFiles


@asynccontextmanager
async def lifespan(app: FastAPI):
    await StartORM.create_tables()
    await StartORM.insert_type_table()
    yield


app = FastAPI(title="Delivery", lifespan=lifespan)
app.mount("/src/app/static",
          StaticFiles(directory="src/app/static"), name="static")

app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)
app.include_router(router_pages)
app.include_router(post_router)
app.include_router(get_router)
