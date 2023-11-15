from sklearn.neural_network import MLPClassifier
import pandas as pd
import matplotlib.pyplot as plt

print('started...')

X = [[0., 0.], [1., 1.]]
y = [0, 1]

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
#clf.fit(X, y)
#out = clf.predict([[2., 2.], [-1., -2.]])
#print(out)

# _____________

baseDir = "C:\\Users\\Stopy\\Documents\\GitHub\\visualisation-of-classification-in-nnet\\datasets\\"

corners80 = pd.read_csv(baseDir + "corners_80_commas.csv")
corners1000 = pd.read_csv(baseDir + "corners_1000_commas.csv")
print(corners80)
print(type(corners80)) # expected DataFrame

plot1 = corners80.plot.scatter(x='x', y='y', c='class')
plot2 = corners1000.plot.scatter(x='x', y='y', c='class')
# plt.show()


cornersCoordsData = corners80[['x', 'y']].values.tolist()
cornersClassesTargets = corners80['class'].values.tolist()
print(cornersCoordsData)
print(cornersClassesTargets)

dataForPrediction = []
step = 0.5
for i in range(int(-10*(1/step)), int(10*(1/step))+1):
    for j in range(int(-10*(1/step)), int(10*(1/step))+1):
        dataForPrediction.append([i*step, j*step]) # horrendously slow, replace
#print(dataForPrediction)
print(dataForPrediction[1:10])
print('length:', len(dataForPrediction))

        


clf.fit(cornersCoordsData, cornersClassesTargets)
predictions = clf.predict(dataForPrediction)

print(predictions[1:10], len(predictions))


predictionsDFrame = pd.DataFrame(dataForPrediction, columns=['x', 'y'])
predictionsDFrame['predicted class'] = predictions

print(predictionsDFrame)
predPlot = predictionsDFrame.plot.scatter(x=0, y=1, c=2)
plt.show()
