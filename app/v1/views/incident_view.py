from flask import request, json, jsonify, Blueprint, make_response
from flask_restful import Resource, Api, reqparse

from app.v1.models.incidents import IncidentModel

incident_api = Blueprint('incident_api',__name__)

class IncidentApi(Resource):
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
            ),200)
        else:
            return make_response(jsonify(
                {
                    'status': 404,
                    'error': 'Not results were returned.'
                }
            ))

    def post(self):
        data = request.get_json()
        try:
            res = json.loads(data.data.decode())
            redflag = res["type"]
            location = res["location"]
            status = res["status"]
            comment = res["comment"]
            result = self.incident.save_incidents(redflag_type,location,status,comment)
            return make_response(jsonify(
                {
                    'status': 201,
                    'data': result
                }
            ), 201)
        except Exception as error:
            return make_response(jsonify(
                {
                    'status': 404,
                    'error': 'Some error occurred'
                }
            ))