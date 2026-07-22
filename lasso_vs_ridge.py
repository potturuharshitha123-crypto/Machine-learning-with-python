"""
Comparison of Lasso and Ridge Regression
----------------------------------------
This program compares the performance of Lasso and Ridge
Regression models on the Diabetes dataset using
Mean Squared Error (MSE).
"""

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso, Ridge
from sklearn.metrics import mean_squared_error

# Load the dataset
data = load_diabetes()
X = data.data
y = data.target

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# Lasso Regression
# -----------------------------
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)

lasso_predictions = lasso.predict(X_test)
lasso_mse = mean_squared_error(y_test, lasso_predictions)

# -----------------------------
# Ridge Regression
# -----------------------------
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)

ridge_predictions = ridge.predict(X_test)
ridge_mse = mean_squared_error(y_test, ridge_predictions)

# Display results
print("Model Comparison")
print("----------------")
print("Lasso Regression MSE :", lasso_mse)
print("Ridge Regression MSE :", ridge_mse)

if lasso_mse < ridge_mse:
    print("\nLasso Regression performed better.")
elif ridge_mse < lasso_mse:
    print("\nRidge Regression performed better.")
else:
    print("\nBoth models performed equally.")