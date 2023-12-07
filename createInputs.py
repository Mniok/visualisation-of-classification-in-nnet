import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import math
from functools import partial

import pandas as pd
import matplotlib.pyplot as plt
from DataStore import dataStore
from ModelStore import modelStore

from plotComponent import plotComponent

def createTopBar(container):
    topBarFrame = tk.Frame(container)
    def updateSolverCallback(value):
        modelStore.solver = value
    def updateActivationFunctionCallback(value):
        modelStore.activation = value
    def updateHiddenLayer(n, value):
        modelStore.hidden_layer_sizes[n] = int(math.floor(value))

    # solver
    solvers = ['lbfgs', 'sgd', 'adam']
    solverDropdown = createDropdown(topBarFrame,
                                    labelText="Optymizer:",
                                    optionsList=solvers,
                                    startingValue='adam',
                                    valueChangedCallback=updateSolverCallback)

    # activation function
    activationFunctions = ['identity', 'logistic', 'tanh', 'relu']
    activationDropdown = createDropdown(topBarFrame,
                                    labelText="Funkcja aktywacji:",
                                    optionsList=activationFunctions,
                                    startingValue='relu',
                                    valueChangedCallback=updateActivationFunctionCallback)

    # hidden layer sizes:
    layer1Size = createNumberInput(
        topBarFrame,
        "Warstwy ukryte:",
        modelStore.hidden_layer_sizes[0],
        partial(updateHiddenLayer, 0))
    layer2Size = createNumberInput(
        topBarFrame,
        "",
        modelStore.hidden_layer_sizes[1],
        partial(updateHiddenLayer, 1))
    layer3Size = createNumberInput(
        topBarFrame,
        "",
        modelStore.hidden_layer_sizes[2],
        partial(updateHiddenLayer, 2))
    layer4Size = createNumberInput(
        topBarFrame,
        "",
        modelStore.hidden_layer_sizes[3],
        partial(updateHiddenLayer, 3))

    return topBarFrame

def createBottomBar(container):
    bottomBarFrame = tk.Frame(container)

    createPlotDimensionsInputs(bottomBarFrame)

    return bottomBarFrame

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
        try:
            valueChangedCallback(float(entryValue.get()))
        except ValueError:
            if (
                entryValue.get() is None
                or not entryValue.get()
                or entryValue.get().isspace()
            ):
                entryValue.set('0')

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