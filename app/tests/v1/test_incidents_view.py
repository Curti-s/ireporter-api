import unittest

from app import create_app
from app.api.v1.views import incident_view

class TestIncidentAPi(unittest.TestCase):
    """Test IncidentApi"""

    def setUp(self):
        self.app = create_app('testing')
        self. client = self.app.test_client
        

    def test_get_incidents(self):
        pass