from pathlib import Path
from inspect import getmembers
import os

from sanic import Sanic
from sanic.blueprints import Blueprint

from app.config import get_config
import app.blueprints as blueprints


def create_app(config_name: str) -> Sanic:
    """ Creates and returns an instance of Sanic """

    config_class = get_config(config_name)

    app = Sanic("Sanic boilerplate with Jinja2 template rendering", config=config_class())
    app.static("/static", os.path.join(Path(__file__).parent.resolve(), "static"), name="static")

    # Automatically register blueprints imported to app/blueprints/__init__.py
    for blueprint in getmembers(blueprints, lambda x: isinstance(x, Blueprint)):
        app.blueprint(blueprint[1])

    return app
