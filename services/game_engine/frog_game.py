from random import choice

from app.config import PROJECT_ROOT
from models.game_model import FrogGameRequest, FrogGameConfig, FrogGameAction, FrogGameResponse, FrogGameObject, ResultType
from services.game_engine import decision_game
from utils import load_config


CONFIG_FILE = PROJECT_ROOT / "data/frog.json"


def main(request: FrogGameRequest) -> FrogGameResponse:
    config: FrogGameConfig = FrogGameConfig.model_validate(load_config.main(CONFIG_FILE))
    oppponent_action: FrogGameAction = generate_action()
    action_config: FrogGameObject = config.objects[request.action]
    result: str = get_result(action_config, oppponent_action)
    decision_game.result = config.results[result]
    return FrogGameResponse(
        your_action=request.action,
        opponent_action=oppponent_action,
        result=result
    )


def get_result(action_config: FrogGameObject, opponent_action: FrogGameAction) -> str:
    if opponent_action == action_config.wins:
        return ResultType.wins
    elif opponent_action == action_config.loses:
        return ResultType.lost
    else:
        return ResultType.draw


def generate_action() -> FrogGameAction:
    return choice(FrogGameAction._member_names_)
