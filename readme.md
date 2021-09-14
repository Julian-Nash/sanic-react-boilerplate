# Sanic React boilerplate

Sanic, React & React Router, built with Webpack & Babel

Installation:

```shell
pip install -e .
```

Install JS dependencies:

```shell
npm install
```

Building the react app

```shell
npm run build
```

> Note: This will start a watcher configured in `webpack.config.js`

Starting the Sanic web app:

```shell
python run.py
```

The application will start on http://localhost:8000

Sanic app options:

```shell
$ python run.py --help
usage: Sanic application boilerplate [-h] [--host HOST] [--port PORT] [--debug DEBUG] [--access-log ACCESS_LOG] [--auto-reload AUTO_RELOAD] [--workers WORKERS]
                                     [--config {prod,dev,test}]

optional arguments:
  -h, --help            show this help message and exit
  --host HOST           Application host (default: 0.0.0.0)
  --port PORT           Application port (default: 8000)
  --debug DEBUG         Enable debug mode (default: False)
  --access-log ACCESS_LOG
                        Enable access log (default: False)
  --auto-reload AUTO_RELOAD
                        Enable auto reload (default: False)
  --workers WORKERS     N. workers (default: 12)
  --config {prod,dev,test}
                        Configuration name (default: prod)
```

__Sanic:__
- [Sanic Docs](https://sanicframework.org/)
- [Sanic GitHub](https://github.com/sanic-org/sanic)

