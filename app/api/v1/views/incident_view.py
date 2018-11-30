from flask import request, json, Blueprint
from flask_restful import Resource, Api, reqparse

from app.api.v1.models.incidents import IncidentModel

incident_api = Blueprint('incident_api',__name__)


class IncidentApi(Resource):
    """ Shows a single incident and lets you delete it"""
    def get(self,id):
        pass

    def put(self,id):
        pass
    
    def delete(self,id):
        pass

class IncidentApiList(Resource):
    """Shows a list of all incidents, and lets you post"""
    def __init__(self):
        self.incident = IncidentModel()

    def get(self):
        incidents = self.incident.get_all_incidents()
        if incidents:
            return make_response(jsonify(
                {
                    'status': 200,
                    'data': incidents
                }
            ))

    def post(self):
        pass

