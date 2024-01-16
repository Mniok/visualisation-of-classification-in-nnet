import tkinter as tk
from tkinter import ttk
from classChooser import createClassChooser

def createColumnContainer(container):
    ### left column container (for external padding)
    columnContainer = ttk.Frame(container)
    columnContainer['padding'] = (12, 8)
    return columnContainer
    

def createLeftColumn(container):
    leftColumnContainer = createColumnContainer(container)
    leftColumnInternal = ttk.Frame(leftColumnContainer)

    leftColumnInternal['borderwidth'] = 1
    leftColumnInternal['relief'] = 'groove'
    leftColumnInternal['padding'] = (2,1) # 2 widthwise, 1 heightwise

    leftColumnInternal.pack(side=tk.LEFT, fill=tk.BOTH, expand=True) # moved to main window

    classChooser = createClassChooser(leftColumnInternal)
    classChooser.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    return leftColumnContainer
