from sklearn.neural_network import MLPClassifier
import pandas as pd
import matplotlib.pyplot as plt
from createPredictionDataArray import createPredictionDataArray

from timeit import default_timer as timer


print('started...')

X = [[0., 0.], [1., 1.]]
y = [0, 1]

t1 = timer() #!
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(8, 4), random_state=1, max_iter=2000)
t2 = timer() #!
print('setup classifier time:', t2 - t1) #!
#clf.fit(X, y)
#out = clf.predict([[2., 2.], [-1., -2.]])
#print(out)

# _____________

baseDir = "C:\\Users\\Stopy\\Documents\\GitHub\\visualisation-of-classification-in-nnet\\datasets\\"

t3 = timer() #!
corners80 = pd.read_csv(baseDir + "corners_80_commas.csv")
corners1000 = pd.read_csv(baseDir + "corners_1000_commas.csv")
chosenDataset = corners1000
t4 = timer() #!
print('read csv time:', t4 - t3) #!
print(corners80)
print(type(corners80)) # expected DataFrame

tplot1 = timer() #!
plot1 = corners80.plot.scatter(x='x', y='y', c='class')
plot2 = corners1000.plot.scatter(x='x', y='y', c='class')
tplot2 = timer() #!
print('plot1 plot2 time:', tplot2 - tplot1) #!
# plt.show()

tlist1 = timer() #!
coordsData = chosenDataset[['x', 'y']].values.tolist()
classesTargets = chosenDataset['class'].values.tolist()
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
predictionPlotWithTrueDataOnTop = predictionsDFrame.plot.scatter(x=0, y=1, c=2, cmap='Pastel1')
predictionPlotWithTrueDataOnTop.scatter(x=chosenDataset['x'].values.tolist(), y=chosenDataset['y'].values.tolist(), c=chosenDataset['class'].values.tolist(), cmap='gist_rainbow')
#! ---

tend = timer() #!
print('time of everything:', tend - t1) #1
plt.show()

