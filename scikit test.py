from sklearn.neural_network import MLPClassifier
import pandas as pd
import matplotlib.pyplot as plt
from createPredictionDataArray import createPredictionDataArray
from DataStore import dataStore

from timeit import default_timer as timer


print('started...')

t1 = timer() #!
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(8, 4), random_state=1, max_iter=2000)
t2 = timer() #!
print('setup classifier time:', t2 - t1) #!
#print(out)

# _____________

#print(dataStore.plotData) #!
#print(type(dataStore.plotData)) # expected DataFrame

tplot1 = timer() #!
#plot1 = corners80.plot.scatter(x='x', y='y', c='class')
#plot2 = corners1000.plot.scatter(x='x', y='y', c='class')
plot = dataStore.plotData.plot.scatter(x='x', y='y', c='class')
tplot2 = timer() #!
print('plot1 plot2 time:', tplot2 - tplot1) #!
# plt.show()

tlist1 = timer() #!
coordsData = dataStore.plotData[['x', 'y']].values.tolist()
classesTargets = dataStore.plotData['class'].values.tolist()
tlist2 = timer() #!
print('time values.tolist()', tlist2 - tlist1)
print(coordsData)
print(classesTargets)

dataForPrediction = createPredictionDataArray(-10, 10, width=800)
print(dataForPrediction[1:10])
print('length:', len(dataForPrediction))



t5 = timer() #!
clf.fit(coordsData, classesTargets)
t6 = timer() #!
predictions = clf.predict(dataForPrediction)
t7 = timer() #!
print('fit time:', t6 - t5) #!
print('predict time:', t7 - t6) #!


print(predictions[1:10], len(predictions))


predictionsDFrame = pd.DataFrame(dataForPrediction, columns=['x', 'y'])
predictionsDFrame['predicted class'] = predictions

print(predictionsDFrame)
predPlot = predictionsDFrame.plot.scatter(x=0, y=1, c=2)

#! ---
predictionPlotWithTrueDataOnTop = predictionsDFrame.plot.scatter(x=0, y=1, c=2, cmap='Pastel1', marker=',') #',' - pixel
predictionPlotWithTrueDataOnTop.scatter(
    x=dataStore.plotData['x'].values.tolist(),
    y=dataStore.plotData['y'].values.tolist(),
    c=dataStore.plotData['class'].values.tolist(),
    cmap='gist_rainbow')
#! ---

tend = timer() #!
print('time of everything:', tend - t1) #1
plt.show()

