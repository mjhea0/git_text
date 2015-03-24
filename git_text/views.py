import os.path
import json

from flask import request, Response

import models

from git_text import app
from database import session

import requests

import moment
from datetime import datetime

from info import *

import smtplib
from email.MIMEMultipart import MIMEMultipart



@app.route("/", methods=["GET"])
def get_updates():
	git_commits = get_user_commits()
	print type(git_commits)
	if git_commits["total_count"] > 0:
		return "yayyyyy", send_text()
	return "nayyyy"
	return send_text()


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

def send_text():
	# connect to the server
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(address, password)

	msg = MIMEMultipart()
	msg['From'] = address
	msg['To'] = phone_number
	msg['Subject'] = 'Your daily git_text motivation'

	server.sendmail(address, phone_number, msg.as_string())
	server.quit()





