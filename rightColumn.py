import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from createInputs import createTopBar, createBottomBar

import pandas as pd
import matplotlib.pyplot as plt
from DataStore import dataStore

from plotComponent import createPlot

#def createTopBar(container):
    # hidden layer sizes:


#def createBottomBar(container):
    # zakres:
    # xlimLow, xlimHigh, ylimLow, ylimHigh

def createRightColumn(container):
    rightColumn = ttk.Frame(container)
    topInputsBar = createTopBar(rightColumn)
    mainPlot = createPlot(rightColumn)
    bottomInputsBar = createBottomBar(rightColumn)
    return rightColumn
