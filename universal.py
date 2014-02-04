import urllib
import urllib2

def universal_analytics(webproperty='', category='', action='', ln='', lv=''):
    parameters = {
        'v': '1', 'tid': webproperty, 'cid': 'xyz', 't': 'event',
        'ec': category, 'ea': action, 'el': ln, 'ev': lv
    }
    data = urllib.urlencode(parameters).encode('utf-8')
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MeasurementProtocol/1.0; script)'}
    req = urllib2.Request('https://ssl.google-analytics.com/collect', data, headers)
    res = urllib2.urlopen(req)
    return "ok"