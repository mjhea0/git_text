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
	if git_commits["total_count"] > 0:
		positive_text = get_positive_text()
		return positive_text.contents["quote"]
		#return "yayyyy", #send_text()
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
	msg['Subject'] = get_positive_text()

	server.sendmail(address, phone_number, msg.as_string())
	server.quit()

def get_positive_text():
	# use the theysaidso.com API to get the quote of the day
	url = 'http://api.theysaidso.com/qod.json'
	try:
		resp = requests.get(url)
		resp = resp.json()
		return resp
		#print resp["quote"]
		#return resp["quote"]
	except:
		return "Great job today, pal. Keep up the good work!"



