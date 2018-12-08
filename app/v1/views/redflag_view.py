import uuid, datetime, requests
from flask import request,jsonify, make_response, Blueprint, abort, json
from rapidjson import loads
from marshmallow import ValidationError, pprint
from app.v1.models.red_flag_model import RedFlagModel, RedFlagSchema

red_flag_api = Blueprint('red_flag_api',__name__)

red_flag_schema = RedFlagSchema()


@red_flag_api.route('/',methods=['POST'])
@red_flag_api.route('/redflag/',methods=['POST'])
def new_redflag():
    json_data = request.json
    try:
        des_data = red_flag_schema.load(json_data)
    except ValidationError as err:
        return jsonify({
                'status': 422,
                'error': err.messages
        }), 422
    new_red_flag = RedFlagModel()
    new_red_flag.save(des_data.data)
    response_obj = {
            'status': 201,
            'message': "Created red-flag record"
    }
    return make_response(jsonify(response_obj),201)

@red_flag_api.route('/',methods=['GET'])
@red_flag_api.route('/redflag/',methods=['GET'])
def get_all():
    try:
        all_flags = RedFlagModel().get_red_flags()
        response_obj = {
            'status': 200,
            'data': all_flags
        }
        return make_response(jsonify(response_obj),200)
    except Exception as e:
        response_obj = {
            'status': 404,
            'data': 'Record not found'
        }
        return make_response(jsonify(response_obj),404)

@red_flag_api.route('/redflag/<int:id>', methods=['GET','PUT','DELETE'])
def alter_redflag(id):
    if request.method == 'GET':
        try:

            new_red_flag = RedFlagModel()
            flag = new_red_flag.get_red_flag_by_id(id)
            response_obj = {
                'status': 200,
                'data': flag
            }
            return make_response(jsonify(response_obj),200)
        except Exception as e:
            response_obj = {
                'status': 404,
                'message': 'Record not found'
            }
            return make_response(jsonify(response_obj),404)

    if request.method == 'PUT':
        try:
            new_red_flag = RedFlagModel()
            # edit the location
            request_data = request.get_json(force=True)
            flag = new_red_flag.get_red_flag_by_id(id)
            flag['location'] = request_data['location']
            response_obj = {
                'status': 202,
                'message': "Updated red-flag record location"
            }
            return make_response(jsonify(response_obj),200)
        except Exception as e:
            response_obj = {
                'status': 404,
                'message': 'Record not found'
            }
            return make_response(jsonify(response_obj),204)

    if request.method == 'DELETE':
        try:
            new_red_flag = RedFlagModel()
            new_red_flag.delete(id)
            response_obj = {
                'status': 204,
                'message': 'Records object has been deleted'
            }
            return make_response(jsonify(response_obj),200)
        except Exception as e:
            response_obj = {
                'status': 404,
                'message': 'Record not found'
            }
            return make_response(jsonify(response_obj),204)