import datetime
import uuid
from marshmallow import Schema, fields, ValidationError, validates

red_flag_data = []

# Model
class RedFlagModel(object):
    """Red-flag domain model"""

    def __init__(self):
        self.red_flag_data = red_flag_data

    def save(self, red_flag_dict):
        """Append the data in the red-flag dictionary into a red-flag list"""
        
        payload = {
            'id': uuid.uuid4(),
            'created_on': datetime.datetime.now(),
            'created_by': red_flag_dict['created_by'],
            'record_type': red_flag_dict['record_type'],
            'location': red_flag_dict['location'],
            'status': red_flag_dict['status'],
            'image': red_flag_dict['image'],
            'video': red_flag_dict['video'],
            'comment': red_flag_dict['comment']
        }
        self.red_flag_data.append(payload)
        return self.red_flag_data

    
    def get_red_flags(self):
        """Return all created red-flags"""
        item = [item for item in self.red_flag_data]
        return item

    def get_red_flag_by_id(self,id):
        """Get one red-flag by its uuid"""
        if not self.red_flag_data:
            return "No redflag record found"
        for index in range(len(self.red_flag_data)):
            if index == id:
                return self.red_flag_data[index]


    def  delete(self, id):
        if self.get_red_flag_by_id(id):
            return self.red_flag_data.pop(id)
        return " Invalid red flag ID"

def null_validator(data):
    if data is None:
        raise ValidationError('Input is required')

# Schema
class RedFlagSchema(Schema):
    """
    Define RedFlagModel schema
    """
    id = fields.UUID(missing=uuid.uuid4)
    created_on = fields.DateTime(default=datetime.datetime.now())
    created_by = fields.String(validate=null_validator)
    record_type = fields.String(required=True, 
                                error_messages = {'required': {'message': 'Record type required',
                                                    'record_type': 'red flag'}})
    location = fields.String(required=True,
                            error_messages={'required': {'message': 'Location type required'}})
    status = fields.String(validate=null_validator)
    image = fields.String(validate=null_validator)
    video = fields.String(validate=null_validator)
    comment = fields.String(validate=null_validator)
    
    