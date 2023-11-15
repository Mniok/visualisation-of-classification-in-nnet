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

plot = corners80.plot.scatter(x='x', y='y', c='class')
plot = corners1000.plot.scatter(x='x', y='y', c='class')
plt.show()
