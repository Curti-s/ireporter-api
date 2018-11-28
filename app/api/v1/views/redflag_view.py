from flask import request, jsonify, make_response, Blueprint, abort
from flask_restful import Resource, Api, reqparse

parser = reqparse.RequestParser()
parser.add_argument('message', type=str, action='append')

redflag_list = [
    {    
        "status": 201,
        "data": [{
                "id": 0,
                "message": "Created  red-flag record"
        }]
    },
    {    
        "status": 201,
        "data": [{
                "id": 1,
                "message": "Created  red-flag record"
        }]
    }
]

class RedFlags(Resource):
    """Redflags, lists all red flags and lets you create new ones"""
    
    def __init__(self):
        self.db = redflag_list
    
    # create a red flag
    def post(self):
        response = {
                    "status": 201,
                    "data": [
                        {
                            "id": self.db[-1]['data'][0]['id']+1,
                            "message": "Create red-flag record"
                        }
                    ]
            }
        self.db.append(response)
        return make_response(jsonify(response),201) 

    # get all red flags
    def get(self):
        response = self.db
        return make_response(jsonify(response),200) 
    

class RedFlag(Resource):
    """Redflag, shows a single red flag and lets you delete it"""
    
    def __init__(self):
        self.db = redflag_list

    # get a red flag
    def get(self,id):
        response = self.db[id]
        if len(response) < 0:
            abort(404)
        return make_response(jsonify(response),200)

    # # edit a red flag comment / locaion
    # def put(self,id):
    #     json_data = request.get_json()
    #     args = parser.parse_args()
    #     response = self.db[id]
    #     response['data'][0]['message'] = args.message
    #     return make_response(jsonify(response),201)        


    # delete a red flag
    def delete(self,id):
        response = self.db
        del response[id]
        return make_response(jsonify(response),204)  
