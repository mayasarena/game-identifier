#test model with existing model

from tensorflow.keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator

height = int(720/3)
width = int(1280/3)

#generate dataset
datagen = ImageDataGenerator(rescale=1./255)

test_generator = datagen.flow_from_directory('data/test', target_size = (height, width), batch_size = 25, class_mode = 'categorical', shuffle = False)

#load model
model = load_model('working-model.h5')

#get score
score = model.evaluate_generator(generator = test_generator, steps = 40)
print('acc:', score[1]) 
