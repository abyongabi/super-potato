from models.game_model import FrogGameResult, DecisionGameRequest


result: FrogGameResult | None = None


def main(request: DecisionGameRequest) -> bool:
    if request.action == result.action:
        return True
    return False
