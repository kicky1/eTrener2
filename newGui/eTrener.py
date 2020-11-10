from threading import Timer

import imutils
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, QUrl
from PyQt5 import QtCore
from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh
from newGui.MainWindow1 import Ui_MainWindow
import argparse
import logging
import cv2
import sys
import math
import time
import winsound
import random
from datetime import timedelta

start_time = time.time()
x = 1
counter = 0
blueMinimum = (86, 102, 88)
blueMaximum = (102, 255, 253)

logger = logging.getLogger('eTrener')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
parser = argparse.ArgumentParser(description='eTrener')
parser.add_argument('--camera', type=str, default=0)
parser.add_argument('--resize', type=str, default='400x368')
parser.add_argument('--resize-out-ratio', type=float, default=4.0)
parser.add_argument('--model', type=str, default='cmu')
parser.add_argument('--show-process', type=bool, default=False)
args = parser.parse_args()
logger.debug('Inicializacja %s : %s' % (args.model, get_graph_path(args.model)))

w, h = model_wh(args.resize)
e = TfPoseEstimator(get_graph_path(args.model), target_size=(w, h))


def findPoint(pose, p):
    for point in pose:
        try:
            bodyPart = point.body_parts[p]
            return int(bodyPart.x * width), int(bodyPart.y * height)
        except:
            return (0, 0)
    return (0, 0)


'''
Odleglosc euklidesowa - sluzy do obliczenia odleglosci pomiedzy dwoma punktami w przestrzeni dwuwymiarowej.
Miara ta jest odległością wyrażoną w linii prostej między skupieniami. Dedykowana jest tylko dla zmiennych ilościowych.
'''


def euclidianDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


'''
Funkcja odpowiedzialna za znalezienie kata gdy znane sa trzy punkty wzor, jest to
obliczanie katow miedzy wektorami.
Wykorzystano prawo cosinusów cas(c) = (a^2+b^2-c^2)/2ab
'''


def cosAngle(point1, point2, point3):
    '''
        p1 is center point from where we measured angle between p0 and p2
        Punkt 1 jest punktem skad mierzymy kat miedzy punktami 0 i 2
    '''
    try:
        a = (point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2
        b = (point2[0] - point3[0]) ** 2 + (point2[1] - point3[1]) ** 2
        c = (point3[0] - point1[0]) ** 2 + (point3[1] - point1[1]) ** 2
        angle = math.acos((a + b - c) / math.sqrt(4 * a * b)) * 180 / math.pi
    except:
        return 0
    return int(angle)


def lungesStart(kneeAngleR, kneeAngleL, neckAngleR, neckAngleL):
    """
    kneeAngleR oraz kneeAngleL to katy tworzone przez kosc udowa i piszczelowa
    neckAngleR oraz neckAngleL to katy miedzy szyja a tulowiem
    """
    if (kneeAngleR in range(74, 180) or kneeAngleL in range(74, 180)) and (
            neckAngleR in range(110, 150) or neckAngleL in range(110, 150)):
        return True
    return False


def lungesDone(kneeAngleR, kneeAngleL):
    if kneeAngleR in range(74, 100) or kneeAngleL in range(74, 100):
        return True
    return False


def lungesDoneScore(kneeAngleR, kneeAngleL):
    if kneeAngleR in range(74, 90) or kneeAngleL in range(74, 90):
        return True
    return False


def pushUps(ankleAngleR, ankleAngleL, kneeAngleR, kneeAngleL, hipAngleR, hipAngleL, neckAngleR, neckAngleL):
    """
        ankleAngleR oraz ankleAngleL to katy miedzy ramieniem a przedramieniem
        kneeAngleR oraz kneeAngleL to katy tworzone przez kosc udowa i piszczelowa
        hipAngleR oraz hipAngleL to katy miedzy tulowiem a nogami
        neckAngleR oraz neckAngleL to katy miedzy szyja a tulowiem
    """
    if (ankleAngleR in range(75, 180) or ankleAngleL in range(75, 180)) and (
            kneeAngleR in range(135, 175) or kneeAngleL in range(135, 175)) and \
            (hipAngleR in range(150, 180) or hipAngleL in range(150, 180) and (
                    neckAngleR in range(130, 180) or neckAngleL in range(130, 180))):
        return True
    return False


def pushUpsDone(ankleAngleR, ankleAngleL):
    if ankleAngleR in range(75, 110) or ankleAngleL in range(75, 110):
        return True
    return False


def pushUpsDoneScore(ankleAngleR, ankleAngleL):
    if ankleAngleR in range(75, 90) or ankleAngleL in range(75, 90):
        return True
    return False


def plank(ankleAngleR, ankleAngleL, kneeAngleR, kneeAngleL, hipAngleR, hipAngleL, neckAngleR, neckAngleL):
    """
        ankleAngleR oraz ankleAngleL to katy miedzy ramieniem a przedramieniem
        kneeAngleR oraz kneeAngleL to katy tworzone przez kosc udowa i piszczelowa
        hipAngleR oraz hipAngleL to katy miedzy tulowiem a nogami
        neckAngleR oraz neckAngleL to katy miedzy szyja a tulowiem
    """
    if (ankleAngleR in range(80, 180) or ankleAngleL in range(80, 180)) and (
            kneeAngleR in range(125, 180) or kneeAngleL in range(125, 180)) and \
            (hipAngleR in range(115, 180) or hipAngleL in range(115, 180) and (
                    neckAngleR in range(130, 180) or neckAngleL in range(130, 180))):
        return True
    return False


def plankDone(ankleAngleR, ankleAngleL):
    if ankleAngleR in range(70, 100) or ankleAngleL in range(70, 100):
        return True
    return False


def squats(kneeAngleR, kneeAngleL, neckAngleR, neckAngleL):
    """
    kneeAngleR oraz kneeAngleL to katy miedzy lydka a udem
    neckAngleR oraz neckAngleL to katy miedzy tulowiem a szyja
    """
    if (kneeAngleR in range(70, 180) or kneeAngleL in range(70, 180)) and (
            neckAngleR in range(120, 180) or neckAngleL in range(120, 180)):
        return True
    return False


def squatsDone(kneeAngleR, kneeAngleL):
    if kneeAngleR in range(70, 120) or kneeAngleL in range(70, 120):
        return True
    return False


def squatDoneScore(kneeAngleR, kneeAngleL):
    if kneeAngleR in range(70, 90) or kneeAngleL in range(70, 90):
        return True
    return False


class Lunges(QThread):
    changePixmap = pyqtSignal(QImage)

    def __init__(self, *args, **kwargs):
        super().__init__()

    def run(self):
        global counter, start_time
        global height, width
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap.set(3, 480)
        self.cap.set(4, 640)
        self.cap.set(5, 7)
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter('Wideo/Wykroki.avi', self.fourcc, 7, (640, 480))
        while True:
            ret1, image1 = self.cap.read()
            if ret1:
                humans = e.inference(image1, resize_to_default=(w > 0 and h > 0), upsample_size=args.resize_out_ratio)
                pose = humans
                image1 = TfPoseEstimator.draw_humans(image1, humans, imgcopy=False)
                height, width = image1.shape[0], image1.shape[1]

                if len(pose) > 0:
                    # katy
                    angleKneeR = cosAngle(findPoint(pose, 10), findPoint(pose, 9), findPoint(pose, 8))
                    angleKneeL = cosAngle(findPoint(pose, 13), findPoint(pose, 12), findPoint(pose, 11))
                    angleNeckR = cosAngle(findPoint(pose, 8), findPoint(pose, 1), findPoint(pose, 0))
                    angleNeckL = cosAngle(findPoint(pose, 11), findPoint(pose, 1), findPoint(pose, 0))
                    # dystans
                    wrist_hipR = int(euclidianDistance(findPoint(pose, 4), findPoint(pose, 8)))
                    wrist_hipL = int(euclidianDistance(findPoint(pose, 7), findPoint(pose, 11)))
                    wrist_noseR = int(euclidianDistance(findPoint(pose, 4), findPoint(pose, 0)))
                    wrist_noseL = int(euclidianDistance(findPoint(pose, 7), findPoint(pose, 0)))
                    print(str(angleNeckR))
                    if angleKneeR < 70:
                        cv2.putText(image1, "Zachowaj kat prosty w kolanie!", (20, 50), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                    color=(0, 0, 255))
                    if angleNeckR < 110 or angleNeckL > 150:
                        cv2.putText(image1, "Patrz przed siebie!", (20, 70), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                    color=(0, 0, 255))
                    if wrist_hipR > wrist_noseR:
                        cv2.putText(image1, "Trzymaj ręce przy ciele!", (20, 90), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                    color=(0, 0, 255))

                    if lungesStart(angleKneeR, angleKneeL, angleNeckR, angleNeckL) and (
                            wrist_hipL < wrist_noseL or wrist_hipR < wrist_noseR):
                        image1 = TfPoseEstimator.draw_humans2(image1, humans, imgcopy=False)
                        if lungesDone(angleKneeR, angleKneeL):
                            image1 = TfPoseEstimator.draw_humans3(image1, humans, imgcopy=False)
                            if lungesDoneScore(angleKneeR, angleKneeL):
                                image1 = TfPoseEstimator.draw_humans4(image1, humans, imgcopy=False)
                                cv2.putText(image1, "Powrot do gory!", (20, 80), cv2.FONT_HERSHEY_TRIPLEX, 1,
                                            color=(255, 255, 255))

                qImg1 = QImage(image1.data, width, height, QImage.Format_BGR888)
                self.changePixmap.emit(qImg1)
                self.out.write(image1)

    def stop(self):
        self.out.release()
        self.cap.release()


class PushUps(QThread):
    changePixmap = pyqtSignal(QImage)

    def __init__(self, *args, **kwargs):
        super().__init__()

    def run(self):
        global height, width
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap.set(3, 480)
        self.cap.set(4, 640)
        self.cap.set(5, 7)
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter('Wideo/Pompki.avi', self.fourcc, 7, (640, 480))
        while True:
            ret1, image1 = self.cap.read()
            if ret1:
                humans = e.inference(image1, resize_to_default=(w > 0 and h > 0), upsample_size=args.resize_out_ratio)
                pose = humans
                image1 = TfPoseEstimator.draw_humans(image1, humans, imgcopy=False)
                height, width = image1.shape[0], image1.shape[1]
                cv2.putText(image1, "Brak uzytkownika na obrazie!", (20, 70), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                            color=(0, 0, 255))
                if len(pose) > 0:
                    # katy
                    angleAnkleR = cosAngle(findPoint(pose, 4), findPoint(pose, 3), findPoint(pose, 2))
                    angleAnkleL = cosAngle(findPoint(pose, 7), findPoint(pose, 6), findPoint(pose, 5))
                    angleKneeR = cosAngle(findPoint(pose, 8), findPoint(pose, 9), findPoint(pose, 10))
                    angleKneeL = cosAngle(findPoint(pose, 11), findPoint(pose, 12), findPoint(pose, 13))
                    angleHipR = cosAngle(findPoint(pose, 1), findPoint(pose, 8), findPoint(pose, 9))
                    angleHipL = cosAngle(findPoint(pose, 1), findPoint(pose, 11), findPoint(pose, 12))
                    angleNeckR = cosAngle(findPoint(pose, 8), findPoint(pose, 1), findPoint(pose, 0))
                    angleNeckL = cosAngle(findPoint(pose, 11), findPoint(pose, 1), findPoint(pose, 0))
                    print(str(angleNeckR))
                    if angleKneeR < 135:
                        cv2.putText(image1, "Nie zginaj kolan!", (20, 50), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                    color=(0, 0, 255))
                    if angleHipR < 150:
                        cv2.putText(image1, "Tylek nizej!", (20, 70), cv2.FONT_HERSHEY_TRIPLEX, 0.75, color=(0, 0, 255))
                    if angleNeckR < 130:
                        cv2.putText(image1, "Patrz przed siebie!", (20, 90), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                    color=(0, 0, 255))

                    if pushUps(angleAnkleR, angleAnkleL, angleKneeR, angleKneeL, angleHipR, angleHipL, angleNeckR,
                               angleNeckL):
                        image1 = TfPoseEstimator.draw_humans2(image1, pose, imgcopy=False)
                        if pushUpsDone(angleAnkleR, angleAnkleL):
                            image1 = TfPoseEstimator.draw_humans3(image1, pose, imgcopy=False)
                            if pushUpsDoneScore(angleAnkleR, angleAnkleL):
                                image1 = TfPoseEstimator.draw_humans4(image1, pose, imgcopy=False)
                                cv2.putText(image1, "Powrot do gory!", (20, 80), cv2.FONT_HERSHEY_TRIPLEX, 1,
                                            color=(255, 255, 255))
                qImg2 = QImage(image1.data, width, height, QImage.Format_BGR888)
                self.changePixmap.emit(qImg2)
                self.out.write(image1)

    def stop(self):
        self.out.release()
        self.cap.release()


class Plank(QThread):
    changePixmap = pyqtSignal(QImage)

    def __init__(self, *args, **kwargs):
        super().__init__()

    def run(self):
        global height, width
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap.set(3, 480)
        self.cap.set(4, 640)
        self.cap.set(5, 7)
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter('Wideo/Plank.avi', self.fourcc, 7, (640, 480))
        while True:
            ret1, image1 = self.cap.read()
            if ret1:
                humans = e.inference(image1, resize_to_default=(w > 0 and h > 0), upsample_size=args.resize_out_ratio)
                pose = humans
                image1 = TfPoseEstimator.draw_humans(image1, humans, imgcopy=False)
                height, width = image1.shape[0], image1.shape[1]
                cv2.putText(image1, "Brak uzytkownika na obrazie!", (20, 70), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                            color=(0, 0, 255))
                if len(pose) > 0:
                    # distance calculations
                    foot_distance = int(euclidianDistance(findPoint(pose, 10), findPoint(pose, 13)))
                    ankle_distance = int(euclidianDistance(findPoint(pose, 3), findPoint(pose, 6)))
                    # angle calcucations
                    angleAnkleR = cosAngle(findPoint(pose, 7), findPoint(pose, 6), findPoint(pose, 5))
                    angleAnkleL = cosAngle(findPoint(pose, 4), findPoint(pose, 3), findPoint(pose, 2))
                    angleKneeR = cosAngle(findPoint(pose, 8), findPoint(pose, 9), findPoint(pose, 10))
                    angleKneeL = cosAngle(findPoint(pose, 11), findPoint(pose, 12), findPoint(pose, 13))
                    angleHipR = cosAngle(findPoint(pose, 1), findPoint(pose, 8), findPoint(pose, 9))
                    angleHipL = cosAngle(findPoint(pose, 1), findPoint(pose, 11), findPoint(pose, 12))
                    angleNeckR = cosAngle(findPoint(pose, 0), findPoint(pose, 1), findPoint(pose, 8))
                    angleNeckL = cosAngle(findPoint(pose, 0), findPoint(pose, 1), findPoint(pose, 11))

                    if angleAnkleR < 80:
                        cv2.putText(image1, "Trzymaj kat prosty w lokciach!", (20, 50), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                    color=(0, 0, 255))
                    if angleKneeR < 125:
                        cv2.putText(image1, "Nie zginaj kolan!", (20, 60), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                    color=(0, 0, 255))
                    if angleHipR < 115:
                        cv2.putText(image1, "Tylek nizej!", (20, 70), cv2.FONT_HERSHEY_TRIPLEX, 0.75, color=(0, 0, 255))
                    if angleNeckR < 130:
                        cv2.putText(image1, "Patrz przed siebie!", (20, 80), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                    color=(0, 0, 255))

                    if plank(angleAnkleR, angleAnkleL, angleKneeR, angleKneeL, angleHipR, angleHipL, angleNeckR,
                             angleNeckL) and foot_distance < ankle_distance:
                        image1 = TfPoseEstimator.draw_humans2(image1, pose, imgcopy=False)
                        if plankDone(angleAnkleR, angleAnkleL):
                            image1 = TfPoseEstimator.draw_humans3(image1, pose, imgcopy=False)
                            cv2.putText(image1, "Tak trzymaj!", (20, 90), cv2.FONT_HERSHEY_TRIPLEX, 1,
                                        color=(255, 255, 255))

                qImg3 = QImage(image1.data, width, height, QImage.Format_BGR888)
                self.changePixmap.emit(qImg3)
                self.out.write(image1)

    def stop(self):
        self.out.release()
        self.cap.release()


class Squats(QThread):
    changePixmap = pyqtSignal(QImage)

    def __init__(self, *args, **kwargs):
        super().__init__()

    def run(self):
        global height, width
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap.set(3, 480)
        self.cap.set(4, 640)
        self.cap.set(5, 7)
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter('Wideo/Squats.avi', self.fourcc, 7, (640, 480))
        while True:
            ret1, image1 = self.cap.read()
            if ret1:
                humans = e.inference(image1, resize_to_default=(w > 0 and h > 0), upsample_size=args.resize_out_ratio)
                pose = humans
                image1 = TfPoseEstimator.draw_humans(image1, humans, imgcopy=False)
                height, width = image1.shape[0], image1.shape[1]
                cv2.putText(image1, "Brak uzytkownika na obrazie!", (20, 70), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                            color=(0, 0, 255))
                if len(pose) > 0:
                    # dystans
                    foot_distance = int(euclidianDistance(findPoint(pose, 10), findPoint(pose, 13)))
                    knee_distance = int(euclidianDistance(findPoint(pose, 9), findPoint(pose, 12)))
                    shoulders_distance = int(euclidianDistance(findPoint(pose, 2), findPoint(pose, 5)))
                    # katy
                    angleKneeR = cosAngle(findPoint(pose, 11), findPoint(pose, 12), findPoint(pose, 13))
                    angleKneeL = cosAngle(findPoint(pose, 8), findPoint(pose, 9), findPoint(pose, 10))
                    angleNeckR = cosAngle(findPoint(pose, 8), findPoint(pose, 1), findPoint(pose, 0))
                    angleNeckL = cosAngle(findPoint(pose, 11), findPoint(pose, 1), findPoint(pose, 0))
                    print(str(shoulders_distance))

                    if angleNeckR < 120:
                        cv2.putText(image1, "Patrz przed siebie!", (20, 50), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                    color=(0, 0, 255))
                    if shoulders_distance <= 0.55 * foot_distance:
                        cv2.putText(image1, "Stopy za szeroko!", (20, 70), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                    color=(0, 0, 255))
                    if shoulders_distance >= 1.3 * foot_distance:
                        cv2.putText(image1, "Rozszerz stopy!", (20, 80), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                    color=(0, 0, 255))
                    if knee_distance <= 0.7 * foot_distance:
                        cv2.putText(image1, "Kolana zbyt wasko!", (20, 90), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                    color=(0, 0, 255))
                    if knee_distance >= 1.35 * foot_distance:
                        cv2.putText(image1, "Kolana za szeroko!", (20, 100), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                    color=(0, 0, 255))

                    if squats(angleKneeR, angleKneeL, angleNeckR, angleNeckL) and (
                            knee_distance >= 0.7 * foot_distance) and (
                            foot_distance <= 1.35 * knee_distance) \
                            and (shoulders_distance >= 0.55 * foot_distance) and (
                            shoulders_distance <= 1.3 * foot_distance):

                        image1 = TfPoseEstimator.draw_humans2(image1, pose, imgcopy=False)
                        if squatsDone(angleKneeR, angleKneeL):
                            image1 = TfPoseEstimator.draw_humans3(image1, pose, imgcopy=False)
                            if squatDoneScore(angleKneeR, angleKneeL):
                                image1 = TfPoseEstimator.draw_humans4(image1, pose, imgcopy=False)
                                cv2.putText(image1, "Powrot do gory!", (20, 80), cv2.FONT_HERSHEY_TRIPLEX, 1,
                                            color=(255, 255, 255))
                qImg4 = QImage(image1.data, width, height, QImage.Format_BGR888)
                self.changePixmap.emit(qImg4)
                self.out.write(image1)

    def stop(self):
        self.out.release()
        self.cap.release()


class BallReaction(QThread):
    changePixmap = pyqtSignal(QImage)

    def __init__(self, *args, **kwargs):
        super().__init__()

    def run(self):
        global height, width, start_time
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap.set(3, 480)
        self.cap.set(4, 640)
        self.cap.set(5, 7)
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter('Wideo/Squats.avi', self.fourcc, 7, (640, 480))
        startTime = random.randint(5, 13)
        time.sleep(startTime)
        print(str(startTime))
        duration = 800  # milliseconds
        freq = 540  # Hz
        winsound.Beep(freq, duration)
        start_time = time.time()

        while True:
            ret1, image1 = self.cap.read()
            if ret1:
                humans = e.inference(image1, resize_to_default=(w > 0 and h > 0), upsample_size=args.resize_out_ratio)
                pose = humans
                image1 = TfPoseEstimator.draw_humans(image1, humans, imgcopy=False)
                height, width = image1.shape[0], image1.shape[1]

                hsv = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
                mask = cv2.inRange(hsv, blueMinimum, blueMaximum)
                mask = cv2.erode(mask, None, iterations=2)
                mask = cv2.dilate(mask, None, iterations=2)
                ball = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

                center = None
                if len(ball) > 0:
                    c = max(ball, key=cv2.contourArea)
                    ((x, y), radius) = cv2.minEnclosingCircle(c)
                    wrist_ball = int(euclidianDistance(findPoint(pose, 4), (x, y)))
                    print(str(wrist_ball))
                    timer = (time.time() - start_time)
                    hours, rem = divmod(timer, 3600)
                    minutes, seconds = divmod(rem, 60)
                    if radius > 10:
                        cv2.circle(image1, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                        if wrist_ball < 50:
                            winsound.Beep(freq+100, duration)
                            break
                        cv2.putText(image1, "Czas: {:0>2}:{:05.2f}".format(int(minutes),seconds), (20, 80), cv2.FONT_HERSHEY_TRIPLEX, 1,
                                    color=(255, 255, 255))

                qImg5 = QImage(image1.data, width, height, QImage.Format_BGR888)
                self.changePixmap.emit(qImg5)
                self.out.write(image1)

    def stop(self):
        self.out.release()
        self.cap.release()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

        self.ui.pushButton_2.clicked.connect(self.showPage3)
        self.ui.pushButton_4.clicked.connect(self.showPage7)
        self.ui.pushButton_5.clicked.connect(self.showPage)
        self.ui.pushButton_6.clicked.connect(self.showPage5)
        self.ui.pushButton_7.clicked.connect(self.showPage6)
        self.ui.pushButton_8.clicked.connect(self.showPage4)
        self.ui.pushButton_9.clicked.connect(self.showPage2)
        self.ui.pushButton_11.clicked.connect(self.showPage7)
        self.ui.pushButton_12.clicked.connect(self.showPage)
        self.ui.pushButton20.clicked.connect(self.showPage3)
        self.ui.pushButton14.clicked.connect(self.showPage7)
        self.ui.pushButton15.clicked.connect(self.showPage)
        self.ui.pushButton17.clicked.connect(self.showPage7)
        self.ui.pushButton18.clicked.connect(self.showPage)
        self.ui.pushButton_13.clicked.connect(self.showPage_6)
        self.ui.pushButton20_7.clicked.connect(self.showPage)
        self.ui.pushButton20_2.clicked.connect(self.openFile)
        self.ui.pushButton19.clicked.connect(self.startVideo)
        self.ui.pushButton.clicked.connect(self.exit)

        self.ui.pushButton_3.clicked.connect(self.controlTimer)
        self.saveTimer = QTimer()
        self.ui.pushButton13.clicked.connect(self.controlTimer2)
        self.saveTimer2 = QTimer()
        self.ui.pushButton_10.clicked.connect(self.controlTimer3)
        self.saveTimer3 = QTimer()
        self.ui.pushButton16.clicked.connect(self.controlTimer4)
        self.saveTimer4 = QTimer()
        self.ui.pushButton19_4.clicked.connect(self.controlTimer5)
        self.saveTimer5 = QTimer()

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setVideoOutput(self.ui.video_label)

    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, directory="Wideo/")
        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))

    def startVideo(self):

        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
            self.ui.pushButton19.setText("Start")
        else:
            self.mediaPlayer.play()
            self.ui.pushButton19.setText("Stop")

    def show(self):
        self.main_win.show()

    def exit(self):
        QtCore.QCoreApplication.instance().quit()

    def showPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

    def showPage2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)

    def showPage3(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)

    def showPage5(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_5)

    def showPage4(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_4)

    def showPage6(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page6)

    def showPage_6(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_6)

    def showPage7(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page7)

    @QtCore.pyqtSlot(QImage)
    def setImage(self, qImg1):
        self.ui.image_label.setPixmap(QPixmap.fromImage(qImg1))

    @QtCore.pyqtSlot(QImage)
    def setImage2(self, qImg2):
        self.ui.image_label_3.setPixmap(QPixmap.fromImage(qImg2))

    @QtCore.pyqtSlot(QImage)
    def setImage3(self, qImg3):
        self.ui.image_label_2.setPixmap(QPixmap.fromImage(qImg3))

    @QtCore.pyqtSlot(QImage)
    def setImage4(self, qImg4):
        self.ui.image_label_7.setPixmap(QPixmap.fromImage(qImg4))

    @QtCore.pyqtSlot(QImage)
    def setImage5(self, qImg5):
        self.ui.image_label_11.setPixmap(QPixmap.fromImage(qImg5))

    def controlTimer(self):
        if not self.saveTimer.isActive():
            self.saveTimer.start()
            self.th1 = Lunges(self)
            self.th1.changePixmap.connect(self.setImage)
            self.th1.start()
            self.ui.pushButton_3.setText("Zakończ\nnagrywanie")
        else:
            # stop timer
            self.ui.image_label.clear()
            self.th1.changePixmap.disconnect(self.setImage)
            self.saveTimer.stop()
            self.th1.stop()
            self.ui.pushButton_3.setText("Rozpocznij\nnagrywanie")

    def controlTimer2(self):
        if not self.saveTimer2.isActive():
            self.saveTimer2.start()
            self.th2 = PushUps(self)
            self.th2.changePixmap.connect(self.setImage2)
            self.th2.start()
            self.ui.pushButton13.setText("Zakończ\nnagrywanie")
        else:
            self.ui.image_label_3.clear()
            self.th2.changePixmap.disconnect(self.setImage2)
            self.saveTimer2.stop()
            self.th2.stop()
            self.ui.pushButton13.setText("Rozpocznij\nnagrywanie")

    def controlTimer3(self):
        if not self.saveTimer3.isActive():
            self.saveTimer3.start()
            self.th3 = Plank(self)
            self.th3.changePixmap.connect(self.setImage3)
            self.th3.start()
            self.ui.pushButton_10.setText("Zakończ\nnagrywanie")
        else:
            self.ui.image_label_2.clear()
            self.th3.changePixmap.disconnect(self.setImage3)
            self.saveTimer3.stop()
            self.th3.stop()
            self.ui.pushButton_10.setText("Rozpocznij\nnagrywanie")

    def controlTimer4(self):
        if not self.saveTimer4.isActive():
            self.saveTimer4.start()
            self.th4 = Squats(self)
            self.th4.changePixmap.connect(self.setImage4)
            self.th4.start()
            self.ui.pushButton16.setText("Zakończ\nnagrywanie")
        else:
            self.ui.image_label_7.clear()
            self.th4.changePixmap.disconnect(self.setImage4)
            self.saveTimer4.stop()
            self.th4.stop()
            self.ui.pushButton16.setText("Rozpocznij\nnagrywanie")

    def controlTimer5(self):
        if not self.saveTimer5.isActive():
            global start_time
            self.saveTimer5.start()
            self.th5 = BallReaction(self)
            self.th5.changePixmap.connect(self.setImage5)
            self.th5.start()
            self.ui.pushButton19_4.setText("Jeszcze\nraz!")

        else:
            self.ui.image_label_11.clear()
            self.th5.changePixmap.disconnect(self.setImage5)
            self.saveTimer5.stop()
            self.th5.stop()
            self.ui.pushButton19_4.setText("Start")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
