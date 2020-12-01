import winsound

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, QUrl
from PyQt5 import QtCore
from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh
from newGui.MainWindow1 import Ui_MainWindow

import cv2
import sys
import math
import time
import random

start_time = time.time()
x = 1
counter = 0
greenMinimum = (78, 59, 50)
greenMaximum = (102, 248, 199)

w, h = model_wh('400x368')
estimator = TfPoseEstimator(get_graph_path('cmu'), target_size=(w, h))


def findPoint(pose, points):
    for value in pose:
        try:
            partOfBody = value.body_parts[points]
            return int(partOfBody.x * width), int(partOfBody.y * height)
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


def angleCount(point1, point2, point3):
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
    if (kneeAngleR in range(80, 180) or kneeAngleL in range(80, 180)) and (
            neckAngleR in range(110, 150) or neckAngleL in range(110, 150)):
        return True
    return False


def lungesDone(kneeAngleR, kneeAngleL):
    if kneeAngleR in range(80, 100) or kneeAngleL in range(80, 100):
        return True
    return False


def lungesDoneScore(kneeAngleR, kneeAngleL):
    if kneeAngleR in range(80, 90) or kneeAngleL in range(80, 90):
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
            kneeAngleR in range(145, 180) or kneeAngleL in range(145, 180)) and \
            (hipAngleR in range(145, 180) or hipAngleL in range(150, 145)) and (
            neckAngleR in range(150, 180) or neckAngleL in range(150, 180)):
        return True
    return False


def pushUpsDone(ankleAngleR, ankleAngleL):
    if ankleAngleR in range(75, 120) or ankleAngleL in range(75, 120):
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
        self.out = cv2.VideoWriter('Wideo/Wykroki.avi', self.fourcc, 3, (640, 480))
        while True:
            ret, frame = self.cap.read()
            if ret:
                allPerson = estimator.inference(frame, resize_to_default=(w > 0 and h > 0), upsample_size=4.0)
                frame = TfPoseEstimator.draw_humans(frame, allPerson, imgcopy=False)
                height, width = frame.shape[0], frame.shape[1]

                if len(allPerson) > 0:
                    # katy
                    angleKneeR = angleCount(findPoint(allPerson, 10), findPoint(allPerson, 9), findPoint(allPerson, 8))
                    angleKneeL = angleCount(findPoint(allPerson, 13), findPoint(allPerson, 12),
                                            findPoint(allPerson, 11))
                    angleNeckR = angleCount(findPoint(allPerson, 8), findPoint(allPerson, 1), findPoint(allPerson, 0))
                    angleNeckL = angleCount(findPoint(allPerson, 11), findPoint(allPerson, 1), findPoint(allPerson, 0))
                    # dystans
                    wrist_hipR = int(euclidianDistance(findPoint(allPerson, 4), findPoint(allPerson, 8)))
                    wrist_hipL = int(euclidianDistance(findPoint(allPerson, 7), findPoint(allPerson, 11)))
                    wrist_noseR = int(euclidianDistance(findPoint(allPerson, 4), findPoint(allPerson, 0)))
                    wrist_noseL = int(euclidianDistance(findPoint(allPerson, 7), findPoint(allPerson, 0)))

                    if angleKneeR < 80:
                        cv2.putText(frame, "Zachowaj kat prosty w kolanie!", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)
                    if angleNeckR < 110 or angleNeckL > 150:
                        cv2.putText(frame, "Patrz przed siebie!", (20, 55), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)
                    if wrist_hipR > wrist_noseR:
                        cv2.putText(frame, "Trzymaj rece przy ciele!", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)

                    if lungesStart(angleKneeR, angleKneeL, angleNeckR, angleNeckL) and (
                            wrist_hipL < wrist_noseL or wrist_hipR < wrist_noseR):
                        frame = TfPoseEstimator.draw_humans2(frame, allPerson, imgcopy=False)
                        if lungesDone(angleKneeR, angleKneeL):
                            frame = TfPoseEstimator.draw_humans3(frame, allPerson, imgcopy=False)
                            if lungesDoneScore(angleKneeR, angleKneeL):
                                frame = TfPoseEstimator.draw_humans4(frame, allPerson, imgcopy=False)
                                cv2.putText(frame, "Powrot do gory!", (20, 105), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                            color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)
                else:
                    cv2.putText(frame, "Brak uzytkownika na obrazie!", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)

                qImg1 = QImage(frame.data, width, height, QImage.Format_BGR888)
                self.changePixmap.emit(qImg1)
                self.out.write(frame)

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
        self.out = cv2.VideoWriter('Wideo/Pompki.avi', self.fourcc, 3, (640, 480))
        while True:
            ret, frame = self.cap.read()
            if ret:
                allPerson = estimator.inference(frame, resize_to_default=(w > 0 and h > 0), upsample_size=4.0)
                frame = TfPoseEstimator.draw_humans(frame, allPerson, imgcopy=False)
                height, width = frame.shape[0], frame.shape[1]
                if len(allPerson) > 0:
                    # katy
                    angleAnkleR = angleCount(findPoint(allPerson, 4), findPoint(allPerson, 3), findPoint(allPerson, 2))
                    angleAnkleL = angleCount(findPoint(allPerson, 7), findPoint(allPerson, 6), findPoint(allPerson, 5))
                    angleKneeR = angleCount(findPoint(allPerson, 8), findPoint(allPerson, 9), findPoint(allPerson, 10))
                    angleKneeL = angleCount(findPoint(allPerson, 11), findPoint(allPerson, 12),
                                            findPoint(allPerson, 13))
                    angleHipR = angleCount(findPoint(allPerson, 1), findPoint(allPerson, 8), findPoint(allPerson, 9))
                    angleHipL = angleCount(findPoint(allPerson, 1), findPoint(allPerson, 11), findPoint(allPerson, 12))
                    angleNeckR = angleCount(findPoint(allPerson, 8), findPoint(allPerson, 1), findPoint(allPerson, 0))
                    angleNeckL = angleCount(findPoint(allPerson, 11), findPoint(allPerson, 1), findPoint(allPerson, 0))

                    if angleKneeR < 145:
                        cv2.putText(frame, "Nie zginaj kolan!", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)
                    if angleHipR < 145:
                        cv2.putText(frame, "Biodra nizej!", (20, 55), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)
                    if angleNeckR < 150:
                        cv2.putText(frame, "Patrz przed siebie!", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)

                    if pushUps(angleAnkleR, angleAnkleL, angleKneeR, angleKneeL, angleHipR, angleHipL, angleNeckR,
                               angleNeckL):
                        frame = TfPoseEstimator.draw_humans2(frame, allPerson, imgcopy=False)
                        if pushUpsDone(angleAnkleR, angleAnkleL):
                            frame = TfPoseEstimator.draw_humans3(frame, allPerson, imgcopy=False)
                            if pushUpsDoneScore(angleAnkleR, angleAnkleL):
                                frame = TfPoseEstimator.draw_humans4(frame, allPerson, imgcopy=False)
                                cv2.putText(frame, "Powrot do gory!", (20, 105), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                            color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)
                else:
                    cv2.putText(frame, "Brak uzytkownika na obrazie!", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)

                qImg2 = QImage(frame.data, width, height, QImage.Format_BGR888)
                self.changePixmap.emit(qImg2)
                self.out.write(frame)

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
        self.out = cv2.VideoWriter('Wideo/Plank.avi', self.fourcc, 3, (640, 480))
        while True:
            ret, frame = self.cap.read()
            if ret:
                allPerson = estimator.inference(frame, resize_to_default=(w > 0 and h > 0), upsample_size=4.0)
                frame = TfPoseEstimator.draw_humans(frame, allPerson, imgcopy=False)
                height, width = frame.shape[0], frame.shape[1]
                if len(allPerson) > 0:
                    # dystans
                    foot_distance = int(euclidianDistance(findPoint(allPerson, 10), findPoint(allPerson, 13)))
                    ankle_distance = int(euclidianDistance(findPoint(allPerson, 3), findPoint(allPerson, 6)))
                    # katy
                    angleAnkleR = angleCount(findPoint(allPerson, 7), findPoint(allPerson, 6), findPoint(allPerson, 5))
                    angleAnkleL = angleCount(findPoint(allPerson, 4), findPoint(allPerson, 3), findPoint(allPerson, 2))
                    angleKneeR = angleCount(findPoint(allPerson, 8), findPoint(allPerson, 9), findPoint(allPerson, 10))
                    angleKneeL = angleCount(findPoint(allPerson, 11), findPoint(allPerson, 12),
                                            findPoint(allPerson, 13))
                    angleHipR = angleCount(findPoint(allPerson, 1), findPoint(allPerson, 8), findPoint(allPerson, 9))
                    angleHipL = angleCount(findPoint(allPerson, 1), findPoint(allPerson, 11), findPoint(allPerson, 12))
                    angleNeckR = angleCount(findPoint(allPerson, 0), findPoint(allPerson, 1), findPoint(allPerson, 8))
                    angleNeckL = angleCount(findPoint(allPerson, 0), findPoint(allPerson, 1), findPoint(allPerson, 11))

                    if angleAnkleR < 80:
                        cv2.putText(frame, "Trzymaj kat prosty w lokciach!", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)
                    if angleKneeR < 125:
                        cv2.putText(frame, "Nie zginaj kolan!", (20, 55), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)
                    if angleHipR < 115:
                        cv2.putText(frame, "Biodra nizej!", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)
                    if angleNeckR < 130:
                        cv2.putText(frame, "Patrz przed siebie!", (20, 105), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)
                    if foot_distance > ankle_distance:
                        cv2.putText(frame, "Stopy za szeroko!", (20, 105), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)

                    if plank(angleAnkleR, angleAnkleL, angleKneeR, angleKneeL, angleHipR, angleHipL, angleNeckR,
                             angleNeckL) and foot_distance < ankle_distance:
                        frame = TfPoseEstimator.draw_humans2(frame, allPerson, imgcopy=False)
                        if plankDone(angleAnkleR, angleAnkleL):
                            frame = TfPoseEstimator.draw_humans3(frame, allPerson, imgcopy=False)
                            cv2.putText(frame, "Tak trzymaj!", (20, 130), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                        color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)
                else:
                    cv2.putText(frame, "Brak uzytkownika na obrazie!", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)

                qImg3 = QImage(frame.data, width, height, QImage.Format_BGR888)
                self.changePixmap.emit(qImg3)
                self.out.write(frame)

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
        self.out = cv2.VideoWriter('Wideo/Przysiady.avi', self.fourcc, 3, (640, 480))
        while True:
            ret, frame = self.cap.read()
            if ret:
                allPerson = estimator.inference(frame, resize_to_default=(w > 0 and h > 0), upsample_size=4.0)
                frame = TfPoseEstimator.draw_humans(frame, allPerson, imgcopy=False)
                height, width = frame.shape[0], frame.shape[1]
                if len(allPerson) > 0:
                    # dystans
                    foot_distance = int(euclidianDistance(findPoint(allPerson, 10), findPoint(allPerson, 13)))
                    knee_distance = int(euclidianDistance(findPoint(allPerson, 9), findPoint(allPerson, 12)))
                    shoulders_distance = int(euclidianDistance(findPoint(allPerson, 2), findPoint(allPerson, 5)))
                    # katy
                    angleKneeR = angleCount(findPoint(allPerson, 11), findPoint(allPerson, 12),
                                            findPoint(allPerson, 13))
                    angleKneeL = angleCount(findPoint(allPerson, 8), findPoint(allPerson, 9), findPoint(allPerson, 10))
                    angleNeckR = angleCount(findPoint(allPerson, 8), findPoint(allPerson, 1), findPoint(allPerson, 0))
                    angleNeckL = angleCount(findPoint(allPerson, 11), findPoint(allPerson, 1), findPoint(allPerson, 0))

                    if angleNeckR < 120:
                        cv2.putText(frame, "Patrz przed siebie!", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)
                    if shoulders_distance <= 0.55 * foot_distance:
                        cv2.putText(frame, "Stopy za szeroko!", (20, 55), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)
                    if shoulders_distance >= 1.3 * foot_distance:
                        cv2.putText(frame, "Rozszerz stopy!", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)
                    if knee_distance <= 0.7 * foot_distance:
                        cv2.putText(frame, "Kolana zbyt wasko!", (20, 105), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)
                    if knee_distance >= 1.35 * foot_distance:
                        cv2.putText(frame, "Kolana za szeroko!", (20, 130), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)

                    if squats(angleKneeR, angleKneeL, angleNeckR, angleNeckL) and (
                            knee_distance >= 0.7 * foot_distance) and (
                            foot_distance <= 1.35 * knee_distance) \
                            and (shoulders_distance >= 0.55 * foot_distance) and (
                            shoulders_distance <= 1.3 * foot_distance):

                        frame = TfPoseEstimator.draw_humans2(frame, allPerson, imgcopy=False)
                        if squatsDone(angleKneeR, angleKneeL):
                            frame = TfPoseEstimator.draw_humans3(frame, allPerson, imgcopy=False)
                            if squatDoneScore(angleKneeR, angleKneeL):
                                frame = TfPoseEstimator.draw_humans4(frame, allPerson, imgcopy=False)
                                cv2.putText(frame, "Powrot do gory!", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                            color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)
                else:
                    cv2.putText(frame, "Brak uzytkownika na obrazie!", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)

                qImg4 = QImage(frame.data, width, height, QImage.Format_BGR888)
                self.changePixmap.emit(qImg4)
                self.out.write(frame)

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
        startTime = random.randint(5, 13)
        time.sleep(startTime)
        start_time = time.time()
        duration = 800  # milliseconds
        freq = 540  # Hz
        while True:
            ret, frame = self.cap.read()
            if ret:
                allPerson = estimator.inference(frame, resize_to_default=(w > 0 and h > 0), upsample_size=4.0)
                frame = TfPoseEstimator.draw_humans(frame, allPerson, imgcopy=False)
                height, width = frame.shape[0], frame.shape[1]
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                mask = cv2.inRange(hsv, greenMinimum, greenMaximum)
                mask = cv2.erode(mask, None, iterations=2)
                mask = cv2.dilate(mask, None, iterations=2)
                allBall = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
                qImg5 = QImage(frame.data, width, height, QImage.Format_BGR888)

                if len(allBall) > 0:
                    c = max(allBall, key=cv2.contourArea)
                    ((x, y), radius) = cv2.minEnclosingCircle(c)
                    wrist_ballR = int(euclidianDistance(findPoint(allPerson, 4), (x, y)))
                    wrist_ballL = int(euclidianDistance(findPoint(allPerson, 7), (x, y)))
                    timer = (time.time() - start_time)
                    hours, rem = divmod(timer, 3600)
                    minutes, seconds = divmod(rem, 60)
                    if radius > 10:
                        cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                        if wrist_ballR < 50 or wrist_ballL < 50:
                            winsound.Beep(freq + 100, duration)
                            self.cap.release()

                        cv2.putText(frame, "Czas: {:0>2}:{:05.2f}".format(int(minutes), seconds), (20, 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)
                else:
                    cv2.putText(frame, "Nie wykryto pilki", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)

                self.changePixmap.emit(qImg5)

    def stop(self):
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
        self.ui.pushButton20.clicked.connect(self.showPage)
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

        self.ui.pushButton19.setEnabled(False)

    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, directory="Wideo/")
        self.ui.pushButton19.setEnabled(True)
        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))


    def startVideo(self):

        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.stop()
            self.ui.pushButton19.setText("Start")
            self.ui.pushButton20.setEnabled(True)
            self.ui.pushButton20_2.setEnabled(True)
        else:
            self.mediaPlayer.play()
            self.ui.pushButton19.setText("Cofnij")
            self.ui.pushButton20.setEnabled(False)
            self.ui.pushButton20_2.setEnabled(False)


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
            self.ui.pushButton_4.setEnabled(False)
            self.ui.pushButton_5.setEnabled(False)
        else:
            # stop timer
            self.ui.image_label.clear()
            self.th1.changePixmap.disconnect(self.setImage)
            self.saveTimer.stop()
            self.th1.stop()
            self.ui.pushButton_3.setText("Rozpocznij\nnagrywanie")
            self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton_5.setEnabled(True)

    def controlTimer2(self):
        if not self.saveTimer2.isActive():
            self.saveTimer2.start()
            self.th2 = PushUps(self)
            self.th2.changePixmap.connect(self.setImage2)
            self.th2.start()
            self.ui.pushButton13.setText("Zakończ\nnagrywanie")
            self.ui.pushButton14.setEnabled(False)
            self.ui.pushButton15.setEnabled(False)
        else:
            self.ui.image_label_3.clear()
            self.th2.changePixmap.disconnect(self.setImage2)
            self.saveTimer2.stop()
            self.th2.stop()
            self.ui.pushButton13.setText("Rozpocznij\nnagrywanie")
            self.ui.pushButton14.setEnabled(True)
            self.ui.pushButton15.setEnabled(True)

    def controlTimer3(self):
        if not self.saveTimer3.isActive():
            self.saveTimer3.start()
            self.th3 = Plank(self)
            self.th3.changePixmap.connect(self.setImage3)
            self.th3.start()
            self.ui.pushButton_10.setText("Zakończ\nnagrywanie")
            self.ui.pushButton_11.setEnabled(False)
            self.ui.pushButton_12.setEnabled(False)
        else:
            self.ui.image_label_2.clear()
            self.th3.changePixmap.disconnect(self.setImage3)
            self.saveTimer3.stop()
            self.th3.stop()
            self.ui.pushButton_10.setText("Rozpocznij\nnagrywanie")
            self.ui.pushButton_11.setEnabled(True)
            self.ui.pushButton_12.setEnabled(True)

    def controlTimer4(self):
        if not self.saveTimer4.isActive():
            self.saveTimer4.start()
            self.th4 = Squats(self)
            self.th4.changePixmap.connect(self.setImage4)
            self.th4.start()
            self.ui.pushButton16.setText("Zakończ\nnagrywanie")
            self.ui.pushButton17.setEnabled(False)
            self.ui.pushButton18.setEnabled(False)
        else:
            self.ui.image_label_7.clear()
            self.th4.changePixmap.disconnect(self.setImage4)
            self.saveTimer4.stop()
            self.th4.stop()
            self.ui.pushButton16.setText("Rozpocznij\nnagrywanie")
            self.ui.pushButton17.setEnabled(True)
            self.ui.pushButton18.setEnabled(True)

    def controlTimer5(self):
        if not self.saveTimer5.isActive():
            global start_time
            self.saveTimer5.start()
            self.th5 = BallReaction(self)
            self.th5.changePixmap.connect(self.setImage5)
            self.th5.start()
            self.ui.pushButton19_4.setText("Jeszcze\nraz!")
            self.ui.pushButton20_7.setEnabled(False)
        else:
            self.ui.image_label_11.clear()
            self.th5.changePixmap.disconnect(self.setImage5)
            self.saveTimer5.stop()
            self.th5.stop()
            self.ui.pushButton19_4.setText("Start")
            self.ui.pushButton20_7.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
