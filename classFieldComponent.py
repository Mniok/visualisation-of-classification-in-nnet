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
        self.figureCanvas = None

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        # create label
        self.nameLabel = ttk.Label(self.frame, text=name)
        self.nameLabel.grid(column=0, row=0, sticky=tk.NW)

        # create mini plot to showcase marker
        fig = Figure(figsize=(0.2, 0.2), dpi=100)
        self.axes = fig.add_subplot(1, 1, 1)  # 1x1 grid, place plot in index 1
        self.figureCanvas = FigureCanvasTkAgg(fig, master=self.frame)
        self.update()
        self.figureCanvas.get_tk_widget().grid(column=1, row=0, sticky=tk.NE)

        # create context menu
        def createContextMenu():
            def setNameCallback():
                self.name = 'abcd'
                self.update()

            def setColorCallback():
                self.color = 'red'
                self.update()

            def setMarkerCallback():
                self.marker = '+'
                self.update()

            nonlocal self
            m = tk.Menu(self.frame, tearoff=0)
            m.add_command(label="Zmień nazwę", command=setNameCallback)
            m.add_command(label="Zmień kolor", command=setColorCallback)
            m.add_command(label="Zmień znacznik", command=setMarkerCallback)
            ## TODO? duplicate?
            m.add_separator()
            m.add_command(label="Usuń klasę")
            return m
        contextMenu = createContextMenu()

        # callback for opening context menu
        def openContextMenu(event):
            nonlocal contextMenu
            try:
                contextMenu.tk_popup(event.x_root, event.y_root)
            finally:
                contextMenu.grab_release()

        # bind callback to right click
        self.frame.bind("<Button-3>", openContextMenu)
        self.nameLabel.bind("<Button-3>", openContextMenu)
        self.figureCanvas.get_tk_widget().bind('<Button-3>', openContextMenu)

    def update(self):
        self.nameLabel.config(text=self.name)

        self.axes.clear()
        self.axes.set_axis_off()
        self.axes.scatter(
            x=[0], y=[0],
            color=self.color,
            marker=self.marker) # cannot neatly change marker shape without redrawing
        self.figureCanvas.draw()


def createClassField(container, name, color, marker):
    classField = ClassField(tk.Frame(container),
                            name,
                            color,
                            marker)
    #classField.frame.config(bg='#EEFFEE') # debug color
    return classField
