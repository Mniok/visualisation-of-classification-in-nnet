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
        self.classChoosers.append(newClassField)

    def deleteClass(self, targetID):
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
    classChoosersStore.classChoosers[0].isSelected = True # init with first class already selected
    classChoosersStore.classChoosers[0].updateSelectedStyle()

    addClassButton = ttk.Button(
        classChooserContainer,
        text='+',
        command=classChoosersStore.addNewClass)
    addClassButton.pack(side=tk.TOP, fill=tk.X, expand=False)
    return classChooserContainer
