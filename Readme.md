# HARCAPSTONE

Smart Human Activity Detection Using [YOLO](https://pjreddie.com/darknet/yolo/)

![Alt text](https://github.com/HarCapstone/harcapstone_project/blob/main/images/har-capstone-7-228x228.jpeg?raw=true)

This is a project to perform Object detection,fall detection,vehicle crash detection and social distancing detection from Webcam & video.

<b>Discipline | <b> Bachelor of Engineering in Computer Science
:--|:--|
<b> Project Name | <b> Smart Human Activity Detection Using YOLO
<b> Field |     <b> 1. Machine Learning<br>2. Computer Vision<br>

#### Mentor Details

<b>Mentored by | <b>  Prof.Anjali Dalvi 
:--|:--|
<b> Institute | <b> Suman Ramesh Tulsiani Technical Campus-Faculty of Engineering
<b> Email id|     <b> hodcomp@srttc.ac.in
<b> Department | Department of Computer Science (HOD)
<b> Photo | <img src="images/hod.jpg" alt="Prof.Anjali Dalvi" hight="100px" width="150px"/>

#### Developer Team

SrNo | Name | Work | Department| Institute | Email id |Photo
:--|:--|:--|:--|:--|:--| :--|
1 | Vedant Jadhav | Web Developer   | Bachelor of Engineering in Computer Science | Suman Ramesh Tulsiani Technical Campus-Faculty of Engineering , Kamshet |jadhav.vedant02062000@gmail.com | <a href="https://github.com/MrMuzik1"><img src="images/vedant.jpeg" alt="Vedant Jadhav" hight="150px" width="150px"/></a>

## How YOLO works ?

![Alt text](https://cdn-images-1.medium.com/max/1024/1*bSLNlG7crv-p-m4LVYYk3Q.png)

YOLO stands for You Only Look Once. It is used for object detection
To perform object detection on an image it looks at an image only once in a very clever way unlike R-CNN which takes several instances of the same image to perform detection. 

YOLO divides an image into a grid and several bounding boxes are formed. Then a confidence score is taken for each boundary box to see whether an bounding box contains any object within it. The confidence score is high if the object inside the box matches the pre-trained YOLO dataset ( [COCO Dataset](https://cocodataset.org/) ). The higher the confidence score, the higher the probability that a bounding box contains an object. Now several bounding boxes will intersect with each other. More the bounding boxes intersect, more is the probability that there is an object inside that box. Now we only keep those bounding boxes whose confidence score is more than threshold value lets say 30%. Now we match these bounding boxes with already known features of an object like person, car and classify them.

The good thing about YOLO is that all the predictions in the boxes are made at the same time i.e. the neural networks just ran only once.
And that is why YOLO is powerful and fast.

## Installation

### Softwares Required
* Python: Language in which code is written
* CMake: For compiling openCV
* Visual Studio Code: For building openCV and darknet code
* Nvidia GPU Driver: For faster GPU performance
* CUDA: For parallel computing using GPU
* CuDNN: A GPU-accelerated library of primitives for deep neural networks
* OpenCV: For working on images/videos in python
* Darknet: Neural network framework for YOLO
### Installation of above softwares
You can follow the two part YouTube videos of [Augmented Startups](https://www.youtube.com/watch?v=5pYh1rFnNZs&ab_channel=AugmentedStartups)

## Object Detection
### Working
Simple YOLO program for object detection.

### Installing the Requirement files:
```python
pip install -r requirements.txt
```

### Running the script:
```python
python obj_Detection.py
```
### Sample Output:
![Alt text](https://github.com/HarCapstone/harcapstone_project/blob/main/images/object_2.png?raw=true)
## Fall Detection
### Working
We take the input video from a source and  divide the video into several frames. Now these frames are converted into black and white. On each frame a person is detected using YOLO. 

Now we write the code to draw rectangles on the detected persons. Whenever the height of the rectangle is greater than width of the rectangle Fall is not detected and when width is greater than height Fall is detected.

And this is how we classify the images into a fall and not fall and an alert is generated if a fall is detected.

All of the above process happens for a single frame. Now all of this is set in a loop for each frame of the video and Fall is detected.

### Installing the Requirement files:
```python
pip install -r requirements.txt
```
### Running the script:
```python
python Fall Detection.py
```
### Sample Output:
![Alt text](https://github.com/vibhorkrishna/S.H.A.D.Y/blob/main/Screenshots/fall.PNG?raw=true)

## Social Distancing Detection
### Working
We take the input video from a source and  divide the video into several frames. Now these frames are converted into black and white. On each frame a person is detected using YOLO. 

Now we write the code to draw rectangles on the detected persons. We check the distances between each detected person on the frame from each other. If the distance between the two persons is less than a particular value then we colour the box red and draw a line between these boxes and add the no. of social distancing violations in a variable and display it. 

All of the above process happens for a single frame. Now all of this is set in a loop for each frame of the video and People at Risks are detected.

### Installing the Requirement files:
```python
pip install -r requirements.txt
```

### Running the script:
```python
python Social_Distance.py
```
### Sample Output:
![Alt text](https://github.com/HarCapstone/harcapstone_project/blob/main/images/social_1.png?raw=true)

## Vehicle Crash Detection
### Working
We take the input video from a source and  divide the video into several frames. Now these frames are converted into black and white. On each frame a car is detected using YOLO. 

Now we write the code to draw rectangles on the detected cars. We check the distances between each detected car on the frame from each other. If the distance between the two cars is less than a particular value and the rectangle boxes of any two cars intersect each other then we colour the box red display the message that Crash has been detected. 

All of the above process happens for a single frame. Now all of this is set in a loop for each frame of the video and Vehicle crash is detected.

### Installing the Requirement files:
```python
pip install -r requirements.txt
```

### Running the script:
```python
python vehicle.py
```
### Sample Output:
![Alt text](https://github.com/HarCapstone/harcapstone_project/blob/main/images/crash.png?raw=true)

## HARCAPSTONE Website
Smart Human Activity Detection Using [CLICK HERE](https://hardetection.social/)

### Home Page
![Alt text](https://github.com/vibhorkrishna/S.H.A.D.Y/blob/main/Screenshots/home.PNG?raw=true)
### Object Detection Page
![Alt text](https://github.com/vibhorkrishna/S.H.A.D.Y/blob/main/Screenshots/object_detection.PNG?raw=true)
### Fall Detection Page
![Alt text](https://github.com/vibhorkrishna/S.H.A.D.Y/blob/main/Screenshots/fall_detection.PNG?raw=true)
### Social Distancing Detection Page
![Alt text](https://github.com/vibhorkrishna/S.H.A.D.Y/blob/main/Screenshots/social_distancing_detection.PNG?raw=true)
### Vehicle Crash Detection Page
![Alt text](https://github.com/vibhorkrishna/S.H.A.D.Y/blob/main/Screenshots/vehicle_crash_detection.PNG?raw=true)


## Future Work
* As our code uses GPU, it would cost us money to deploy our Models on cloud servers like Google Cloud and AWS. But our future goal is to deploy these models globally from Google Cloud by using their GPU's.