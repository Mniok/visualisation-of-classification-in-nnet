import tkinter as tk
#from tkinter import *
from tkinter import ttk

def createColumnContainer(container):
    ### left column container (for external padding)
    columnContainer = ttk.Frame(container) # tkinter.ttk.Frame doesn't support bgcolor. tkinter.Frame does.
    columnContainer['padding'] = (12, 8)
    #columnContainer.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y, expand=True)
    return columnContainer
    

def createLeftColumn(container):
    leftColumnContainer = createColumnContainer(container)
    ### left column (classes container)
    leftColumnInternal = ttk.Frame(leftColumnContainer) # ! apparrently tkintr.ttk.Frame doesn't support background colors, tkinter.Frame does
    #leftColumn = Frame(rootWindow, bg='#EEFFEE')
    leftColumnInternal['borderwidth'] = 1
    leftColumnInternal['relief'] = 'groove'
    leftColumnInternal['padding'] = (2,1) # 2 widthwise, 1 heightwise
    #leftColumn.grid(column=0, row=0, rowspan=10, sticky='NSEW') # position frame in column 0
    leftColumnInternal.pack(side=tk.LEFT, fill=tk.BOTH, expand=True) # moved to main window
    #leftColumn.config(bg='#EEFFEE') # debug color
    leftColumnInternal.pack_propagate(0)
    #leftColumn.config(width = 300)
    #leftColumn['width'] = 800
    #
    #leftColumn.rowConfigure(1, 1)
    label1 = tk.Label(leftColumnInternal, text='top left', bg='#BBFFBB')
    label1.grid(column=0, row=0, sticky=tk.NW)
    label2 = ttk.Label(leftColumnInternal, text='top right text')
    label2.grid(column=1, row=0, sticky=tk.NE)
    label3 = ttk.Label(leftColumnInternal, text='bot left')
    label3.grid(column=0, row=1, sticky=tk.SW)
    label4 = ttk.Label(leftColumnInternal, text='bot right')
    label4.grid(column=1, row=1, sticky=tk.SE)
    #
    return leftColumnContainer
