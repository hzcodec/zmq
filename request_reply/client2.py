import zmq

context = zmq.Context()

#  Socket to talk to server
print('Connecting ...')

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
for request in range(10):
    print('Sending request from client %s' % request)
    socket.send(b"Message from client")

    #  Get the reply.
    message = socket.recv()
    print('Received reply %s [ %s ]' % (request, message))
