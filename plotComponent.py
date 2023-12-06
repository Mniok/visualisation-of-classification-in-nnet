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
        self.patchCollections = []
        self.figureCanvas = None
        self.created = False

    def prepPatchCollectionsArray(self):
        # prepare enough patchCollections for every class in classChoosers
        while len(self.patchCollections) < len(classChoosersStore.classChoosers):
            classData = classChoosersStore.classChoosers[len(self.patchCollections)]
            newPatchCollection = plotComponent.axes.scatter(
                x=[],
                y=[],
                color=classData.color,
                marker=classData.marker)
            self.patchCollections.append(newPatchCollection)

    def refreshPlot(self):
        if not self.created:
            raise Exception('Plot has not been created yet!')
        self.prepPatchCollectionsArray()
        for i in range(0, len(self.patchCollections)):
            filteredPlotData = dataStore.plotData[dataStore.plotData['class'] == i]
            if len(filteredPlotData) > 0:
                self.patchCollections[i].set(
                    offsets=filteredPlotData[['x', 'y']].values.tolist(),
                    visible=True)
            else:
                self.patchCollections[i].set_visible(False) # trying to set empty data throws errors, hiding patchCollection instead
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
    plotComponent.prepPatchCollectionsArray()
    plotComponent.figureCanvas = FigureCanvasTkAgg(fig, master=container)
    plotComponent.figureCanvas.draw()
    plotComponent.figureCanvas.get_tk_widget().pack()

    plotComponent.updatePlotXYDimensions(refresh=False)

    def callbackOnCanvasClick(event):
        if event.xdata is None or event.ydata is None: return
        selectedClassData = classChoosersStore.getSelectedClassData()
        dataStore.appendPlotDataPoint(event.xdata, event.ydata, selectedClassData['c'])
        plotComponent.refreshPlot()
    plotComponent.figureCanvas.mpl_connect('button_press_event', callbackOnCanvasClick)

    plotComponent.created = True
    return plotComponent.figureCanvas
