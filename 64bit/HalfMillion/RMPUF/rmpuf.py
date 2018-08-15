import numpy as np
import pandas as pd
from sklearn import cross_validation
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense,Dropout

import numpy
from sklearn import metrics
import pandas as pd
from keras.layers.advanced_activations import LeakyReLU, PReLU
from keras.layers import LeakyReLU
import keras_metrics
from sklearn.metrics import confusion_matrix


df1=pd.read_csv('../dataset/APUF_XOR_Challenge_Parity_64_500000.csv',header=None)
df2=pd.read_csv('rmpuf.csv',header=None)

# fix random seed for reproducibility
numpy.random.seed(42)

# split into input (X) and output (Y) variables
X = df1.iloc[:99999,:65]
Y = df2.iloc[:99999,22:23]
train_features, test_features, train_labels, test_labels = cross_validation.train_test_split(X, Y, test_size = 0.2, random_state = 42)
# create model
model = Sequential()

model.add(Dense(30,input_dim=65, activation='relu'))
model.add(Dense(30, activation='relu'))
model.add(Dense(30, activation='relu'))

model.add(Dense(1, activation='sigmoid'))

model.summary()

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy',keras_metrics.precision(), keras_metrics.recall()])
# Fit the model
results = model.fit(
 train_features, train_labels,
 epochs= 300,
 batch_size = 1000,
 validation_data = (test_features, test_labels)
)
# evaluate the model
scores = model.evaluate(test_features, test_labels)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
