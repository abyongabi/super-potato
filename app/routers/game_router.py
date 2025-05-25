from fastapi import APIRouter, Depends
from typing import Annotated

from services.game_engine import frog_game, decision_game
from models.game_model import FrogGameRequest, FrogGameResponse, DecisionGameRequest


router: APIRouter = APIRouter()


@router.get("/frog_game")
async def run_frog_game(request: Annotated[FrogGameRequest, Depends()]) -> FrogGameResponse:
    return frog_game.main(request)


@router.get("/decision_game")
async def run_decision_game(request: Annotated[DecisionGameRequest, Depends()]) -> bool:
    return decision_game.main(request)
