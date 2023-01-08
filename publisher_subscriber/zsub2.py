import sys
import zmq

port = "5500"

context = zmq.Context()
socket = context.socket(zmq.SUB)

print('Connect to localhost port %s' % port)
socket.connect("tcp://localhost:%s" % port)

topicfilter = "10001"
socket.setsockopt(zmq.SUBSCRIBE, topicfilter)

for update_nbr in range(10):
    string = socket.recv()
    topic, messagedata = string.split()
    print topic, messagedata
