import zmq

host = '127.0.0.1'
port = '5001'

context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect('tcp://{}:{}'.format(host, port))

socket.subscribe(b'Voltage')

while True:
    rv = socket.recv_multipart()
    print('[SUB] - Topic:', rv[0].decode('ascii'))
    print('[SUB] - Message:', rv[1].decode('ascii'))

socket.close()
context.term()
