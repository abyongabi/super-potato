from functools import lru_cache
import json


@lru_cache
def main(config_file: str) -> dict:
    with open(config_file, "r") as file:
        config: dict = json.load(file)
    return config
