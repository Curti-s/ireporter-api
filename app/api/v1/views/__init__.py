from flask import Blueprint
from flask_restful import Resource, Api

from .redflag_view import RedFlags, RedFlag

redflag = Blueprint('redflag',__name__)
api = Api(redflag)

api.add_resource(RedFlags,'/redflag/')
api.add_resource(RedFlag, '/redflag/<int:id>/')