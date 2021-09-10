from sanic import Blueprint

from .utctime import utctime

ws = Blueprint("ws", url_prefix="/ws")

ws.add_websocket_route(utctime, "/utctime", name="utctime")
