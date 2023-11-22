import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

import pandas as pd
import matplotlib.pyplot as plt
#import dataStore from DataStore
from DataStore import dataStore

#def createTopBar(container):
#def createBottomBar(container):

def createPlot(container):
    fig = Figure(figsize=(5, 5), dpi=100)
    plot1 = fig.add_subplot(1, 1, 1) # 1x1 grid, place plot in index 1
    scatter = plot1.scatter(
        x = dataStore.plotData['x'].values.tolist(),
        y = dataStore.plotData['y'].values.tolist(),
        c = dataStore.plotData['class'].values.tolist())
    canvas = FigureCanvasTkAgg(fig, master=container)
    canvas.draw()
    canvas.get_tk_widget().pack()

    def callbackOnCanvasClick(event):
        if event.xdata is None or event.ydata is None: return
        #dataStore.plotData.appendPlotDataPoint(event.xdata, event.ydata, 1)
        #dataToAppend = pd.DataFrame([[event.xdata, event.ydata, 1]], columns=['x', 'y', 'class'])
        nonlocal plot1, scatter, canvas
        #chosenDataset = pd.concat([chosenDataset, dataToAppend], ignore_index=True)
        dataStore.appendPlotDataPoint(event.xdata, event.ydata, 1);
        print(dataStore.plotData);
        scatter.set(
            offsets=dataStore.plotData[['x', 'y']].values.tolist(),
            array=dataStore.plotData['class'].values.tolist())
        plot1.redraw_in_frame()
        canvas.draw()
    canvas.mpl_connect('button_press_event', callbackOnCanvasClick)
    return canvas
    

def createRightColumn(container):
    rightColumn = ttk.Frame(container)
    createPlot(rightColumn)
    return rightColumn
