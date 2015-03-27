import unittest
import os
import shutil
import json

from git_text import app
from git_text import models
from git_text.database import Base, engine, session

from datetime import datetime

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
            'postgresql://localhost/git_text_test'
        )

    def test_get_empty_commits(self):
    	""" Getting commits from an empty database """
    	response = self.client.get("/commits",
    		headers=[("Accept", "application/json")])

    	self.assertEqual(response.status_code, 200)
    	self.assertEqual(response.mimetype, "application/json")

    	data = json.loads(response.data)
    	self.assertEqual(data, [])

    def test_get_commits(self):
    	""" Getting commits from a populated database """
    	commitA = models.Commit()
    	commitB = models.Commit()

    	session.add_all([commitA, commitB])
    	session.commit()

    	response = self.client.get("/commits",
    		headers=[("Accept", "application/json")])

    	self.assertEqual(response.status_code, 200)
    	self.assertEqual(response.mimetype, "application/json")

    	data = json.loads(response.data)
    	self.assertEqual(len(data), 2)

    	commitA = data[0]
    	self.assertEqual(commitA["id"], 1)

    	commitB = data[1]
    	self.assertEqual(commitB["id"], 2)
