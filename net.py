#neural network using keras

from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import ModelCheckpoint
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import matplotlib.pyplot as plt
import cv2
from tqdm import tqdm
import os
import random

height = int(720/3)
width = int(1280/3)

#generating all data
datagen = ImageDataGenerator(rescale=1./255)

train_generator = datagen.flow_from_directory('data/train', target_size = (height, width), batch_size = 25, class_mode = 'categorical', shuffle = True)

val_generator = datagen.flow_from_directory('data/val', target_size = (height, width), batch_size = 25, class_mode = 'categorical', shuffle = True)

test_generator = datagen.flow_from_directory('data/test', target_size = (height, width), batch_size = 25, class_mode = 'categorical', shuffle = False)

#creating the model
model = Sequential()
model.add(Conv2D(filters = 64, kernel_size = 2, padding = 'same', activation = 'relu', input_shape = (height, width, 3)))
model.add(MaxPooling2D(pool_size = 2))
model.add(Flatten())
model.add(Dense(4, activation = 'softmax'))
model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

#model checkpoint
checkpoint = ModelCheckpoint('model{epoch:02d}.h5', period = 1)

#generate the model
model.fit_generator(train_generator, steps_per_epoch = 320, epochs = 30, callbacks = [checkpoint], validation_data = val_generator, validation_steps = 40, workers = 1, use_multiprocessing = False)

#print scores
score = model.evaluate_generator(generator = test_generator, steps = 40)
print('acc:', score[1])


#save model
model.save('final_model.h5')

#to load model:
#model = load.model('final_model.h5')
