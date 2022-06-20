import logging
import os
from logging.config import dictConfig

from flask import Flask
from flask_restx import Api
from flask_cors import CORS

from main.controller.echo import echo_ns

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': os.environ.get('QC_LOG_LEVEL', 'INFO'),
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
CORS(app)

api = Api(title='QC API', description='API Layer for the Mobile')
api.init_app(app)
api.add_namespace(echo_ns, path="/api")

if __name__ == '__main__':
    logging.info('API service starting ...')
    app.run(host=os.getenv('API_IP_ADDRESS'), debug=False)
