import json
import zmq

HOST = '127.0.0.1'
PORT = '5001'

ctx = zmq.Context()
s = ctx.socket(zmq.PULL)

s.connect('tcp://{}:{}'.format(HOST, PORT))

while True:
    msg = s.recv()

    ds = json.loads(msg)
    print('%s :: %s - %s' % (ds['code'], ds['text'], ds['Value']))
