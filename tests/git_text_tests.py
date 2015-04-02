import unittest

from git_text import app


class TestAPI(unittest.TestCase):
    """ Tests for the git_text API """

    def setUp(self):
        """ Test setup """

        # Configure our app to use the testing database
        app.config.from_object('git_text.config.TestingConfig')
        self.client = app.test_client()

    def tearDown(self):
        """ Test teardown """
        pass

    def test_app_is_testing(self):
        self.assertTrue(app.config['TESTING'])

    def test_main_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, "hi!")
        self.assertEqual(response.mimetype, "text/html")
