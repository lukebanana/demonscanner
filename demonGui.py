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
# Filename: demonGui.py

from tkinter import *
import demonScanner

class DemonGui:
    RANGE_MIN = 0
    RANGE_MAX = 65535

    def __init__(self, title, model, lenX, lenY):
        # main Window
        self.scanModel = model
        self.mainWin = Tk()
        self.mainWin.title(title)
        self.lenX = lenX
        self.lenY = lenY
        dimensions = "%dx%d" % (lenX, lenY)
        self.mainWin.geometry(dimensions)

        self.frame = Frame(self.mainWin)

        self.createHead()
        self.createCenter()
        self.createFooter()


    def createHead(self):
        self.labelHead = Label(self.mainWin, text="Enter Port range:")
        self.labelFrom = Label(self.mainWin, text="From")
        self.labelTo = Label(self.mainWin, text="To")

        self.portScaleFrom = Scale(self.mainWin, from_=self.RANGE_MIN, to=self.RANGE_MAX,
        length=self.lenX, orient=HORIZONTAL, variable=IntVar)
        self.portScaleTo = Scale(self.mainWin, from_=self.RANGE_MIN, to=self.RANGE_MAX,
        length=self.lenX, orient=HORIZONTAL, variable=IntVar)


        self.labelHead.grid()
        self.labelFrom.grid(row=1, column=0)
        self.portScaleFrom.grid(row=2, column=0)
        self.labelTo.grid(row=3, column=0)
        self.portScaleTo.set(self.RANGE_MAX)
        self.portScaleTo.grid(row=4, column=0)

    def createCenter(self):
        self.targetLabel = Label(self.mainWin, text="Target-IP")
        self.ipInput = Entry(self.mainWin)
        self.ipInput.grid(row=5)
        # Start-Button
        self.startBtn = Button(self.mainWin, text="Start Scan",
        command=self.callScan)
        self.startBtn.grid(row=6)

    def createFooter(self):
        # Scroll Bar
        self.scrollbar = Scrollbar(self.mainWin)
        self.scrollbar.grid(row=8, column=1, sticky=N+S)
        # List Box
        self.listBox = Listbox(self.mainWin, yscrollcommand=self.scrollbar.set)
        self.listBox.grid(row=8, column=0, sticky=N+E+S+W)
        self.countLabel = Label(self.mainWin, text="")
        self.countLabel.grid(row=9, column=0)

    def callScan(self):
        self.setParameters()
        self.scanModel.scanTarget()

    def setParameters(self):
         self.scanModel.setRange(self.portScaleFrom.get(), self.portScaleTo.get())
         self.scanModel.setTarget(self.ipInput.get())

    def updateList(self, msg):
        # Wenn Port offen
        if msg[2] == True:
            self.listBox.insert(END, msg[0])

        self.countLabel.configure(text="Scanning Port %d..." % msg[1])
        self.listBox.see(END)
        self.listBox.update()


# End of demonGui.py