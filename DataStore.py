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


dataStore = DataStore()
print(dataStore)
dataStore.setPlotData(pd.DataFrame([[1,2,3]], columns=['x', 'y', 'class']))
print(dataStore, dataStore.plotData, dataStore.classesData)
classData = ClassData()
print(classData)


dataStore.plotData = pd.DataFrame([[1,2,3], [4, 5, 4]], columns=['x', 'y', 'class'])
print(dataStore.plotData)


baseDir = "C:\\Users\\Stopy\\Documents\\GitHub\\visualisation-of-classification-in-nnet\\datasets\\"
dataStore.plotData = pd.read_csv(baseDir + "corners_1000_commas.csv")
print(dataStore.plotData, len(dataStore.plotData))
