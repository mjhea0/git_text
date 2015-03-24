import os.path
import json

from flask import request, Response

import models

from git_text import app
from database import session

import requests

import moment
from datetime import datetime



@app.route("/", methods=["GET"])
def get_updates():
	git_commits = get_user_commits()
	print type(git_commits)
	if git_commits["total_count"] > 0:
		return "yayyyyy"

	return "nayyyy"


@app.route("/commits", methods=["GET"])
def get_commits():

	commits = session.query(models.Commit).all()
	if not commits:
		commits = []

	data = json.dumps([commit.as_dictionary() for commit in commits])
	return Response(data, 200, mimetype="application/json")

def get_user_commits():
	today = moment.now().format("YYYY-M-D")
	#print moment.now()
	url = 'https://api.github.com/search/repositories?q=user:kyle8285+pushed:{}'.format(today)
	try:
		r = requests.get(url)
		return r.json()
	except: # this needs to be fixed
		return "fix this"





