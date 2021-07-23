import os

from dotenv import find_dotenv, load_dotenv


class ConfigEnv:

    params: dict = {}

    def __init__(self) -> None:
        load_dotenv(find_dotenv())

        self.params = {
            "host": os.environ.get("host"),
            "port": os.environ.get("port"),
            "dbname": os.environ.get("dbname"),
            "user": os.environ.get("user"),
            "password": os.environ.get("password"),
        }

        print(f"params : {self.params}")

    def get_params(self) -> dict:
        return self.params
