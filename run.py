import os
#from flask.ext.script import Manager

from git_text import app

#manager = Manager(app)

#@manager.command
def run():
	port = int(os.environ.get('PORT', 8080))
	app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
	run()