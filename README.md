# Engineering thesis - Image processing based athleets training support system

## Table of Contents
1. [Abstract](#abstract-)
2. [Assumptions](#assumptions-)
3. [System architecture](#system-architecture-)
4. [Implementation](#implementation-)
5. [Tests](#tests-)

## Abstract :

The aim of engeneering work is to create an information system to support athlete training
using analysis of procsessed video images to detect special features such as ball or body parts.
In addition, system is designed to allow user to measure response time.

The objectives set were fully achived. Result of work is creation of a desktop application
e-Trener enabling, in conjuction with laptop equipped with webcam, to analyze exercises
performer, such as sit-ups, push-ups, planks and lunges, in real time. The system also allows to
measure the response time by using algotithms witch detects ball.
The paper describes history of computer vision creation and its implementation. In order
to detemine conditions for analysis of exercise, collected information about correct performance
of exercises was used.

The application was written in Python 3.7 using Realtime Multi-Person 2D Pose Estimation
algorithm to detect key points on body. After testing, it was decided to choose the CMU
classification model. Unlike to other models, CMU is characterized by high accurancy. Despite
low-performance equipment, the resulting frame rate is 2,5 frames per second. This allows to
correct analisys of the exercise. When chcecking reflex, an algorithm was used to detect the ball
by colour granding. Due to high frame rate required, a more efficient device should be used to
measure response time

## Assumptions :
* detection of specific features such as the ball and body parts
* checking that exercises are carried out correctly
* real-time operation
* measurement of an athlete's reflexes

## System architecture :

<img src="https://user-images.githubusercontent.com/58517152/123172649-b5bd1380-d47d-11eb-9044-c1c7f9864281.png" width="50%" height="50%">

## Implementation :

The user panel consists of eight pages on a single
stackedWidget. Moving within the application is made possible by functions that change the
the page displayed on the widget when the button is pressed, an example is shown below
below is an example of the showPage function allowing the display of the "e-Trainer" panel.

<img src="https://user-images.githubusercontent.com/58517152/123172911-1e0bf500-d47e-11eb-8b63-f49fa984cd0b.png" width="50%" height="50%">

<img src="https://user-images.githubusercontent.com/58517152/123173820-75f72b80-d47f-11eb-8587-a74b1331815d.png" width="50%" height="50%">

The repetitions performed during training are analysed in an equal manner
for each exercise. For a particular model, key points are generated and then combined to
key points are generated for a specific model and then combined to form the user's "skeleton". There are 18 key points in the application
determining the position of the nose, neck, eyes, ears, shoulders, elbows, wrists, hips, knees and
ankles. Using the findPoint function x and y coordinates are calculated coordinates are used to determine the position of points in the image.

Then, depending on the selected exercise, the conditions for
to pass the repetition performed. They are determined by the distance and angles between
determined key points. In order to calculate the distance between body parts in
Cartesian coordinates, the formula for the Euclidean distance


To calculate the angles formed by the "skeleton" connecting the points, the theorem
cosines theorem. The cosAngle function calculates the distances between points point1, point2 and
point3 are calculated, and then inserted into the transformed cosine formula that allows
calculation of angles with known side lengths of the triangle. To convert radians to degrees
the result is multiplied by 180/π.

Example for Push Up:

<img src="https://user-images.githubusercontent.com/58517152/123174344-4268d100-d480-11eb-87d3-c061c3e38c25.png" width="120%" height="120%">

## Tests :

In order to ensure optimal system results, available
models with varying degrees of accuracy in applying keypoints to the user
and impact on application start-up and frame rate. Tests
were carried out on four models: "CMU", "Mobilenet_thin", "Mobilenet_v2_large" and
"Mobilenet_v2_small".

Despite the large difference in application start-up time and the frequency with which
frames are displayed on the screen, the mobilenet models' accuracy in comparison to the CMU 
model is very low. The generated keypoints do not allow to carry out measurements.
The generated keypoints do not allow measurements to be taken of exercises performed in the supine position and generate frequent errors during the reading of.
The generated key points do not allow measurements for exercises performed in a standing position and generate frequent errors when reading workouts performed in a standing position. Therefore it was decided to select the
CMU model as the default for the e-Trainer application.

Examples of models tested:

<img src="https://user-images.githubusercontent.com/58517152/123174814-05510e80-d481-11eb-911f-2794df799d53.png" width="70%" height="70%">

The main factor determining the frame rate and the accuracy with which
keypoints are superimposed on the user are the image resolution values. In order to
improve the speed of the processes carried out for the CMU model, different variants of
multiples of 16.

Reducing the image resolution values has a high impact on the number of
frames per second, however, in the case of exercises performed in the lying position
the accuracy of overlaying key points decreases dramatically. For a resolution of
384x368 resolution point deviations begin to appear which have an impact on the analysis of the performed
analysis of the performed exercise. In the case of exercises performed in the standing position, the generated points
points generated allow the analysis to be carried out even for values of 368x304. In order to increase the
of displayed frames without significant loss of quality, a resolution of 400x368
