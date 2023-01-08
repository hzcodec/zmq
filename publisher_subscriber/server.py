import json
import time
import zmq

HOST = '127.0.0.1'
PORT = '5001'

ctx = zmq.Context()

s = ctx.socket(zmq.PUSH)
s.bind('tcp://{}:{}'.format(HOST, PORT))

local_value = 0.1

while True:
    print('Server is running ...')

    msg = {
        'code': 200,
        'text': 'Hello from server',
        'Value': local_value
    }

    msg_json = json.dumps(msg)

    s.send_string(msg_json)
    time.sleep(1)

    msg['Value'] = local_value
    local_value += .2
    local_value = round(local_value, 2)
