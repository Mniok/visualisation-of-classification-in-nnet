from sklearn.neural_network import MLPClassifier
import pandas as pd
import matplotlib.pyplot as plt
from createPredictionDataArray import createPredictionDataArray
from DataStore import dataStore
from ModelStore import modelStore

from timeit import default_timer as timer

def fitAndPredict():
    if len(dataStore.plotData) < 1:
        raise Exception('No data!')
    modelStore.updateModel()
    print('in fitAndPredict:', dataStore.plotData)
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

    plot = predictionsDFrame.plot.scatter(
        x=0, y=1, c=2, cmap='Pastel1', marker=',', s=1,  #',' - pixel, s(size)=1
        xlim=(dataStore.plotDimensions.xmin, dataStore.plotDimensions.xmax),
        ylim=(dataStore.plotDimensions.ymin, dataStore.plotDimensions.ymax))
    plot.scatter(
        x=dataStore.plotData['x'].values.tolist(),
        y=dataStore.plotData['y'].values.tolist(),
        c=dataStore.plotData['class'].values.tolist(),
        cmap='gist_rainbow')
    plt.show()
