# -*- coding: utf-8 -*-
"""DL_CNN_MNIST.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UUakT8CbqtPH8UyWub_s1-UsB4j-3KzY

https://blog.paperspace.com/intro-to-optimization-momentum-rmsprop-adam/
"""

import keras

#model.summary()

from keras.datasets import mnist
from keras.utils import to_categorical

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images.shape

train_images[0].shape

train_images[0]

train_labels[0]

train_images = train_images.reshape((60000, 28, 28, 1))

train_images.shape

test_labels[0]

train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28, 28, 1))
test_images = test_images.astype('float32') / 255

train_images[0]

train_labels[0]

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

train_labels[0]

print (train_labels.shape)





from keras import layers
from keras import models

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(16, (5,5), activation = "relu"))
model.add(layers.MaxPooling2D((2, 2)))



model.add(layers.Flatten())

model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=50, batch_size=64)

test_loss, test_acc = model.evaluate(test_images, test_labels)

test_images[0].shape

test_acc

model.layers

train_images[0].shape

type(train_images)

test_data = train_images[10].reshape(1,28,28,1)

test_data.shape

prediction = model.predict(test_data)

prediction

"""Set axis=-1 means, extract largest indices in each row. Here we have only one row."""

import numpy as np

y = np.argmax(prediction, axis=-1)

y

train_labels[10]

"""Code challenge 
https://medium.com/coinmonks/handwritten-digit-prediction-using-convolutional-neural-networks-in-tensorflow-with-keras-and-live-5ebddf46dc8
"""

test_images.shape

test_data = test_images

predictions = model.predict(test_data)

final_pred = np.argmax(predictions, axis=-1)

final_pred.shape

from sklearn import metrics

matrix = metrics.confusion_matrix(test_labels.argmax(axis=1), final_pred)