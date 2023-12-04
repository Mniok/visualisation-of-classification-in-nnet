import tkinter as tk
from tkinter import ttk
from classFieldComponent import createClassField

class ClassChoosersStore:
    def __init__(self):
        self.currentAddedClassNumber = 0
        self.frame = None
        self.created = False
        self.classChoosers = []

    def addNewClass(self):
        if not self.created:
            raise Exception('Class chooser not created yet')
        self.currentAddedClassNumber += 1
        newClassField = createClassField(
            self.frame,
            f'Klasa {self.currentAddedClassNumber}',
            'blue', # TODO: color sequence
            'o' # TODO: marker sequence
        )
        newClassField.frame.pack(side=tk.TOP, fill=tk.X, expand=True)
        self.classChoosers.append(newClassField)


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
