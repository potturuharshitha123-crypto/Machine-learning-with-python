from sklearn.metrics import confusion_matrix

# Actual values
y_true = [1, 0, 1, 1, 0, 1, 0, 0]

# Predicted values
y_pred = [1, 0, 1, 0, 0, 1, 1, 0]

# Create confusion matrix
cm = confusion_matrix(y_true, y_pred)

# Print the confusion matrix
print("Confusion Matrix:")
print(cm)