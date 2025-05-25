from pydantic import BaseModel
from enum import StrEnum
from typing import Literal


class FrogGameAction(StrEnum):
    scissors = "scissors"
    paper = "paper"
    stone = "stone"


class ResultType(StrEnum):
    wins = "wins"
    lost = "lost"
    draw = "draw"


class FrogGameObject(BaseModel):
    action: FrogGameAction
    wins: str
    loses: str


class FrogGameResult(BaseModel):
    action: ResultType
    result: str | list


class FrogGameConfig(BaseModel):
    objects: dict[str, FrogGameObject]
    results: dict[str, FrogGameResult]



class FrogGameRequest(BaseModel):
    action: Literal[FrogGameAction.scissors, FrogGameAction.paper, FrogGameAction.stone]


class FrogGameResponse(BaseModel):
    your_action: FrogGameAction
    opponent_action: FrogGameAction
    result: str


class DecisionGameRequest(BaseModel):
    action: Literal[ResultType.wins, ResultType.lost, ResultType.draw]
