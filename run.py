import multiprocessing
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

from app import create_app
from app.config import Configuration


if __name__ == "__main__":

    parser = ArgumentParser("Sanic application boilerplate", formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Application host")
    parser.add_argument("--port", type=int, default=8000, help="Application port")
    parser.add_argument("--debug", type=bool, default=False, help="Enable debug mode")
    parser.add_argument("--access-log", type=bool, dest="access_log", default=False, help="Enable access log")
    parser.add_argument("--auto-reload", type=bool, dest="auto_reload", default=False, help="Enable auto reload")
    parser.add_argument("--workers", type=int, default=multiprocessing.cpu_count(), help="N. workers")
    parser.add_argument("--config", type=str, default=Configuration.PROD.value, choices=[i.value for i in Configuration],
                        help="Configuration name")
    args = parser.parse_args()

    app = create_app(args.config)

    app.run(
        host=args.host,
        port=args.port,
        debug=args.debug,
        access_log=args.access_log,
        auto_reload=args.auto_reload,
        workers=args.workers
    )
