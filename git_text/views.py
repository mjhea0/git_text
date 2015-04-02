import requests
import moment
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

from config import ADDRESS, PASSWORD, PHONE_NUMBER, USER_NAME
from git_text import app


# routes

@app.route("/")
def index():
    return "hi!"


@app.route("/test")
def get_updates():
    git_commits = get_user_commits()
    if git_commits["total_count"] > 0:
        subject = get_positive_text()
        return "yayyyy", send_text(subject)
    subject = get_negative_text()
    return "nayyyy", send_text(subject)


# helper functions

def get_user_commits():
    today = moment.now().format("YYYY-M-D")
    base_url = 'https://api.github.com/search/repositories'
    api_endpoint = base_url + '?q=user:{0}+pushed:{1}'.format(USER_NAME, today)
    try:
        resp = requests.get(api_endpoint)
        return resp.json()
    except:  # silencing all errors - bad!
        return "yikes! something went wrong!"


def send_text(subject):
    # connect to the server
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(ADDRESS, PASSWORD)

    msg = MIMEMultipart()
    msg['From'] = ADDRESS
    msg['To'] = PHONE_NUMBER
    msg['Subject'] = 'Your Daily Git Text'
    msg.attach(MIMEText(subject))

    server.sendmail(ADDRESS, PHONE_NUMBER, msg.as_string())
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
