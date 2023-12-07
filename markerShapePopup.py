import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)

def askMarkerShape():
    top = tk.Toplevel() # use Toplevel() instead of Tk()
    returnValue = ''

    def highlightCallback(event):
        event.canvas.figure.patch.set_facecolor('yellow')
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
        fig.canvas.mpl_connect('button_press_event', lambda event: selectMarkerCallback(marker))

    tk.Label(top, text='Wybierz nowy kształt znacznika:').pack()

    markers2DList = [['o', '.', 's', '8'],
                    ['v', '^', '<', '>'],
                    ['p', '*', 'h', 'H'],
                    ['+', 'P', 'x', 'X'],
                    ['D', 'd', 8, 9]]
    for markersRow in markers2DList:
        row = tk.Frame(top)
        for marker in markersRow:
            drawMarker(row, marker)
        row.pack(side=tk.TOP, fill=tk.Y, expand=True)

    top.grab_set()
    top.wait_window(top)  # await window being destroyed (on marker shape selected)
    return returnValue
