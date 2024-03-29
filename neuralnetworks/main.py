import pandas as pd
import numpy as np

from helpers.loss_functions.loss import CrossEntropy
from core.model.model import Model
from helpers.activation_functions.activation import Softmax
from core.layer.layer import Dense


# prepare data
df = pd.read_csv("data/seeds_dataset.csv")
X_train = []
y_train = []
for idx in range(len(df)):
    X_train.append(np.asarray(df.loc[idx][1:]).reshape(-1,1))
    y_train.append(np.asarray([1,0] if df.loc[idx][0] == 1 else [0,1]).reshape(-1,1))

# create a model
model = Model(loss=CrossEntropy())
model.add(Dense(input_size=len(X_train[0]), output_size=3))
model.add(Dense(input_size=3, output_size=5))
model.add(Dense(input_size=5, output_size=len(y_train[0]), activation=Softmax()))

# train the model
model.train(X_train, y_train)