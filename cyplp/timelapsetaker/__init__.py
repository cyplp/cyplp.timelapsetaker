from worker import Worker

import zmq


def main():

    context = zmq.Context()

    orderReceiver = context.socket(zmq.REP)
    orderReceiver.bind("tcp://127.0.0.1:5559")
#    orderReceiver.setsockopt(zmq.SUBSCRIBE, "")

#CalledProcessError:
    worker_ = Worker()
    while True:

        order = orderReceiver.recv_json()

        if order['command'] == 'stop':
            worker_.go = False
            orderReceiver.send_json('ack')
            worker_ = Worker()

        elif order['command'] == 'start':
            if worker_.go:
                orderReceiver.send_json('already running')
                continue
            worker_.newJob(order['interval'], order['filename'], order['batch'])
            worker_.start()
            orderReceiver.send_json('ack')

        elif order['command'] == 'status':
            choices = {True: 'on',
                       False: 'off',}

            orderReceiver.send_json(choices[worker_.go])

