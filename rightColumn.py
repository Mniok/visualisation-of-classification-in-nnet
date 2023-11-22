import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

import pandas as pd
import matplotlib.pyplot as plt
from DataStore import dataStore

from plotComponent import createPlot

#def createTopBar(container):
#def createBottomBar(container):


def createRightColumn(container):
    rightColumn = ttk.Frame(container)
    createPlot(rightColumn)
    return rightColumn
