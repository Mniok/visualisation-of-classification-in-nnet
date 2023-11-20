import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

import pandas as pd
import matplotlib.pyplot as plt

#def createTopBar(container):
#def createBottomBar(container):

def createPlot(container):
    fig = Figure(figsize=(5, 5), dpi=100)
    plot1 = fig.add_subplot(1, 1, 1) # 1x1 grid, place plot in index 1
    #! temp for dataset
    baseDir = "C:\\Users\\Stopy\\Documents\\GitHub\\visualisation-of-classification-in-nnet\\datasets\\"
    corners80 = pd.read_csv(baseDir + "corners_80_commas.csv")
    chosenDataset = corners80
    #! temp for dataset
    scatter = plot1.scatter(
        x = chosenDataset['x'].values.tolist(),
        y = chosenDataset['y'].values.tolist(),
        c = chosenDataset['class'].values.tolist())
    canvas = FigureCanvasTkAgg(fig, master=container)
    canvas.draw()
    canvas.get_tk_widget().pack()

    def callbackOnCanvasClick(event):
        if event.xdata is None or event.ydata is None: return
        dataToAppend = pd.DataFrame([[event.xdata, event.ydata, 1]], columns=['x', 'y', 'class'])
        nonlocal chosenDataset, plot1, scatter, canvas
        chosenDataset = pd.concat([chosenDataset, dataToAppend], ignore_index=True)
        scatter.set(
            offsets=chosenDataset[['x', 'y']].values.tolist(),
            array=chosenDataset['class'].values.tolist())
        plot1.redraw_in_frame()
        canvas.draw()
    canvas.mpl_connect('button_press_event', callbackOnCanvasClick)
    return canvas
    

def createRightColumn(container):
    rightColumn = ttk.Frame(container)
    createPlot(rightColumn)
    return rightColumn
