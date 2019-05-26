import queue
import threading
import sys

from sqliscanner import sqliScannerClass
from waybackmachine import waybackMachineClass


class sqliWaybackClass():

    def __init__(self):
        self.urls = []
        self.q = queue.Queue()

    def getWaybackUrls(self,domain):
        self.urls = []
        wbm = waybackMachineClass(domain)
        waybackJson = wbm.getUrls()
        for row in waybackJson:
            self.urls.append(row[0])

    def checkSqli(self,url):
        ss = sqliScannerClass()
        ss.createSqliUrl(url)

    def worker(self):
        while 1:
            url = self.q.get()
            self.checkSqli(url)
            self.q.task_done()

    def run(self,domain):

        self.getWaybackUrls(domain)

        #Spin up workers
        for i in range(50):
            t = threading.Thread(target=self.worker)
            t.daemon = True
            t.start()

        for url in self.urls:
            self.q.put(url)
        self.q.join()


sw = sqliWaybackClass()
sw.run(sys.argv[1])
