from enum import Enum

import tensorflow as tf
import cv2

regularizer_conv = 0.004
regularizer_dsconv = 0.0004
batchnorm_fused = True
activation_fn = tf.nn.relu


class CocoPart(Enum):
    Nose = 0
    Neck = 1
    RShoulder = 2
    RElbow = 3
    RWrist = 4
    LShoulder = 5
    LElbow = 6
    LWrist = 7
    RHip = 8
    RKnee = 9
    RAnkle = 10
    LHip = 11
    LKnee = 12
    LAnkle = 13
    REye = 14
    LEye = 15
    REar = 16
    LEar = 17
    Background = 18


CocoPairs = [
    (1, 2), (1, 5), (2, 3), (3, 4), (5, 6), (6, 7), (1, 8), (8, 9), (9, 10), (1, 11),
    (11, 12), (12, 13), (1, 0), (0, 14), (14, 16), (0, 15), (15, 17), (2, 16), (5, 17)
]  # = 19
CocoPairsRender = CocoPairs[:-2]

CocoColors = [[0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255],
              [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255],
              [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]]

CocoColors2 = [[0, 140, 0], [0, 140, 0], [0, 140, 0], [0, 140, 0], [0, 140, 0], [0, 140, 0], [0, 140, 0],
               [0, 140, 0], [0, 140, 0], [0, 140, 0], [0, 140, 0], [0, 140, 0], [0, 140, 0], [0, 140, 0],
               [0, 140, 0], [0, 140, 0], [0, 140, 0], [0, 140, 0]]

CocoColors3 = [[127, 255, 0], [127, 255, 0], [127, 255, 0], [127, 255, 0], [127, 255, 0], [127, 255, 0], [127, 255, 0],
               [127, 255, 0], [127, 255, 0], [127, 255, 0], [127, 255, 0], [127, 255, 0], [127, 255, 0], [127, 255, 0],
               [127, 255, 0], [127, 255, 0], [127, 255, 0], [127, 255, 0]]

CocoColors4 = [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255],
               [255, 255, 255],
               [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255],
               [255, 255, 255],
               [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]]


def read_imgfile(path, width=None, height=None):
    val_image = cv2.imread(path, cv2.IMREAD_COLOR)
    if width is not None and height is not None:
        val_image = cv2.resize(val_image, (width, height))
    return val_image


def to_str(s):
    if not isinstance(s, str):
        return s.decode('utf-8')
    return s