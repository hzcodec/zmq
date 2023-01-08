import time
import zmq

TOPIC1 = b"Volt"
TOPIC2 = b"Amps"

HOST = '127.0.0.1'
PORT = '5001'

context = zmq.Context()
socket = context.socket(zmq.PUB)

socket.bind('tcp://{}:{}'.format(HOST, PORT))
print('Bind to Host: {} - Port: {}'.format(HOST, PORT))
time.sleep(1)

value1 = 0.0
value2 = 0.0

str_val = str(value1)
byte_val1 = str_val.encode()
byte_val2 = str_val.encode()


def send_topic1(byte_val):
    socket.send_multipart([TOPIC1, byte_val, b"Current value1"])


def send_topic2(byte_val):
    socket.send_multipart([TOPIC2, b"Jennie", byte_val])


while True:
    send_topic1(byte_val1)
    send_topic2(byte_val2)

    time.sleep(1)

    value1 += .1
    value1 = round(value1, 2)
    str_val = str(value1)

    value2 = value1 * 5
    str_val2 = str(value2)

    byte_val1 = str_val.encode()
    byte_val2 = str_val2.encode()

    print('[PUB] - value1:', value1)
    print('[PUB] - value2:', value2)

socket.close()
context.term()
