#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Luke
#
# Created:     24.03.2013
# Copyright:   (c) Luke 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------



import demonGui
import demonScanner

class DemonController:
    def __init__(self):
        self.model = demonScanner.DemonScanner()
        self.model.counter.addCallback(self.counterChanged)
        self.gui = demonGui.DemonGui("Port Demon", self.model, 550, 400)
        self.gui.mainWin.mainloop()

    def counterChanged(self, msg):
        self.gui.updateList(msg);