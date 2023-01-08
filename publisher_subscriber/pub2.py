import time
import zmq

host = '127.0.0.1'
port = '5001'

context = zmq.Context()
socket = context.socket(zmq.PUB)

socket.bind('tcp://{}:{}'.format(host, port))
time.sleep(1)

socket.send_multipart([b"Voltage", b"Hello"])
