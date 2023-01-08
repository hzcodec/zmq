import time
import zmq

TOPIC = b"Volt"

HOST = '127.0.0.1'
PORT = '5001'

context = zmq.Context()
socket = context.socket(zmq.PUB)

socket.bind('tcp://{}:{}'.format(HOST, PORT))
time.sleep(1)

value = 0.0

str_val = str(value)
byte_val = str_val.encode()

while True:
    socket.send_multipart([TOPIC, byte_val, b"Current value"])
    time.sleep(1)

    value += .1
    value = round(value, 2)
    str_val = str(value)
    byte_val = str_val.encode()

    print('[PUB] - value:', value)

socket.close()
context.term()
