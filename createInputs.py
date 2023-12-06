import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

import pandas as pd
import matplotlib.pyplot as plt
from DataStore import dataStore
from ModelStore import modelStore

from plotComponent import plotComponent

def createTopBar(container):
    def updateSolverCallback(value):
        modelStore.solver = value

    # solver
    solvers = ['lbfgs', 'sgd', 'adam']
    solverDropdown = createDropdown(container,
                                    labelText="Optymizer:",
                                    optionsList=solvers,
                                    startingValue='adam',
                                    valueChangedCallback=updateSolverCallback)

    # hidden layer sizes:
    #hiddenLayerSizesLabel = ttk.Label(container, text="Rozmiary warstw ukrytych:")
    #hiddenLayerSizesLabel.pack(fill='x', expand=True)
    #layer1Size = ttk.Entry(container, textvariable=password, validate='all')
    #layer1Size.pack(fill='x', expand=True)

def createBottomBar(container):
    createPlotDimensionsInputs(container)

def createPlotDimensionsInputs(container):
    def updateXMinCallback(value):
        dataStore.plotDimensions.xmin = value
        plotComponent.updatePlotXYDimensions()
    def updateXMaxCallback(value):
        dataStore.plotDimensions.xmax = value
        plotComponent.updatePlotXYDimensions()
    def updateYMinCallback(value):
        dataStore.plotDimensions.ymin = value
        plotComponent.updatePlotXYDimensions()
    def updateYMaxCallback(value):
        dataStore.plotDimensions.ymax = value
        plotComponent.updatePlotXYDimensions()

    xminInput = createNumberInput(
        container,
        "Wymiary pola: x:",
        dataStore.plotDimensions.xmin,
        updateXMinCallback)
    xmaxInput = createNumberInput(
        container,
        "-",
        dataStore.plotDimensions.xmax,
        updateXMaxCallback)
    yminInput = createNumberInput(
        container,
        ", y:",
        dataStore.plotDimensions.ymin,
        updateYMinCallback)
    ymaxInput = createNumberInput(
        container,
        "-",
        dataStore.plotDimensions.ymax,
        updateYMaxCallback)

def createNumberInput(container, labelText, startingValue, valueChangedCallback):
    entryValue = tk.StringVar(value=startingValue)
    def callback(var, index, mode):
        valueChangedCallback(float(entryValue.get()))
    entryValue.trace_add('write', callback)

    frame = tk.Frame(container)
    label = ttk.Label(frame, text=labelText)
    label.pack(side='left', fill='x', expand=False)
    entry = tk.Entry(frame, textvariable=entryValue, width=8)
    entry.pack(side='left', fill='x', expand=False)

    frame.pack(side='left', fill='x', expand=False)
    return frame

def createDropdown(container, labelText, optionsList, valueChangedCallback, startingValue=None):
    entryValue = tk.StringVar(value=startingValue if startingValue is not None else optionsList[0])
    def callback(var, index, mode):
        valueChangedCallback(entryValue.get())
    entryValue.trace_add('write', callback)

    frame = tk.Frame(container)
    label = ttk.Label(frame, text=labelText)
    label.pack(side='left', fill='x', expand=False)
    dropdown = tk.OptionMenu(frame, entryValue, *optionsList)
    dropdown.config(width=8)
    dropdown.pack(side='left', fill='x', expand=False)

    frame.pack(side='left', fill='x', expand=False)
    return frame