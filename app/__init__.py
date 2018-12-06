from flask import Flask, Blueprint
from flask_restful import Resource, Api

# local import
from instance.config import app_config
from .v1.views.redflag_view import red_flag_api
from .v2.views.user_view import user

def create_app(config_name):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SECRET_KEY'] = '937429a926a654fdd93e98cba5f45108'
    app.register_blueprint(red_flag_api)
    app.register_blueprint(user)
    return app




