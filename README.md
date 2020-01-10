# Game Detector
<i>Game Detector</i> is an image classification model that detects which video game a given screenshot is from. The model was trained, validated, and tested using 10,000 screenshots from each video game. The four categories used were Breath of the Wild, Luigi's Mansion, Mario Odyssey, and Pokemon Let's Go. 

## How to use

To collect data, run `screenshot.py`, which is a program that collects screenshots from a video every n frames.
* Source video and <i>n</i> must be manually updated in code

To train, validate, and test the model, run `net.py`. This will save an updated model every <i>n</i> epochs. 

To test on an already existing model, run `test.py`.
* Source model must be manually updated in code

To predict the category of an image, run `predict.py`. 
* Desired image to predict and model must be updated in code. 
* If different categories are used, print statements should be manually updated as well.

## Results

`working-model.h5` is the current up-to-date model, which has about 99% accuracy. 
* Result images soon to come

### Future improvements

* Create a model with more categories
* Allow programs to take command line arguments
