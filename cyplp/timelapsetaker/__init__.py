from worker import Worker

def main():
    worker_ = Worker()
    worker_.newJob(2, "tmp/test_%06d.nef")
    worker_.start()
    import time

    time.sleep(8)
    print "here"
    worker_.go = False


