"""
Lasso Regression on the Diabetes Dataset
----------------------------------------
This program trains a Lasso Regression model using the
Scikit-learn Diabetes dataset and evaluates it using
Mean Squared Error (MSE).
"""

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error

# Load the dataset
data = load_diabetes()
X = data.data
y = data.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train the Lasso Regression model
model = Lasso(alpha=0.1)
model.fit(X_train, y_train)

# Predict on the test data
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)

print("Lasso Regression")
print("-----------------")
print("Mean Squared Error:", mse)