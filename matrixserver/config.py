import json


class Config:
    def __init__(
        self,
        matrix_action_schema,
        matrix_response_schema
    ):
        self.matrix_action_schema = matrix_action_schema
        self.matrix_response_schema = matrix_response_schema

    @staticmethod
    def parse(config_file):
        with open(config_file, "r") as f:
            config = json.load(f)

        with open(config["matrix_action_schema_file"], "r") as f:
            matrix_action_schema = json.load(f)

        with open(config["matrix_response_schema_file"], "r") as f:
            matrix_response_schema = json.load(f)

        return Config(
            matrix_action_schema,
            matrix_response_schema
        )
