import datetime
import uuid

intervention_list = []
class InterventionModel(object):
    """Intervention record model"""

    def __init__(self):
        self.intervention_list = intervention_list

    def save(self, intervention_dict):
        """Append an intervention record dict into a list"""

        payload = {
                    'id': uuid.uuid4(),
                    'created_on': datetime.datetime.now(),
                    'created_by': 'curtis',
                    'record_type': 'red flag',
                    'location': '0.0236° S, 37.9062° E',
                    'status': 'New red flag',
                    'image': '',
                    'video': '',
                    'comment': 'Red flag comment'
                }
        self.intervention_list.append(payload)
        return self.intervention_list
    
    def get_interventions(self):
        record = [record for record in self.intervention_list]
        return record
    
    def get_intervention_by_id(self, id):
        for index in ramge(len(self.intervention_list)):
            if index == id:
                return self.intervention_list[index]

    def delete(self, id):
        if self.get_intervention_by_id(id):
            return self.intervention_list.pop(id)
        else:
            return "Invalid intervention record id"