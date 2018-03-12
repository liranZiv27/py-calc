#Made by Liran Ziv 31.12.17

import redis
import time
import re
import json

actions = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}

r = redis.StrictRedis()
p = r.pubsub(ignore_subscribe_messages=True)
p.subscribe('input')
p.get_message()

while True:
  message = p.get_message()

  if message:
    data = json.loads(message['data'])
    action = actions[data['action']]
    r.publish('output', action(data['x'], data['y']))

  time.sleep(0.001)
