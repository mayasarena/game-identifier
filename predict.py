#predict the class of a given image

from tensorflow.keras.models import load_model 
from keras.preprocessing import image
import numpy as np

height = int(720/3)
width = int(1280/3)

#load image
image_path = 'lm2.jpg' #image path here
img = image.load_img(image_path, target_size = (height, width))
img = image.img_to_array(img)
img = img.reshape((1,) + img.shape)
img = img/255.

#load model
model = load_model('working-model.h5')

#get result
class_prob = model.predict(img, batch_size = 1)
np.set_printoptions(suppress = True, formatter = {'float_kind':'{:f}'.format})
array = np.array(class_prob)
print("\n\nProbabilities in order: BOTW, Luigi's Mansion, Mario Odyssey, Pokemon LG")
print(array)

classes = model.predict_classes(img, batch_size = 1)
class_num = classes[0]
print('What game is this from!?')
if class_num == 0:
    print('Breath of the Wild')
elif class_num == 1:
    print("Luigi's Mansion")
elif class_num == 2:
    print('Mario Odyssey')
elif class_num == 3:
    print("Pokemon Let's Go")



