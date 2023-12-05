import tkinter as tk
from tkinter import ttk
from classFieldComponent import createClassField

class ClassChoosersStore:
    def __init__(self):
        self.currentAddedClassNumber = 0
        self.frame = None
        self.created = False
        self.classChoosers = []
        self.selectedClassID = None

    def getSelectedClassData(self):
        if self.selectedClassID == None: raise Exception("No selected class present")
        for i in range(0, len(self.classChoosers)):
            cl = self.classChoosers[i]
            if id(cl) == self.selectedClassID:
                return {
                    "c": i,
                    "name": cl.name,
                    "color": cl.color,
                    "marker": cl.marker
                }

    def addNewClass(self):
        if not self.created:
            raise Exception('Class chooser not created yet')
        self.currentAddedClassNumber += 1
        newClassField = createClassField(
            self.frame,
            f'Klasa {self.currentAddedClassNumber}',
            'blue', # TODO: color sequence
            'o', # TODO: marker sequence
            deleteHandler=self.deleteClass,
            selectHandler=self.selectClass
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
                print(len(self.classChoosers), i, i < len(self.classChoosers))
                if i+1 < len(self.classChoosers): # ... there is a next class
                    self.classChoosers[i + 1].isSelected = True # to keep element in same place selected
                    self.classChoosers[i + 1].updateSelectedStyle()
                    self.selectedClassID = id(self.classChoosers[i + 1])
                elif len(self.classChoosers) > 1: # ... last, but there are previous classes
                    self.classChoosers[i - 1].isSelected = True # to keep element above (now new last) selected
                    self.classChoosers[i - 1].updateSelectedStyle()
                    self.selectedClassID = id(self.classChoosers[i - 1])

        self.classChoosers = list(filter(lambda cl: id(cl) != targetID, self.classChoosers))

    def selectClass(self, targetID):
        for classField in self.classChoosers:
            classField.isSelected = id(classField) == targetID
            classField.updateSelectedStyle()
        self.selectedClassID = targetID

classChoosersStore = ClassChoosersStore()

def createClassChooser(container):
    classChooserContainer = tk.Frame(container)

    classChoicesFrame = tk.Frame(classChooserContainer)
    classChoicesFrame.pack(side=tk.TOP, fill=tk.X, expand=False)
    classChoosersStore.frame = classChoicesFrame
    classChoosersStore.created = True

    classChoosersStore.addNewClass()  # add initial class so classes chooser is not empty on start

    addClassButton = ttk.Button(
        classChooserContainer,
        text='+',
        command=classChoosersStore.addNewClass)
    addClassButton.pack(side=tk.TOP, fill=tk.X, expand=False)
    return classChooserContainer
