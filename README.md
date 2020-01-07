# game-detector README

* To get data:

`screenshot.py`

Grabs a screenshot from a video every n frames. Change input video in code. 

* To train the model, run on the command line:

`python net.py`

* To test the model with an already existing model:

`python test.py`

Must first change the loaded model source, in code.

* To predict images using a loaded model:

`python predict.py`

Change the desired image path and the loaded model as pleased. 

In progress: 
- improving the model,
- allowing program to take command line arguments

