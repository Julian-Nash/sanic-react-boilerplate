from sanic.views import HTTPMethodView
from sanic.request import Request
from sanic.response import html
from jinja2 import Environment, PackageLoader, select_autoescape


env = Environment(loader=PackageLoader("app", "templates"), autoescape=select_autoescape(["html", "xml"]))


class BaseHTTPView(HTTPMethodView):
    """ Base handler for all HTTP views """

    def render_template(self, template: str, request: Request, **kwargs) -> html:
        """ Render an HTML template """
        template = env.get_template(template)
        rendered = template.render(request=request, app=request.app, url_for=request.app.url_for, **kwargs)
        return html(rendered)
