#!/usr/bin/python

from flask import Flask
import time
import sys
sys.path.insert(0, '/usr/lib/python2.7/bridge/')
from bridgeclient import BridgeClient as bridgeclient

app = Flask(__name__, static_url_path='/static', static_folder='/var/www/static')
brg = bridgeclient()

@app.route('/')
def default_route():
    return "Hello World!"

@app.route('/data/get')
def bridge_get_all():
        res = brg.getall()
        arr = []
        for k, v in res.iteritems():
                arr.append('"' + k + '":"' + v + '"')
        msg = '{"value":{' + ','.join(arr) + '},"response":"get"}'
        return msg, 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/data/get/<key>')
def bridge_get_bykey(key):
        res = brg.get(key)
        msg = '{"value":"' + res + '","key":"' + key + '","response":"get"}'
        return msg, 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/data/put/<key>/<val>')
def bridge_put(key, val):
        res = brg.put(key, val)
        msg = '{"value":"' + val + '","key":"' + key + '","response":"put"}'
        return msg, 200, {'Content-Type': 'application/json; charset=utf-8'}

if __name__ == "__main__":
        app.run(host='0.0.0.0',port='8088')
