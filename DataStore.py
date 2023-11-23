import pandas as pd

class ClassData:
    def __init__(self):
        self.value = 0.0
        self.colour = 'blue'
        self.shape = 'o'

class DataStore:
    def __init__(self):
        self.plotData = pd.DataFrame([], columns=['x', 'y', 'class'])
        self.classesData = []
        print('in DataStore __init__:', self, self.plotData, self.classesData)

    def setPlotData(self, plotData):
        print('in setPlotData:', plotData, type(plotData))
        print(plotData.columns)
        #if plotData is not pd.DataFrame:
            #raise Exception('set plotData must be a pandas DataFrame!')
        #TODO: also raise if wrong columns
        self.plotData = plotData

    def from2DArray(self, data2DArray):
        self.plotData = pd.DataFrame(data2DArray, columns=['x', 'y', 'class'])

    def appendPlotData(self, data2DArray):
        dataFrameToAppend = pd.DataFrame(data2DArray, columns=['x', 'y', 'class'])
        self.plotData = pd.concat([self.plotData, dataFrameToAppend], ignore_index=True)

    def appendPlotDataPoint(self, x, y, classValue):
        print('plot dataPoint:', 'x:', x, 'y:', y, 'class:', classValue)
        self.appendPlotData([[x, y, classValue]])

    def clearData(self):
        self.plotData = self.plotData[0:0]

    def getXValues(self):
        return self.plotData['x'].values.tolist()

    def getYValues(self):
        return self.plotData['y'].values.tolist()

    def getClassValues(self):
        return self.plotData['class'].values.tolist()

    def getXYValues(self):
        return self.plotData[['x', 'y']].values.tolist()
        


dataStore = DataStore()
