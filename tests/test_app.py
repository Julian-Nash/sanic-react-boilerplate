import json

import pytest
from sanic_testing import TestManager

from app import create_app
from app.config import Configuration


@pytest.fixture
def app():
    sanic_app = create_app(Configuration.TEST.value)
    TestManager(sanic_app)
    return sanic_app


@pytest.mark.asyncio
async def test_index(app):
    request, response = await app.asgi_client.get("/")
    assert response.status == 200


@pytest.mark.asyncio
async def test_products_api(app):
    request, response = await app.asgi_client.get("/api/products")
    expected = [
        {"id": 1, "name": "foo", "price": 1.99},
        {"id": 1, "name": "bar", "price": 5.50}
    ]
    assert response.status == 200
    assert json.loads(response.body) == expected
