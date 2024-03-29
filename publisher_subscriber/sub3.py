import zmq

TOPIC = b"Volt"
HOST = '127.0.0.1'
PORT = '5001'

context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect('tcp://{}:{}'.format(HOST, PORT))
print('Connect to Host: {} - Port: {}'.format(HOST, PORT))

socket.subscribe(TOPIC)

while True:
    rv = socket.recv_multipart()
    print(rv[1])

    print('[SUB] - Topic:', rv[0].decode('ascii'))
    print('[SUB] - Message:', rv[1].decode('ascii'))
    print('[SUB] - Message:', rv[2].decode('ascii'))

    str_val = rv[1].decode('utf-8')
    f_val = float(str_val)

    if rv[1] == b'1.1':
        break


print('Client closed')
socket.close()
context.term()
