import tkinter as tk
from tkinter import ttk

class ClassField:
    def __init__(self, frame, name, color, marker):
        self.frame = frame
        self.name = name
        self.color = color
        self.marker = marker

        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)

        self.nameLabel = ttk.Label(self.frame, text=name)
        self.nameLabel.grid(column=0, row=0, sticky=tk.NW)

    def update(self):
        return 'todo'

def createClassField(container, name, color, marker):
    classField = ClassField(tk.Frame(container),
                            name,
                            color,
                            marker)
    #classField.frame.config(bg='#EEFFEE') # debug color
    return classField
