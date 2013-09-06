import os, sys
cmd_folder = os.path.dirname(os.path.abspath(__file__))
if cmd_folder not in sys.path:
  sys.path.insert(0, cmd_folder)

import bottle
from bottle import route, run
import urllib
import urllib2

@route('/event/<webproperty>/<category>/<action>/<label>/<value>', method='POST')
def universal_analytics(webproperty='UA-XXXXX-1', category='Ninja', action='', label='', value='0'):
  parameters = {
    'v': '1', 'tid': webproperty, 'cid': 'ninja', 't': 'event',
    'ec': category, 'ea': action, 'el': label, 'ev': int(value)
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
