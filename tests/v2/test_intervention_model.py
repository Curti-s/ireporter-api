import unittest
import json
import uuid
import datetime

from app import create_app
from app.v2.models.intervention_model import InterventionModel
intervention_list = []

class TestInterventionModel(unittest.TestCase):
    """Test for intervention model"""

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client
        self.intervention_list = intervention_list

    def test_save(self):
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
        new_intervention = InterventionModel()
        saved_data = new_intervention.save(payload)
        self.assertTrue(isinstance(saved_data, list) == True)