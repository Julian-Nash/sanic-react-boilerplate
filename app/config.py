from typing import Type
import enum

from sanic.config import Config


class Configuration(enum.Enum):
    """ Enumeration of configuration names """
    PROD = "prod"
    DEV = "dev"
    TEST = "test"


class BaseConfig(Config):
    """ Shared config class """


class ProdConfig(BaseConfig):
    """ Production config """


class DevConfig(BaseConfig):
    """ Development config """


class TestConfig(BaseConfig):
    """ Testing config """


def get_config(name: str) -> Type[BaseConfig]:
    """ Returns the config class based on the config name, always defaults to the ProdConfig class """
    return {
        Configuration.PROD.value: ProdConfig,
        Configuration.DEV.value: DevConfig,
        Configuration.TEST.value: TestConfig
    }.get(name, ProdConfig)
