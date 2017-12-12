import time
import zmq

def main():
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.bind("tcp://*:5563")

    while True:
        publisher.send_multipart([b"A", b"Send A messages"])
        publisher.send_multipart([b"B", b"Send B messages"])
	print('Send messages')
	time.sleep(1)

    publisher.close()
    context.term()


if __name__ == "__main__":
    main()
