import tkinter as tk
from tkinter import ttk
from classFieldComponent import createClassField

from matplotlib import colors
import math

def getColorInSequence(n):
    startingColor = colors.to_rgb('blue')
    hsv = colors.rgb_to_hsv(startingColor)
    nthColor = ((hsv[0]+((n-1)*0.13))%1, # empirically selected values that produce a reasonable sequence for the first couple colours
                hsv[1]*(0.97**(n-1)),
                hsv[2]*(0.95**(math.floor(max(0, n-14))/7)))
    return colors.hsv_to_rgb(nthColor)
def getMarkerInSequence(n):
    usedDefaultMarkers = ['o', ',', '+', '.']
    return usedDefaultMarkers[math.floor(n/8) % len(usedDefaultMarkers)]

class ClassChoosersStore:
    def __init__(self):
        self.currentAddedClassNumber = 0
        self.frame = None
        self.created = False
        self.classChoosers = []
        self.selectedClassID = None
        self.redrawMarkerHandler = None # assigned in plotComponent

    def getSelectedClassData(self):
        if self.selectedClassID == None: raise Exception("No selected class present")
        for i in range(0, len(self.classChoosers)):
            cl = self.classChoosers[i]
            if id(cl) == self.selectedClassID:
                return self.getClassData(i)

    def getClassData(self, c):
        return {
            "c": c,
            "name": self.classChoosers[c].name,
            "color": self.classChoosers[c].color,
            "marker": self.classChoosers[c].marker
        }

    def addNewClass(self):
        if not self.created:
            raise Exception('Class chooser not created yet')
        self.currentAddedClassNumber += 1
        newClassField = createClassField(
            self.frame,
            f'Klasa {self.currentAddedClassNumber}',
            getColorInSequence(self.currentAddedClassNumber),
            getMarkerInSequence(self.currentAddedClassNumber),
            deleteHandler=self.deleteClass,
            selectHandler=self.selectClass,
            redrawOnPlotHandler=self.redrawClassOnPlot
        )
        newClassField.frame.pack(side=tk.TOP, fill=tk.X, expand=True)
        if len(self.classChoosers) == 0:
            newClassField.isSelected = True # select if it's the only class
            newClassField.updateSelectedStyle()
        self.classChoosers.append(newClassField)

    def deleteClass(self, targetID):
        for i in range(0, len(self.classChoosers)):
            cl = self.classChoosers[i]
            if id(cl) == targetID and cl.isSelected: # deleting selected class
                if i+1 < len(self.classChoosers): # ... there is a next class
                    self.classChoosers[i + 1].isSelected = True # to keep element in same place selected
                    self.classChoosers[i + 1].updateSelectedStyle()
                    self.selectedClassID = id(self.classChoosers[i + 1])
                elif len(self.classChoosers) > 1: # ... last, but there are previous classes
                    self.classChoosers[i - 1].isSelected = True # to keep element above (now new last) selected
                    self.classChoosers[i - 1].updateSelectedStyle()
                    self.selectedClassID = id(self.classChoosers[i - 1])
                break

        self.classChoosers = list(filter(lambda cl: id(cl) != targetID, self.classChoosers))
        for i in range(0, len(self.classChoosers)):
            self.redrawMarkerHandler(i)

    def selectClass(self, targetID):
        for classField in self.classChoosers:
            classField.isSelected = id(classField) == targetID
            classField.updateSelectedStyle()
        self.selectedClassID = targetID

    def redrawClassOnPlot(self, targetID):
        for i in range(0, len(self.classChoosers)):
            cl = self.classChoosers[i]
            if id(cl) == targetID:
                self.redrawMarkerHandler(i)
                break


classChoosersStore = ClassChoosersStore()

def createClassChooser(container):
    classChooserContainer = tk.Frame(container)

    classChoicesFrame = tk.Frame(classChooserContainer)
    classChoicesFrame.pack(side=tk.TOP, fill=tk.X, expand=False)
    classChoosersStore.frame = classChoicesFrame
    classChoosersStore.created = True

    classChoosersStore.addNewClass()  # add initial class so classes chooser is not empty on start
    classChoosersStore.selectClass(id(classChoosersStore.classChoosers[0])) # highlighting first class is also handled in classFieldComponent, this is just to set selectedClassID

    addClassButton = ttk.Button(
        classChooserContainer,
        text='+',
        command=classChoosersStore.addNewClass)
    addClassButton.pack(side=tk.TOP, fill=tk.X, expand=False)
    return classChooserContainer
