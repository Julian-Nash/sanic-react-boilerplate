from app.handlers import BaseHTTPView


class IndexView(BaseHTTPView):

    async def get(self, request, path: str):
        return self.render_template("index.html", request=request)
