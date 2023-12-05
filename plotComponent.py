import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

import pandas as pd
import matplotlib.pyplot as plt
from DataStore import dataStore
from classChooser import classChoosersStore

class PlotStore:
    def __init__(self):
        self.axes = None
        self.patchCollection = None
        self.figureCanvas = None
        self.created = False

    def refreshPlot(self):
        if not self.created:
            raise Exception('Plot has not been created yet!')
        if len(dataStore.plotData) > 0:
            self.patchCollection.set(
                offsets=dataStore.plotData[['x', 'y']].values.tolist(),
                array=dataStore.plotData['class'].values.tolist(),
                visible=True)
        else:
            self.patchCollection.set_visible(False) # trying to set empty data throws errors, hiding patchCollection instead
        self.axes.redraw_in_frame()
        self.figureCanvas.draw()

    def clearPlot(self):
        dataStore.clearData()
        self.refreshPlot()

    def updatePlotXYDimensions(self, refresh=True):
        self.axes.set_xlim(dataStore.plotDimensions.xmin, dataStore.plotDimensions.xmax)
        self.axes.set_ylim(dataStore.plotDimensions.ymin, dataStore.plotDimensions.ymax)
        if refresh: self.refreshPlot()

plotComponent = PlotStore()

def createPlot(container):
    fig = Figure(figsize=(5, 5), dpi=100)
    plotComponent.axes = fig.add_subplot(1, 1, 1) # 1x1 grid, place plot in index 1
    plotComponent.patchCollection = plotComponent.axes.scatter(
        x = dataStore.plotData['x'].values.tolist(),
        y = dataStore.plotData['y'].values.tolist(),
        c = dataStore.plotData['class'].values.tolist())
    plotComponent.figureCanvas = FigureCanvasTkAgg(fig, master=container)
    plotComponent.figureCanvas.draw()
    plotComponent.figureCanvas.get_tk_widget().pack()

    plotComponent.updatePlotXYDimensions(refresh=False)

    def callbackOnCanvasClick(event):
        if event.xdata is None or event.ydata is None: return
        dataStore.appendPlotDataPoint(event.xdata, event.ydata, 1); # TODO: currently selected class
        plotComponent.refreshPlot()
    plotComponent.figureCanvas.mpl_connect('button_press_event', callbackOnCanvasClick)

    plotComponent.created = True
    return plotComponent.figureCanvas
