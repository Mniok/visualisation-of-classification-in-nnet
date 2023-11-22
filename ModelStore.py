from sklearn.neural_network import MLPClassifier
import pandas as pd

class ModelStore:
    def __init__(self):
        self.model = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(8, 4), random_state=1, max_iter=2000)
        
        self.solver='adam'
        self.hidden_layer_sizes=(8, 4)
        self.random_state=1
        self.max_iter=2000

        print('in ModelStore __init__ before update:', self.model, self.random_state, self.max_iter)
        self.updateModel()
        print('in ModelStore __init__:', self.model, self.random_state)

    def updateModel(self):
        print('modelStore.updateModel')
        self.model = MLPClassifier(
            solver=self.solver,
            hidden_layer_sizes=self.hidden_layer_sizes,
            random_state=self.random_state,
            max_iter=self.max_iter)
        #TODO: switch by solver


modelStore = ModelStore()
