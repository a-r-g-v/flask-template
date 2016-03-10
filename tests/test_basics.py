import unittest
from flask import current_app, url_for
from app import create_app


class BasicsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test_app_exists(self):
        assert current_app is not None

    def test_app_is_testing(self):
        assert current_app.config['TESTING']

    def test_root_page(self):
        response = self.client.get(url_for('main.index'))
        assert 'poe' in response.data

    def test_404_page(self):
        response = self.client.get('/invalid_page')
        assert 'Not Found' in response.data
        


