from tkinter import filedialog as fd
from tkinter.messagebox import showwarning
import pandas as pd

from DataStore import dataStore
from plotComponent import plotComponent
from classChooser import classChoosersStore

FILETYPES = (
    ('Pliki CSV', '*.csv'),
    ('Wszystkie pliki', '*.*')
)

def selectFileForRead():
    filename = fd.askopenfilename(
        title='Wczytaj dane z pliku',
        initialdir='/',
        filetypes=FILETYPES)
    return filename

def selectFileForSave():
    filename = fd.asksaveasfilename(
        title='Zapisz dane do pliku',
        initialdir='/',
        filetypes=FILETYPES)
    return filename

def readFromFile():
    filename = selectFileForRead()
    if filename:
        dataStore.plotData = pd.read_csv(filename)
        highestClassRead = max(dataStore.plotData['class'].values.tolist())
        while len(classChoosersStore.classChoosers) <= highestClassRead:
            classChoosersStore.addNewClass()
        plotComponent.prepPatchCollectionsArray()
        plotComponent.refreshPlot()

def saveToFile(dataToSave):
    if not isinstance(dataToSave, pd.DataFrame):
        raise Exception('Incorrect data format')
    if len(dataToSave) < 1:
        showwarning('Uwaga', 'Brak danych do zapisania')
        raise Exception('No data to save')
    filename = selectFileForSave()
    if filename:
        if filename[-4:] != '.csv':
            filename += '.csv'
        dataToSave.to_csv(filename)

