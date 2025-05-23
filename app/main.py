from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.routers import auth_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(auth_router.router, prefix="/auth", tags=["auth"])

