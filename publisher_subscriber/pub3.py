import time
import zmq

host = '127.0.0.1'
port = '5001'

context = zmq.Context()
socket = context.socket(zmq.PUB)

socket.bind('tcp://{}:{}'.format(host, port))
time.sleep(1)

value = 0.0

str_val = str(value)
byte_val = str_val.encode()

while True:
    socket.send_multipart([b"Voltage", byte_val])
    time.sleep(1)

    value += .1
    value = round(value, 2)
    str_val = str(value)
    byte_val = str_val.encode()

    print('[PUB] - value:', value)

socket.close()
context.term()
