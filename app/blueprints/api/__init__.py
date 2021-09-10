from sanic import Blueprint

from .products import ProductsApi

api = Blueprint("api", url_prefix="/api")

api.add_route(ProductsApi.as_view(), "/products", name="products")
