import unittest
import json
import uuid
import datetime

from app import create_app
from app.v1.models.red_flag_model import RedFlagModel

red_flag_data = []
class TestRedFlagModel(unittest.TestCase):
    """Test red flag endpoint"""

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client
        self.red_flag_data = red_flag_data

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
        new_red_flag = RedFlagModel()
        saved_data = new_red_flag.save(payload)
        self.assertTrue(isinstance(saved_data, list) == True)



if __name__ == '__main__':
    unittest.main()