import os.path
import json

from flask import request, Response

import models

from git_text import app
from database import session



@app.route("/", methods=["GET"])
def get_updates():
	return "Did you commit to your github today?"

@app.route("/commits", methods=["GET"])
def get_commits():

	commits = session.query(models.Commit).all()
	if not commits:
		commits = []

	data = json.dumps([commit.as_dictionary() for commit in commits])
	return Response(data, 200, mimetype="application/json")

