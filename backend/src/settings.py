import os
from configparser import ConfigParser
from functools import cache

CONFIG_FILE_PATH_FOR_LOCAL = "config/application_conf.ini"
CONFIG_FILE_PATH_FOR_DOCKER = "config/docker_application_conf.ini"


@cache
class AppSettings:
    def __init__(self):
        """
        This class is used to load the settings from the config file, either local or docker.
        """
        self.settings = None
        self.setup()
        self.API_PORT = self.settings.get("app", "api_port")

        self.DATABASE_HOST = self.settings.get("database", "host")
        self.DATABASE_PORT = self.settings.get("database", "port")
        self.DATABASE_USER = self.settings.get("database", "user")
        self.DATABASE_PASSWORD = self.settings.get("database", "password")
        self.DATABASE_NAME = self.settings.get("database", "dbname")
        self.DATABASE_POOL_SIZE = self.settings.get("database", "pool_size")
        self.DATABASE_URL = f"postgresql://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"
        self.DATABASE_URL_ASYNC = f"postgresql+asyncpg://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"

    def setup(self):
        config_file_to_use = CONFIG_FILE_PATH_FOR_LOCAL
        is_running_in_docker = os.getenv("WITH_DOCKER")
        print(is_running_in_docker)

        if is_running_in_docker:
            print(f"Using docker config file {CONFIG_FILE_PATH_FOR_DOCKER}")
            config_file_to_use = CONFIG_FILE_PATH_FOR_DOCKER
        else:
            print(f"Using local config file {CONFIG_FILE_PATH_FOR_LOCAL}")

        self.settings = ConfigParser()
        self.settings.read(config_file_to_use)


APP_SETTINGS = AppSettings()
