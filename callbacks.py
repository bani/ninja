import os, sys
cmd_folder = os.path.dirname(os.path.abspath(__file__))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

import bottle
from bottle import route, run, post
from universal import universal_analytics
from datetime import datetime, timedelta

@post('/event/<webproperty>/<category>/<action>/<ln>/<lv>')
def send_data(webproperty='', category='', action='', ln='', lv=''):
    if lv == '0':
        est = datetime.now() + timedelta(hours=3)
        hour = est.timetuple()
        ln = str(hour[3])
        lv = hour[4]
    else:
        lv = int(lv)
    universal_analytics(webproperty=webproperty, category=category, action=action, ln=ln, lv=lv)

def application(environ, start_response):
    return bottle.default_app().wsgi(environ,start_response)

if __name__ == "__main__":
    bottle.debug(True)
    run(reloader=True)