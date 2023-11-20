import tkinter as tk
from tkinter import ttk

def createTopBar(container):
def createBottomBar(container):

def createLeftColumn(container):
    #columnContainer = createColumnContainer(container)
    ### left column (classes container)
    leftColumn = ttk.Frame(container) # ! apparrently tkintr.ttk.Frame doesn't support background colors, tkinter.Frame does
    #leftColumn = Frame(rootWindow, bg='#EEFFEE')
    leftColumn['borderwidth'] = 1
    leftColumn['relief'] = 'groove'
    leftColumn['padding'] = (8,10)
    #leftColumn.grid(column=0, row=0, rowspan=10, sticky='NSEW') # position frame in column 0
    #leftColumn.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y, expand=True) # moved to main window
    #leftColumn.config(bg='#EEFFEE') # debug color
    leftColumn.pack_propagate(0)
    #leftColumn.config(width = 300)
    #leftColumn['width'] = 800
    #
    #leftColumn.rowConfigure(1, 1)
    label1 = tk.Label(leftColumn, text='top left', bg='#BBFFBB')
    label1.grid(column=0, row=0, sticky=tk.NW)
    label2 = ttk.Label(leftColumn, text='top right text')
    label2.grid(column=1, row=0, sticky=tk.NE)
    label3 = ttk.Label(leftColumn, text='bot left')
    label3.grid(column=0, row=1, sticky=tk.SW)
    label4 = ttk.Label(leftColumn, text='bot right')
    label4.grid(column=1, row=1, sticky=tk.SE)
    #
    return leftColumn
