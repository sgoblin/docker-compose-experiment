#!/usr/bin/env python3

import falcon
from redis import StrictRedis as Redis

redisdb = Redis(host="redis", port=6379)
with open('index.html', 'r') as indexfile:
    indexPage = indexfile.read()

with open('main.js', 'r') as jsfile:
    jsPage = jsfile.read()

class IncrementCounterHandler:
    def on_post(self, req, resp):
        redisdb.incr('clicks')
        resp.status = falcon.HTTP_200
        resp.body = "Success"

    def on_get(self, req, resp):
        resp.body = redisdb.get('clicks')
        resp.status = falcon.HTTP_200

class IndexPageHandler:
    def on_get(self, resp):
        resp.body = indexPage
        resp.status = falcon.HTTP_200
        resp.content_type = "text/html"

class MainJSHandler:
    def on_get(self, resp):
        resp.body = jsPage
        resp.status = falcon.HTTP_200
        resp.content_type = "application/javascript"

app = falcon.API()
counterHandler = IncrementCounterHandler()

app.add_route('/increment', counterHandler)
app.add_route('/main.js', MainJSHandler)
app.add_route('/', IndexPageHandler)
