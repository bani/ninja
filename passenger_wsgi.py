import os, sys
cmd_folder = os.path.dirname(os.path.abspath(__file__))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

import bottle
from bottle import route, run, post
from datetime import datetime, timedelta
import urllib
import urllib2

@post('/event/<webproperty>/<category>/<action>/<ln>/<lv>')
def universal_analytics(webproperty='', category='', action='', ln='', lv=''):
    if lv == '0':
        est = datetime.now() + timedelta(hours=3)
        hour = est.timetuple()
        ln = str(hour[3])
        lv = hour[4]
    else:
        lv = int(lv)
    parameters = {
        'v': '1', 'tid': webproperty, 'cid': 'xyz', 't': 'event',
        'ec': category, 'ea': action, 'el': ln, 'ev': lv
    }
    data = urllib.urlencode(parameters).encode('utf-8')
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MeasurementProtocol/1.0; script)'}
    req = urllib2.Request('https://ssl.google-analytics.com/collect', data, headers)
    res = urllib2.urlopen(req)
    return "ok"

def application(environ, start_response):
    return bottle.default_app().wsgi(environ,start_response)

if __name__ == "__main__":
    bottle.debug(True)
    run(reloader=True)