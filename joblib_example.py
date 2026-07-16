from joblib import dump, load
from sklearn.linear_model import LogisticRegression

# Create model
model = LogisticRegression()

# Save
dump(model, "logistic.joblib")

# Load
loaded = load("logistic.joblib")

print("Joblib save and load successful")