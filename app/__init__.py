from flask import Flask, Blueprint
from flask_restful import Resource, Api

# local import
from instance.config import app_config
from .v1.views import redflag as rf
from .v1.views import incident_api
from .v1.views.redflag_view import RedFlags, RedFlag
from .v1.views.incident_view import IncidentApi

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.register_blueprint(rf)
    app.register_blueprint(incident_api)
    api = Api(app)
    api.add_resource(RedFlags,'/','/redflag/')
    api.add_resource(RedFlag, '/redflag/<int:id>/')
    api.add_resource(IncidentApi,'/incident-api/')
    return app


