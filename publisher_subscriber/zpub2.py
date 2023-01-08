#!/usr/bin/env python
import zmq
import time
import random

port = "5500"

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" %port)

print('Sending message to port 5500')

time.sleep(3)

while True:
    topic = random.randrange(9999, 10005)
    message_data = random.randrange(1, 215) - 80
    print("%d %d" % (topic, message_data))
    socket.send("%d %d" % (topic, message_data))
    time.sleep(1)

socket.close()
context.term()
print('Closed')
