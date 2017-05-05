#!./ENV3.5 python3
#FofPyNP

from urllib.parse import quote_plus
import http.client
import json

base = '/maps/api/geocode/json'

def geocode(address):
    path = '{}?address={}&sensor=false'.format(base, quote_plus(address))
    connection = http.client.HTTPConnection('maps.google.com')
    connection.request('GET', path)
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    print(reply['result'][0]['geometry']['location']])

if __name__ == '__main__':
    geocode('207 N. Defiance St, Archblod, OH')
    #path = '/maps/api/geocode/json?adddress=207+N.+Definance+St%2C+Archblod%2C+OH&sensor=false'

    