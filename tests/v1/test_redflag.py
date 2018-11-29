import unittest
import json

from app import create_app


class TestRedFlag(unittest.TestCase):
    """Test red flag endpoint"""

    def setUp(self):
        self.app = create_app('testing')
        # initialize the test client
        self.client = self.app.test_client
        # Red flag json test data
        self.redflag_data = """{
            "flag": [ 
                {
                    "status":201,
                    "data": "Create red-flag record"
                }
            ]
        }"""
        # bind the app with the current context
        # with self.app.app_context():
        #     #create db
        
    def test_create_a_redflag(self):
        """Test API can create new red flag. POST request"""

        res = self.client().post('/redflag/', data=self.redflag_data)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Create red-flag record', str(res.data))

    def test_get_all_redflag(self):
        """Test API can get all red flags GET request"""

        # create a redflag by making a POST request
        res = self.client().post(
                '/redflag/',
                data=self.redflag_data)
        # test creation of redflag
        self.assertEqual(res.status_code, 201)
        # get all redflags by making a GET request
        res = self.client().get('/redflag/')
        # test
        self.assertEqual(res.status_code,200)
        self.assertIn('Create red-flag record', str(res.data))
    
    def test_get_a_redflag(self):
        """Test API can get a specific red flag using its id GET request"""

        # first create a red flag
        response = self.client().post('/redflag/', data=self.redflag_data)
        # assert that redflag is created
        self.assertEqual(response.status_code, 201)
        # get response data in json format
        results = json.loads(response.data.decode())
        result = self.client().get(
                '/redflag/{}/'.format(results['data'][0]['id']))
        # assert that redflag is returned given its actual id
        self.assertEqual(result.status_code, 200)
 

    # def test_edit_a_redflag(self):
    #     """Test API can edit an existing redflag. PUT request"""

    #     # create a redflag making a POST request
    #     res = self.client().post('/redflag/',data=self.redflag_data)
    #     # test creation of the red flag
    #     self.assertEqual(res.status_code, 201)
    #     # obtain the json
    #     results = json.loads(res.data.decode())
    #     # edit the created redflag by making a PUT request
    #     rv = self.client().put(
    #             '/redflag/{}/'.format(results['data'][0]['id']),
    #             data={
    #                     'message': 'Update red-flag location.'
    #             })
    #     # test if it changed
    #     self.assertEqual(rv.status_code,201)
    #     # test if the edited red flag is actually edited
    #     req = self.client().get(
    #             '/redflag/{}'.format(results['data'][0]['id']))
    #     self.assertIn('Update red-flag location',str(req.data))

    
    def test_delete_a_redflag(self):
        """Test API can delete an existing redflag. DELETE request"""

        # create red flag
        response = self.client().post('/redflag/', data=self.redflag_data)
        results = json.loads(response.data.decode())
        # delete created red flag
        res = self.client().delete('/redflag/{}/'.format(results['data'][0]['id']))
        self.assertEqual(res.status_code, 204)


if __name__ == '__main__':
    unittest.main()