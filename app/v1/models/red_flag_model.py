import datetime
import uuid

red_flag_data = []
class RedFlagModel(object):
    """Red-flag domain model"""

    def __init__(self,id, created_on, created_by, record_type,
                location, status, image, video, comment):
        # red_flag attributes
        self.id = id
        self.created_on = created_on
        self.created_by = created_by
        self.record_type = record_type
        self.location = location
        self.status = status
        self.image = image
        self.video = video
        self.comment = comment
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
        return self.red_flag_data

    def get_red_flag_by_id(self,id):
        """Get one red-flag by its uuid"""
        for flag in self.red_flag_data:
            if flag['id'] == id:
                return flag
        return "Invalid ID was provided"