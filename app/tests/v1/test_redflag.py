import os, json

from ...app import create_app

class TestRedFlag():
    """Test red flag endpoint"""

    def __init__(self):
        self.app = create_app('testing')
        self.client = self.app.test_client


    def test_create_a_redflag():
        pass

    def test_get_a_redflag():
        pass
    
    def test_get_all_redflags():
        pass

    def test_edit_a_redflag():
        pass
    
    def test_delete_a_redflag():
        pass