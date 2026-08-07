### deep learning problems
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
x = np.array([[1,0],[1,1],[0,1],[0,0]])
y = np.array([1,1,1,0]).reshape(-1, 1) # Reshape y to be 2D
model = Sequential()
model.add(Dense(8,activation = 'relu'))
model.add(Dense(1,activation = 'sigmoid')) # Changed to 1 neuron with sigmoid for binary classification
model.compile(optimizer = 'adam',loss = 'binary_crossentropy',metrics = ['accuracy'])
model.fit(x,y,epochs = 100, verbose = 0)
prediction = model.predict(x)
print(prediction)