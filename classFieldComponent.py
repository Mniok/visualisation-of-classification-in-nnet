import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter.colorchooser import askcolor
from tkinter import simpledialog

def askComboValue(*values):
    top = tk.Toplevel() # use Toplevel() instead of Tk()
    returnValue = ''

    def highlightCallback(event):
        event.canvas.figure.patch.set_facecolor('red')
        event.canvas.draw()

    def unhighlightCallback(event):
        event.canvas.figure.patch.set_facecolor('white')
        event.canvas.draw()

    def selectMarkerCallback(marker):
        nonlocal returnValue
        returnValue = marker
        top.destroy()


    def drawMarker(container, marker):
        fig = Figure(figsize=(0.2, 0.2), dpi=100)
        axes = fig.add_subplot(1, 1, 1)  # 1x1 grid, place plot in index 1
        figureCanvas = FigureCanvasTkAgg(fig, master=container)
        axes.set_axis_off()
        axes.scatter(
            x=[0], y=[0],
            color='black',
            marker=marker)
        figureCanvas.draw()
        figureCanvas.get_tk_widget().pack(side=tk.LEFT)

        # callbacks:
        fig.canvas.mpl_connect('figure_enter_event', highlightCallback)
        fig.canvas.mpl_connect('figure_leave_event', unhighlightCallback)
        fig.canvas.mpl_connect('button_press_event', lambda *args: selectMarkerCallback(marker))

    # from https://stackoverflow.com/questions/62327504/how-to-create-a-simpledialog-like-window-with-a-combo-with-tkinter
    tk.Label(top, text='Select your value').pack()
    box_value = tk.StringVar()
    #combo = ttk.Combobox(top, textvariable=box_value, values=values)
    #combo.pack()
    #combo.bind('<<ComboboxSelected>>', lambda _: top.destroy())
    # ___
    markers2DList = [['o', '.', ',', '+'],
                   ['o', '.', ',', '+'],
                   ['o', '.', ',', '+'],
                   ['o', '+', '+', '+', 'o'],
                   ['.', ',', '.'],
                   ['.', '+', 'o', ',']]
    # ___
    for markersRow in markers2DList:
        row = tk.Frame(top)
        for marker in markersRow:
            drawMarker(row, marker)
        row.pack(side=tk.TOP, fill=tk.Y, expand=True)
    # ___
    top.grab_set()
    top.wait_window(top)  # wait for itself destroyed, so like a modal dialog
    #return box_value.get()
    return returnValue

def testCombobox():
    result = askComboValue('o', '+', '-')
    print(result)
    return result

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
                newMarker = testCombobox()
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
