#loading the dataset
from sklearn.datasets import load_iris
df = load_iris()
print(df)
#creating the dataframe
from sklearn.datasets import load_iris
import pandas as pd
iris = load_iris()
df = pd.DataFrame(iris.data, columns = iris.feature_names)
df['target'] = iris.target
print(df.head(10))
#splitting the data
from sklearn.datasets import load_iris
iris = load_iris()
x = iris.data
y = iris.target
print(x[:5])
print(y[:5])
#about the dataset
from sklearn.datasets import load_iris

iris = load_iris()

print("Feature Names:", iris.feature_names)
print("Target Names:", iris.target_names)
print("Shape:", iris.data.shape)
print("Description:")
print(iris.DESCR)
#using the random forest getting the predection
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
iris = load_iris()
x = iris.data
y = iris.target
x_test,x_train,y_test,y_train = train_test_split(x, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(random_state = 42)
model.fit(x_train,y_train)
y_predict = model.predict(x_test)
accuracy = accuracy_score(y_test, y_predict)
print("Accuracy:", accuracy)