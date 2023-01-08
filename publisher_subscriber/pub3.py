import time
import zmq

TOPIC = b"Volt"
TOPIC2 = b"Amps"

HOST = '127.0.0.1'
PORT = '5001'

context = zmq.Context()
socket = context.socket(zmq.PUB)

socket.bind('tcp://{}:{}'.format(HOST, PORT))
time.sleep(1)

value = 0.0
value2 = 0.0

str_val = str(value)
byte_val = str_val.encode()
byte_val2 = str_val.encode()

while True:
    socket.send_multipart([TOPIC, byte_val, b"Current value"])
    socket.send_multipart([TOPIC2, b"Jennie", byte_val2])
    time.sleep(1)

    value += .1
    value = round(value, 2)
    str_val = str(value)

    value2 = value * 5
    str_val2 = str(value2)

    byte_val = str_val.encode()
    byte_val2 = str_val2.encode()

    print('[PUB] - value:', value)

socket.close()
context.term()
