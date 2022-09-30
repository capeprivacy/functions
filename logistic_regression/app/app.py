import pandas as pd
import numpy as np
import copy

class LogisticRegression():
    def __init__(self):
        self.losses = []
        self.train_accuracies = []
    
    def accuracy_score(self, y_true, y_pred):
        correct = np.sum(y_true == y_pred)
        accuracy = correct/y_true.shape[0]
        return accuracy

    def fit(self, x, y, epochs):
        x = self._transform_x(x)
        y = self._transform_y(y)

        self.weights = np.zeros(x.shape[1])
        self.bias = 0

        for i in range(epochs):
            x_dot_weights = np.matmul(self.weights, x.transpose()) + self.bias
            pred = self._sigmoid(x_dot_weights)
            loss = self.compute_loss(y, pred)
            error_w, error_b = self.compute_gradients(x, y, pred)
            self.update_model_parameters(error_w, error_b)

            pred_to_class = [1 if p > 0.5 else 0 for p in pred]
            self.train_accuracies.append(self.accuracy_score(y, pred_to_class))
            self.losses.append(loss)

    def compute_loss(self, y_true, y_pred):
        # binary cross entropy
        y_zero_loss = y_true * np.log(y_pred + 1e-9)
        y_one_loss = (1-y_true) * np.log(1 - y_pred + 1e-9)
        return -np.mean(y_zero_loss + y_one_loss)

    def compute_gradients(self, x, y_true, y_pred):
        # derivative of binary cross entropy
        difference =  y_pred - y_true
        gradient_b = np.mean(difference)
        gradients_w = np.matmul(x.transpose(), difference)
        gradients_w = np.array([np.mean(grad) for grad in gradients_w])

        return gradients_w, gradient_b

    def update_model_parameters(self, error_w, error_b):
        self.weights = self.weights - 0.1 * error_w
        self.bias = self.bias - 0.1 * error_b

    def predict(self, x):
        x_dot_weights = np.matmul(x, self.weights.transpose()) + self.bias
        probabilities = self._sigmoid(x_dot_weights)
        return [1 if p > 0.5 else 0 for p in probabilities]

    def _sigmoid(self, x):
        return np.array([self._sigmoid_function(value) for value in x])

    def _sigmoid_function(self, x):
        if x >= 0:
            z = np.exp(-x)
            return 1 / (1 + z)
        else:
            z = np.exp(x)
            return z / (1 + z)

    def _transform_x(self, x):
        x = copy.deepcopy(x)
        return x.values

    def _transform_y(self, y):
        y = copy.deepcopy(y)
        return y.values.reshape(y.shape[0], 1)

def cape_handler(input_data):
    csv = input_data.decode("utf-8")
    csv = csv.replace('\\t', ',').replace('\\n', '\n')
    f = open('data.csv', 'w')
    f.write(csv)
    f.close()

    data = pd.read_csv('data.csv')
    data_size = data.shape[0]
    test_split = 0.33
    test_size = int(data_size * test_split)

    choices = np.arange(0, data_size)
    test = np.random.choice(choices, test_size, replace=False)
    train = np.delete(choices, test)

    test_set = data.iloc[test]
    train_set = data.iloc[train]

    column_names = list(data.columns.values)
    features = column_names[1:len(column_names)-1]

    y_train = train_set["target"]
    y_test = test_set["target"]
    X_train = train_set[features]
    X_test = test_set[features]

    lr = LogisticRegression()
    lr.fit(X_train, y_train, epochs=150)
    pred = lr.predict(X_test)

    accuracy = lr.accuracy_score(y_test, pred)
    
    # trained model
    model = {"accuracy": accuracy, "weights": lr.weights.tolist(), "bias": lr.bias.tolist()}
    
    return model