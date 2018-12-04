from flask import request, jsonify, make_response, Blueprint, abort
from flask_restful import Resource
from app.v1.models.red_flag_model import RedFlagModel

red_flag_api = Blueprint('red_flag_api',__name__)


@red_flag_api.route('/',methods=['POST'])
def create():
    """Create new red_flag"""
    pass


@red_flag_api.route('/',methods=['GET'])
def get_all():
    """"Get all red_flags"""
    pass

@red_flag_api.route('/<int:id>',methods=['GET'])
def get_one(id):
    """Get one red_flag"""
    pass

@red_flag_api.route('/<int:id>', methods=['PUT'])
def update(id):
    """Update a particular red_flag"""
    pass

@red_flag_api.route('/<int:id>', methods=['DELETE'])
def delete(id):
    """Delete a particular red_flag"""
    pass

