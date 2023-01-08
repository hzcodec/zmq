import zmq

TOPIC = b"Amps"
HOST = '127.0.0.1'
PORT = '5001'

context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect('tcp://{}:{}'.format(HOST, PORT))
print('Connect to Host: {} - Port: {}'.format(HOST, PORT))

socket.subscribe(TOPIC)

while True:
    rv = socket.recv_multipart()
    print('[SUB] - Topic:', rv[0].decode('ascii'))
    print('[SUB] - Message:', rv[1].decode('ascii'))
    print('[SUB] - Message:', rv[2].decode('ascii'))

socket.close()
context.term()
