from flask import Flask, jsonify, request
import os
from logging.config import dictConfig

#Flask uses standard Python logging. Flask application are logged with app.logger, which takes the same name as app.name.
dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] [%(process)d] [%(levelname)s] in %(module)s: %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S %z"
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": os.environ.get('LOG_LEVEL').upper(), "handlers": ["wsgi"]},
    }
)



app = Flask(__name__)

app.logger.debug("Starting Myapplication - Version: " + os.environ.get('VERSION'))

#code which would serve in /info to produce the json output
@app.route("/info")
def info():
    app.logger.info("/info accessed from IP: " + request.remote_addr)
    retJson = {
        "service_name" : 'myapplication',
        "version" : os.environ.get('VERSION'),
        "git_commit_sha" : os.environ.get('GIT_COMMIT_SHA'),
        "environment" : {'service_port': os.environ.get('PORT'),
        'log_level': os.environ.get('LOG_LEVEL')}
    }
    return jsonify(retJson)
