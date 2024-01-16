from sklearn.neural_network import MLPClassifier

class ModelStore:
    def __init__(self):
        self.model = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(8, 4), random_state=1, max_iter=2000)
        
        self.solver='adam'
        self.activation='relu'
        self.hidden_layer_sizes=[8, 4, 0, 0]
        self.random_state=1
        self.max_iter=2000

        self.updateModel()

    def updateModel(self):
        self.model = MLPClassifier(
            solver=self.solver,
            activation=self.activation,
            hidden_layer_sizes=tuple([val for val in self.hidden_layer_sizes if val]), # eg. [8, 4, 0, 0] => (8, 4)
            random_state=self.random_state,
            max_iter=self.max_iter)


modelStore = ModelStore()
