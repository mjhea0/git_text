# http://apscheduler.readthedocs.org/en/3.0/

from apscheduler.schedulers.blocking import BlockingScheduler
import requests
sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=20)
def job():
    # send get request to "/" route
    r = requests.get('/')
    print 'This job is run every minute.'

@sched.scheduled_job('cron', hour=22):
def ping():
    #send get request to "/test"
    r = requests.get('/test')
    print "This pings the actual route"


sched.start()