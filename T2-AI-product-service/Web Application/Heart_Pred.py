# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 22:04:02 2024

@author: Pavan
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle


loadedmodel = pickle.load(open('C:/Users\Pavan/Downloads/Feynn_P3/train_new_mod.sav', 'rb'))



input_data = (1,0,1,28,1,0,0,0,0,1,0,2,0,0,1,1,11)
# Convert the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# Reshape the numpy array as we are predicting for only one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

# Predictions using logistic regression
lr_prediction = loadedmodel.predict(input_data_reshaped)

# Print predictions
print("Result =", lr_prediction)

# Interpret predictions
if lr_prediction[0] == 0:
    print('The person does not have heart disease.')
else:
    print('Logistic Regression: The person has heart disease.')
