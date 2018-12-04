import unittest
import json
import uuid
import datetime

from app import create_app
from app.v1.models.red_flag_model import RedFlagModel


class TestRedFlag(unittest.TestCase):
    """Test red flag endpoint"""

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client
    
    def test_init(self):
        id = uuid.uuid4()
        created_on = datetime.datetime.now()
        new_red_flag = RedFlagModel(id, created_on,created_by='curtis', record_type='red flag', location='0.0236° S, 37.9062° E', status='New red flag',image='',video='', comment='Red flag comment')
        self.assertEqual(new_red_flag.created_by, 'curtis')
        self.assertEqual(new_red_flag.record_type, 'red flag')
        self.assertEqual(new_red_flag.status, 'New red flag')
        self.assertEqual(new_red_flag.comment, 'Red flag comment')

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
        new_red_flag = RedFlagModel(**payload)
        self.assertEqual(new_red_flag.created_by,'curtis')
        self.assertEqual(new_red_flag.record_type,'red flag')
        self.assertEqual(new_red_flag.location,'0.0236° S, 37.9062° E')
        self.assertEqual(new_red_flag.status, 'New red flag')
        self.assertEqual(new_red_flag.comment, 'Red flag comment')

if __name__ == '__main__':
    unittest.main()