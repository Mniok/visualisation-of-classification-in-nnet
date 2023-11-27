import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class ClassField:
    def __init__(self, frame, name, color, marker):
        self.frame = frame
        self.name = name
        self.color = color
        self.marker = marker
        self.nameLabel = None
        self.axes = None
        self.patchCollection = None
        self.figureCanvas = None

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        self.nameLabel = ttk.Label(self.frame, text=name)
        self.nameLabel.grid(column=0, row=0, sticky=tk.NW)


        fig = Figure(figsize=(0.2, 0.2), dpi=100)
        self.axes = fig.add_subplot(1, 1, 1)  # 1x1 grid, place plot in index 1
        #axes.get_xaxis().set_visible(False)
        #axes.get_yaxis().set_visible(False)
        self.axes.set_axis_off()
        self.patchCollection = self.axes.scatter(x=[0], y=[0], color=self.color, marker=self.marker)
        self.figureCanvas = FigureCanvasTkAgg(fig, master=self.frame)
        self.figureCanvas.draw()
        self.figureCanvas.get_tk_widget().grid(column=1, row=0, sticky=tk.NE)

    def update(self):
        self.nameLabel.set(text=self.name)
        self.patchCollection.set(color=self.color, marker=self.marker)
        self.axes.redraw_in_frame()
        self.figureCanvas.draw()

def createClassField(container, name, color, marker):
    classField = ClassField(tk.Frame(container),
                            name,
                            color,
                            marker)
    #classField.frame.config(bg='#EEFFEE') # debug color
    return classField
