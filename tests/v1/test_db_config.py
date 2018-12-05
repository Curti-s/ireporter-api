import unittest

from app import create_app

class TestDevelopmentConfig(unittest.TestCase):
    """Test if configuration is development"""
    def test_app_is_development(self):
        app = create_app('development')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertTrue(
                        app.config['DATABASE_URL'] == 'postgresql:///ireporter_api' )

class TestTestingConfig(unittest.TestCase):
    """Test if configuration is testing"""
    
    def test_app_is_testing(self):
        app = create_app('testing')
        self.assertTrue(app.config['TESTING'] is True)
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertTrue(
                        app.config['DATABASE_URL'] == 'postgresql:///ireporter_api_test')

class TestProductionConfig(unittest.TestCase):
    """Test if configuration is development"""

    def test_app_is_production(self):
        app = create_app('production')
        self.assertTrue(app.config['TESTING'] is False)
        self.assertTrue(app.config['DEBUG'] is False)

if __name__ == '__main__':
    unittest.main()
