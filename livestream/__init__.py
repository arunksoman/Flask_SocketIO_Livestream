# -*- coding: utf-8 -*-

from gevent import monkey
# see: https://github.com/miguelgrinberg/Flask-SocketIO/issues/65
monkey.patch_all()

from flask import Flask
from flask_socketio import SocketIO
from queue import Queue
from engineio.payload import Payload

Payload.max_decode_packets = 500
# from werkzeug.contrib.cache import MemcachedCache
# cache = MemcachedCache(['127.0.0.1:11211'])

app = Flask(__name__)
app.config['SECRET_KEY'] = '?\xbf,\xb4\x8d\xa3"<\x0c\xb0@\x0f5\xac,w\xee\x8d$0\x13\x8b83'
app.queue = Queue()
socketio = SocketIO(async_mode='gevent', ping_timeout=3, ping_interval=0)
socketio = SocketIO(app)

from .views import *
