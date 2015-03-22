import unittest
import os
import shutil
import json

from git_text import app
from git_text import models
from git_text.database import Base, engine, session


class TestAPI(unittest.TestCase):
    """ Tests for the git_text API """

    def setUp(self):

        """ Test setup """
        # Configure our app to use the testing database
        app.config.from_object('git_text.config.TestingConfig')
        self.client = app.test_client()

        # Set up the tables in the database
        Base.metadata.create_all(engine)

    def tearDown(self):
        """ Test teardown """
        session.close()
        # Remove the tables and their data from the database
        Base.metadata.drop_all(engine)
    
    def test_app_is_testing(self):
        self.assertTrue(app.config['TESTING'])
        self.assertEqual(app.config['DATABASE_URI'],
            'postgresql://localhost:5432/git_text_test'
        )