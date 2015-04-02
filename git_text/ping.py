# http://apscheduler.readthedocs.org/en/3.0/

from apscheduler.schedulers.blocking import BlockingScheduler
import requests


sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=20)
def job():
    # send get request to "/" route every twenty minutes
    requests.get('/')


@sched.scheduled_job('cron', hour=22)
def ping():
    # send get request to "/test" at ten pm each day
    requests.get('/test')


sched.start()
