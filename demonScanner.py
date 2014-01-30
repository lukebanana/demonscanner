#-------------------------------------------------------------------------------
# Name:        Gui
# Purpose:
#
# Author:      Luke
#
# Created:     24.03.2013
# Copyright:   (c) Luke 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#!/usr/bin/python
# Filename: demonScanner.py
from socket import *

class Observable:
    def __init__(self, initialValue=None):
        self.data = initialValue
        self.callbacks = {}

    def addCallback(self, func):
        self.callbacks[func] = 1

    def delCallback(self, func):
        del self.callback[func]

    def _docallbacks(self):
        for func in self.callbacks:
            func(self.data)

    def set(self, data):
        self.data = data
        self._docallbacks()

    def get(self):
        return self.data

    def unset(self):
        self.data = None


class DemonScanner:
    def __init__(self, target=None):
        if target is None:
            self.target = "localhost"
        else:
            self.target = target
        self.rangeFrom = 0
        self.rangeTo = 1024
        # Obersrvable
        self.counter = Observable(0)

    def setTarget(self, target):
        if target != "":
            self.target=target

    def getTarget(self):
        return self.target

    def setRange(self, rangeFrom, rangeTo):
        self.rangeFrom = rangeFrom
        self.rangeTo = rangeTo

    def scanTarget(self):
        targetIP = gethostbyname(self.target)
        # print('Starting scan on host %s' % targetIP)

        #scan reserved ports
        # print('From %d to &d' self.rangeFrom, self.rangeTo)
        for counter in range(self.rangeFrom, self.rangeTo):
            s = socket(AF_INET, SOCK_STREAM)

            result = s.connect_ex((targetIP, counter))

            #if connection is established
            if(result == 0) :
                status = True
                msg = ["Port %d: OPEN" % counter, counter, status]
            else:
                status = False
                msg = ["Port %d: Closed" % counter, counter, status]
            # Obersrevable
            self.counter.set(msg)
        s.close()

# End of demonScanner.py