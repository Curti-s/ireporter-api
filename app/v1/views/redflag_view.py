import uuid, datetime, requests
from flask import request,jsonify, make_response, Blueprint, abort, json
from rapidjson import loads
from flask_restful import Resource
from app.v1.models.red_flag_model import RedFlagModel

red_flag_api = Blueprint('red_flag_api',__name__)


@red_flag_api.route('/',methods=['GET'])
@red_flag_api.route('/redflag/',methods=['GET'])
def get_all():
    """"Get all red_flags"""
    all_flags = RedFlagModel().get_red_flags()
    response_obj = {
        'status': 200,
        'data': [all_flags]
    }
    return make_response(jsonify(response_obj),200)


@red_flag_api.route('/',methods=['POST','GET'])
@red_flag_api.route('/redflag/',methods=['GET', 'POST'])
def redflags():
    if request.method == 'POST':
        new_red_flag = RedFlagModel()
        json_data = request.get_json(force=True)
        payload = dict(
            created_by = json_data['created_by'],
            record_type = json_data['record_type'],
            location = json_data['location'],
            status = json_data['status'],
            image = json_data['image'],
            video = json_data['video'],
            comment = json_data['comment'],
        )
        new_red_flag.save(payload)
        response_obj = {
                'status': 201,
                'message': "Created red-flag record"
        }
        return make_response(jsonify(response_obj),201)

    else:
        # GET
        all_flags = new_red_flag.get_all()
        response_obj = {
            'status': 200,
            'data': all_flags
        }
        return make_response(jsonify(response_obj),200)


@red_flag_api.route('/redflag/<int:id>', methods=['GET','PUT','DELETE'])
def alter_redflag(id):
    if request.method == 'GET':
        new_red_flag = RedFlagModel()
        flag = new_red_flag.get_red_flag_by_id(id)
        response_obj = {
            'status': 200,
            'data': flag
        }
        return make_response(jsonify(response_obj),200)

    if request.method == 'PUT':
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

    if request.method == 'DELETE':
        new_red_flag = RedFlagModel()
        new_red_flag.delete(id)
        response_obj = {
            'status': 204,
            'message': 'Records object has been deleted'
        }
        return make_response(jsonify(response_obj),200)