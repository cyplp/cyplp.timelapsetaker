import time
from threading import Thread

from cyplp.gphoto2 import GPhoto2

class Worker(Thread):
    """
    """
    def __init__(self):
        super(Worker, self).__init__()
        self.go= False

    def newJob(self, interval, filenameTemplate, ):
        self._interval = interval
        self._filenameTemplate =filenameTemplate
        self._cpt = 0

        self.go = True

    def run(self):
        gphoto2 = GPhoto2()
        gphoto2.initCamera()
        while self.go:
            gphoto2.takePicture(self._filenameTemplate
                                % self._cpt)
            self._cpt += 1
            time.sleep(self._interval)



