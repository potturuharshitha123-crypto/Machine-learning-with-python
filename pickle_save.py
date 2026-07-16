import pickle
from sklearn.linear_model import LogisticRegression

# Create model
model = LogisticRegression()

# Save model
pickle.dump(model, open("my_model.pkl", "wb"))

print("Model saved")