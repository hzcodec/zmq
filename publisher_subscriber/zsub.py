import zmq


def main():
    print('Connect and subscribe to B')

    context = zmq.Context()
    subscriber = context.socket(zmq.SUB)
    subscriber.connect("tcp://localhost:5563")

    # select subscriber A or B
    # subscriber.setsockopt(zmq.SUBSCRIBE, b"B")
    subscriber.setsockopt(zmq.SUBSCRIBE, b"A")

    while True:
        [address, contents] = subscriber.recv_multipart()
        print("[%s] %s" % (address, contents))

    subscriber.close()
    context.term()


if __name__ == "__main__":
    main()
