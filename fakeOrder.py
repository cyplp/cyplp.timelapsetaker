import zmq
import time

context = zmq.Context()

orderEmetter = context.socket(zmq.REQ)
orderEmetter.connect("tcp://127.0.0.1:5559")
#orderEmetter.setsockopt(zmq.PUB, "")

# orderEmetter.send_json({'command': 'stop'})
# print orderEmetter.recv_json()
# time.sleep(4)
orderEmetter.send_json({'command': 'start', 'interval': 1, 'filename': 'tmp/crnnwaza3%d.nef', 'batch': "testCoucdb"})
print orderEmetter.recv_json()
