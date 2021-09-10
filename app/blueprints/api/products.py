from sanic.response import json

from app.handlers import BaseHTTPView


class ProductsApi(BaseHTTPView):

    async def get(self, request):

        return json([
            {"id": 1, "name": "foo", "price": 1.99},
            {"id": 1, "name": "bar", "price": 5.50}
        ])
