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
from email.MIMEText import MIMEText



@app.route("/", methods=["GET"])
def get_updates():
	git_commits = get_user_commits()
	if git_commits["total_count"] > 0:
		subject = get_positive_text()
		return "yayyyy", send_text(subject)
	subject = get_negative_text()
	return "nayyyy", send_text(subject)



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
		resp = requests.get(url)
		return resp.json()
	except: # this needs to be fixed
		return "fix this"

def send_text(subject):
	# connect to the server
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(address, password)

	msg = MIMEMultipart()
	msg['From'] = address
	msg['To'] = phone_number
	msg['Subject'] = 'Your Daily Git Text'
	msg.attach(MIMEText(subject))

	server.sendmail(address, phone_number, msg.as_string())
	server.quit()

def get_positive_text():
	# use the theysaidso.com API to get the quote of the day
	url = 'http://api.theysaidso.com/qod.json'
	try:
		resp = requests.get(url)
		resp = resp.json()
		return resp["contents"]["quote"]
	except:
		return "Great job today, pal. Keep up the good work!"

def get_negative_text():
	return "You better commit before you go to sleep!"