# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 21:45:50 2017

@author: jacob
"""

from __future__ import division, print_function, absolute_import

import numpy as np

import tflearn
from tflearn.data_utils import load_csv, pad_sequences

def split_training_testing(X, y):
    # split the data into training and testing for hold-out testing    
    n_rows, n_features = np.shape(X)
        
    train_size = int(n_rows*0.8)
       
    X_train = X[0:train_size]
    y_train = y[0:train_size,:]
        
    X_test = X[train_size:n_rows]
    y_test = y[train_size:n_rows,:]
          
    return (X_train, y_train, X_test, y_test)

X, Y = load_csv('/Users/jacob/Desktop/Python/Guangxi Market/trimed_data.txt',\
                target_column=1, has_header=True, categorical_labels=True, n_classes=25)
trainX, trainY, testX, testY = split_training_testing(X, Y)

# Data preprocessing
# Sequence padding
trainX = pad_sequences(trainX, dtype='int32', maxlen=3, value=0.0)
testX = pad_sequences(testX, dtype='int32', maxlen=3, value=0.0)

# Network building
net = tflearn.input_data([None, 3])
net = tflearn.embedding(net, input_dim=49455, output_dim=128)
net = tflearn.lstm(net, 128, dropout=0.5)
net = tflearn.fully_connected(net, 25, activation='softmax')
net = tflearn.regression(net, optimizer='adam', learning_rate=0.001,
                         loss='categorical_crossentropy')

# Training
model = tflearn.DNN(net)
model.fit(trainX, trainY, validation_set=(testX, testY), show_metric=True, n_epoch=5)
model.save('/Users/jacob/Desktop/Python/Guangxi Market/model_1')

accuracy = model.evaluate(testX, testY)