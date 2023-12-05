import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter.colorchooser import askcolor
from tkinter import simpledialog
from markerShapePopup import askMarkerShape

class ClassField:
    def __init__(self, frame, name, color, marker, deleteHandler, selectHandler):
        self.frame = frame
        self.name = name
        self.color = color
        self.marker = marker
        self.deleteHandler = deleteHandler
        self.selectHandler = selectHandler
        self.nameLabel = None
        self.axes = None
        self.figureCanvas = None
        self.isSelected = False

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        # create label
        self.nameLabel = tk.Label(self.frame, text=name)
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
                newName = simpledialog.askstring(
                    title=f'Zmień nazwę klasy \"{self.name}\"',
                    prompt=f'Nowa nazwa klasy \"{self.name}\":')
                if newName:
                    self.name = newName
                    self.update()

            def setColorCallback():
                newColor = askcolor(title=f'Zmień kolor klasy "{self.name}"')[1] # 2nd element of tuple is hex value
                if newColor:
                    self.color = newColor
                    self.update()

            def setMarkerCallback():
                newMarker = askMarkerShape()
                if newMarker:
                    self.marker = newMarker
                    self.update()

            nonlocal self
            m = tk.Menu(self.frame, tearoff=0)
            m.add_command(label="Zmień nazwę", command=setNameCallback)
            m.add_command(label="Zmień kolor", command=setColorCallback)
            m.add_command(label="Zmień znacznik", command=setMarkerCallback)
            ## TODO? duplicate?
            m.add_separator()
            m.add_command(label="Usuń klasę", command=self.delete)
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

        # bind select callback to left click
        self.frame.bind("<Button-1>", lambda event: self.selectHandler(id(self)))
        self.nameLabel.bind("<Button-1>", lambda event: self.selectHandler(id(self)))
        self.figureCanvas.get_tk_widget().bind('<Button-1>', lambda event: self.selectHandler(id(self)))

    def update(self):
        self.nameLabel.config(text=self.name)

        self.axes.clear()
        self.axes.set_axis_off()
        self.axes.scatter(
            x=[0], y=[0],
            color=self.color,
            marker=self.marker) # cannot neatly change marker shape without redrawing
        self.figureCanvas.draw()
        self.updateSelectedStyle()

    def delete(self):
        self.deleteHandler(id(self))
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.frame.destroy()

    def updateSelectedStyle(self):
        if self.isSelected:
            self.frame.config(bg='#FFFFBB')
            self.frame.config(highlightthickness=1)
            self.frame.config(borderwidth=0) # basically padding
            self.frame.config(highlightbackground='black')  # visual border
            self.nameLabel.config(bg='#FFFFBB')
        else:
            self.frame.config(bg='#D9D9D9') # default background color on windows
            self.frame.config(highlightthickness=0)
            self.frame.config(borderwidth=1) # hiding highlight, using border instead - fixes bug with last class always having highlight
            self.frame.config(highlightbackground='#D9D9D9')
            self.nameLabel.config(bg='#D9D9D9')

def createClassField(container, name, color, marker, deleteHandler, selectHandler):
    classField = ClassField(tk.Frame(container),
                            name,
                            color,
                            marker,
                            deleteHandler,
                            selectHandler)
    #classField.frame.config(bg='#EEFFEE') # debug color
    return classField
