import time
from threading import Thread
import os

import couchdbkit

from cyplp.gphoto2 import GPhoto2

class Worker(Thread):
    """
    """
    def __init__(self):
        super(Worker, self).__init__()
        self.go= False

        # server object
        server = couchdbkit.Server()


        # create database
        db = server.get_or_create_db('timelapse')
        StorageFile.set_db(db)

    def newJob(self, interval, filenameTemplate, batch):
        self._interval = interval
        self._filenameTemplate =filenameTemplate
        self._cpt = 0
        self._batch = batch

        self.go = True

    def run(self):
        gphoto2 = GPhoto2()
        gphoto2.initCamera()
        while self.go:
            filename = self._filenameTemplate % self._cpt
            gphoto2.takePicture(filename)

            sf = StorageFile(batch=self._batch, filename=filename)
            sf.save()
            with open(filename, 'rb') as toStore:
                sf.put_attachment(toStore, 'doc.jpg')

            os.remove(filename)
            self._cpt += 1
            time.sleep(self._interval)



class StorageFile(couchdbkit.Document):
    batch = couchdbkit.StringProperty()
    filename = couchdbkit.StringProperty()
