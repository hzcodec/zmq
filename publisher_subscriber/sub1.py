import zmq

host = '127.0.0.1'
port = '5001'

context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect('tcp://{}:{}'.format(host, port))

socket.subscribe('')
print(socket.recv_string())
