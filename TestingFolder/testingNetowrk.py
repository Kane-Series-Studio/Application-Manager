import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")


for request in range(10):
    #  Get the reply.
    message = socket.recv()
    print(f"Received reply {request} [ {message} ]")


# i was scammed oof
