
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from collections import Counter

# Load Iris dataset
iris = load_iris()
X, y = iris.data, iris.target
names = iris.target_names

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

# KNN prediction
predict = lambda X: np.array([
    Counter(
        y_train[
            np.argsort([
                np.linalg.norm(x - x_train)
                for x_train in X_train
            ])[:3]
        ]
    ).most_common(1)[0][0]
    for x in X
])

# Predict test data
y_pred = predict(X_test)

# Print results
print(f'Accuracy: {np.mean(y_pred == y_test):.4f}')
print("Predictions:", names[y_pred])

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(
    y_test, y_pred, target_names=names
))
