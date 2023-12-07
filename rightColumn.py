import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from createInputs import createTopBar, createBottomBar

import pandas as pd
import matplotlib.pyplot as plt
from DataStore import dataStore

from plotComponent import createPlot

def createRightColumn(container):
    rightColumn = tk.Frame(container)

    topInputsBar = createTopBar(rightColumn)
    topInputsBar.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=False)
    mainPlot = createPlot(rightColumn)
    mainPlot.pack(anchor=tk.CENTER, expand=True)
    bottomInputsBar = createBottomBar(rightColumn)
    bottomInputsBar.pack(side=tk.BOTTOM, anchor=tk.S, fill=tk.X, expand=False)
    return rightColumn
