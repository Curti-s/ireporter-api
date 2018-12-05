import unittest
import datetime
import uuid
from flask import request, json
from rapidjson import dump, dumps, loads, load, DM_ISO8601, UM_CANONICAL

from app import create_app
from app.v1.models.red_flag_model import RedFlagModel 

class TestRedFlagView(unittest.TestCase):
    """Test RedFlagView api"""

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client
        self.red_flag_data = dict(
                                id = uuid.uuid4(),
                                created_on = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
                                created_by = "curtis",
                                record_type = "red flag",
                                location = '0.0236° S, 37.9062° E',
                                status = "New red flag",
                                image = " ",
                                video = " ",
                                comment = "Red flag comment"
                            )

    def test_create(self):
        with self.client():
            response = self.client().post('/', 
                    data=dumps(self.red_flag_data,datetime_mode=DM_ISO8601,
                    uuid_mode=UM_CANONICAL), content_type="application/json")
            response_data = loads(response.data.decode())
            self.assertEqual(response.status_code,201)
            self.assertEqual(response.content_type,'application/json')
            self.assertEqual(response_data['status'],201)
            self.assertEqual(response_data['message'], 'Created red-flag record')
            self.assertEqual(isinstance(response_data['message'],str),True)

    def test_get_all(self):
        with self.client():
            response = self.client().post('/', 
                    data=dumps(self.red_flag_data,datetime_mode=DM_ISO8601,
                    uuid_mode=UM_CANONICAL), content_type="application/json")
            response_data = loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            request_data = self.client().get('/')
            self.assertEqual(request_data.status_code,200)
   
    def test_get_one(self):
        with self.client():
            response = self.client().post('/', 
                    data=dumps(self.red_flag_data,datetime_mode=DM_ISO8601,
                    uuid_mode=UM_CANONICAL), content_type="application/json")
            json_result = loads(response.data.decode('utf-8').replace("'","\""))
            self.assertEqual(response.status_code,201)
    

if __name__ == '__main__':
    unittest.main()