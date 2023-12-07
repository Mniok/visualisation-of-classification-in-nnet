from sklearn.neural_network import MLPClassifier
import pandas as pd
import matplotlib.pyplot as plt
from createPredictionDataArray import createPredictionDataArray
from DataStore import dataStore
from ModelStore import modelStore
from classChooser import classChoosersStore
from sklearn.metrics import accuracy_score

from timeit import default_timer as timer

from matplotlib import colors
from matplotlib.colors import ListedColormap
def constructPredictionsColormap():
    def getPastellizedColor(color):
        colorValue = colors.to_rgb(color)
        hsv = colors.rgb_to_hsv(colorValue)
        pastelHsv = (hsv[0], hsv[1]*0.15, hsv[2]*0.8)
        return colors.hsv_to_rgb(pastelHsv)
    colorsList = [getPastellizedColor(classChooser.color) for classChooser in classChoosersStore.classChoosers]
    return ListedColormap(colorsList, name="predictions_colormap")

def fitAndPredict():
    if len(dataStore.plotData) < 1:
        raise Exception('No data!')
    modelStore.updateModel()
    coordsData = dataStore.plotData[['x', 'y']].values.tolist()
    classesTargets = dataStore.plotData['class'].values.tolist()
    modelStore.model.fit(coordsData, classesTargets)

    dataForPrediction = createPredictionDataArray(startX=dataStore.plotDimensions.xmin,
                                                  endX=dataStore.plotDimensions.xmax,
                                                  startY=dataStore.plotDimensions.ymin,
                                                  endY=dataStore.plotDimensions.ymax,
                                                  width=800)
    predictions = modelStore.model.predict(dataForPrediction)
    predictionsDFrame = pd.DataFrame(dataForPrediction, columns=['x', 'y'])
    predictionsDFrame['predicted class'] = predictions

    # background - predictions chart
    plot = predictionsDFrame.plot.scatter(
        x=0, y=1, c=2,  # columns from dataframe
        cmap=constructPredictionsColormap(),
        marker=',', s=1,  # ',' - pixel, s(size)=1
        xlim=(dataStore.plotDimensions.xmin, dataStore.plotDimensions.xmax),
        ylim=(dataStore.plotDimensions.ymin, dataStore.plotDimensions.ymax))
    # foreground - given data points
    for i in range(0, len(classChoosersStore.classChoosers)):
        filteredPlotData = dataStore.plotData[dataStore.plotData['class'] == i]
        if len(filteredPlotData):
            plot.scatter(
                x=filteredPlotData['x'].values.tolist(),
                y=filteredPlotData['y'].values.tolist(),
                color=classChoosersStore.getClassData(i)['color'],
                marker=classChoosersStore.getClassData(i)['marker'])

    #compute accuracy score:
    testData = dataStore.plotData # TODO: consider separating test data and training data, but probably not possible here since all given data has to be plotted, ergo, has to be training data
    predictionsForSameValuesAsData = modelStore.model.predict(testData[['x', 'y']].values.tolist())
    accuracyScore = accuracy_score(testData['class'].values.tolist(), predictionsForSameValuesAsData)
    print('accuracy:', accuracyScore)
    plt.show()
