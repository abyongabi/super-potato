from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.routers import game_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(game_router.router, prefix="/game", tags=["game"])

