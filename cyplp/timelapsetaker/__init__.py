from worker import Worker

import zmq
import time

def main():

    context = zmq.Context()

    orderReceiver = context.socket(zmq.REP)
    orderReceiver.bind("tcp://127.0.0.1:5559")
#    orderReceiver.setsockopt(zmq.SUBSCRIBE, "")


    worker_ = Worker()
    while True:
        print "here"

        order = orderReceiver.recv_json()
        print order
        if order['command'] == 'stop':
            worker_.go = False
            orderReceiver.send_json('ack')
            worker_ = Worker()
            continue

        elif order['command'] == 'start':
            if worker_.go:
                orderReceiver.send_json('already running')
                continue
            worker_.newJob(order['interval'], order['filename'], order['batch'])
            worker_.start()
            orderReceiver.send_json('ack')


