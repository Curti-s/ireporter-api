from flask import Flask, Blueprint
from flask_restful import Resource, Api

# local import
from instance.config import app_config
from .api.v1.views import redflag as rf

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.register_blueprint(rf)
    return app
