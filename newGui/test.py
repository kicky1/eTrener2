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
import os
import cv2
import sys
import math
import time
global height, width, out
start_time = time.time()
x =1
counter = 0


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
            return int(bodyPart.x * width + 0.5), int(bodyPart.y * height + 0.5)
        except:
            return 0, 0
    return 0, 0


'''
Odleglosc euklidesowa - sluzy do obliczenia odleglosci pomiedzy dwoma punktami w przestrzeni trojwymiarowej.
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


def lungesStart(a, b, c, d):
    """
    a oraz b to katy miedzy udem a lydka
    c oraz d to katy miedzy tulowiem a szyja
    """
    if (a in range(74, 190) or b in range(74, 190)) and (c in range(110, 140) or d in range(110, 140)):
        return True
    return False


def lungesDone(a, b):
    """
    a oraz b to katy miedzy udem a lydka
    """
    if a in range(74, 100) or b in range(74, 100):
        return True
    return False


def lungesDoneScore(a, b):
    """
    a oraz b to katy miedzy udem a lydka
    """
    if a in range(74, 90) or b in range(74, 90):
        return True
    return False


def pushUps(a, b, c, d, e, f, g, h):
    """
        a oraz b to katy miedzy ramieniem a przedramieniem
        c oraz d to katy miedzy lydka a udem
        e oraz f to katy miedzy nogami a tulowiem
        g oraz h to katy miedzy tulowiem a szyja
    """
    if (a in range(75, 200) or b in range(75, 200)) and (c in range(135, 175) or d in range(135, 175)) and \
            (e in range(150, 190) or f in range(150, 190) and (g in range(130, 190) or h in range(130, 190))):
        return True
    return False


def pushUpsDone(a, b):
    """
    a oraz b to katy miedzy ramieniem a przedramieniem
    """
    if a in range(75, 110) or b in range(75, 110):
        return True
    return False


def pushUpsDoneScore(a, b):
    """
    a oraz b to katy miedzy ramieniem a przedramieniem
    """
    if a in range(75, 90) or b in range(75, 90):
        return True
    return False


def plank(a, b, c, d, e, f, g, h):
    """
        a oraz b to katy miedzy ramieniem a przedramieniem
        c oraz d to katy miedzy lydka a udem
        e oraz f to katy miedzy nogami a tulowiem
        g oraz h to katy miedzy tulowiem a szyja
    """
    if (a in range(70, 195) or b in range(60, 195)) and (c in range(125, 175) or d in range(125, 175)) and \
            (e in range(118, 190) or f in range(118, 190) and (g in range(130, 190) or h in range(130, 190))):
        return True
    return False


def plankDone(a, b):
    """
    a oraz b to katy miedzy ramieniem a przedramieniem
    """
    if a in range(70, 100) or b in range(60, 100):
        return True
    return False


def squats(a, b, c, d):
    """
    a oraz b to katy miedzy lydka a udem
    c oraz d to katy miedzy tulowiem a szyja
    """
    if (a in range(75, 195) or b in range(75, 195)) and (c in range(120, 190) or d in range(120, 190)):
        return True
    return False


def squatsDone(a, b):
    """
    a oraz b to katy miedzy lydka a udem
    """
    if a in range(75, 100) or b in range(75, 100):
        return True
    return False


def squatDoneScore(a, b):
    """
    a oraz b to katy miedzy lydka a udem
    """
    if a in range(75, 90) or b in range(75, 90):
        return True
    return False


class Lunges(QThread):
    changePixmap = pyqtSignal(QImage)

    def __init__(self, *args, **kwargs):
        super().__init__()

    def run(self):
        global counter, start_time
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
                image = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
                height1, width1, channel1 = image.shape
                step1 = channel1 * width1
                if len(pose) > 0:
                    # katy
                    angle1 = cosAngle(findPoint(pose, 10), findPoint(pose, 9), findPoint(pose, 8))
                    angle2 = cosAngle(findPoint(pose, 13), findPoint(pose, 12), findPoint(pose, 11))
                    angle3 = cosAngle(findPoint(pose, 8), findPoint(pose, 1), findPoint(pose, 0))
                    angle4 = cosAngle(findPoint(pose, 11), findPoint(pose, 1), findPoint(pose, 0))
                    # dystans
                    wrist_hipR = int(euclidianDistance(findPoint(pose, 4), findPoint(pose, 8)))
                    wrist_hipL = int(euclidianDistance(findPoint(pose, 7), findPoint(pose, 11)))
                    wrist_noseR = int(euclidianDistance(findPoint(pose, 4), findPoint(pose, 0)))
                    wrist_noseL = int(euclidianDistance(findPoint(pose, 7), findPoint(pose, 0)))

                    if angle1 < 72 or angle2 < 72:
                        cv2.putText(image1, "Zachowaj kat prosty w kolanie!", (20, 50), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                    color=(0, 0, 255))
                    if angle3 < 98 or angle4 > 148:
                        cv2.putText(image1, "Patrz przed siebie!", (20, 70), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                    color=(0, 0, 255))
                    if wrist_hipR > wrist_noseR:
                        cv2.putText(image1, "Trzymaj ręce przy ciele!", (20, 90), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                    color=(0, 0, 255))

                    if lungesStart(angle1, angle2, angle3, angle4) and (
                            wrist_hipL < wrist_noseL or wrist_hipR < wrist_noseR):
                        image1 = TfPoseEstimator.draw_humans2(image1, humans, imgcopy=False)
                        if lungesDone(angle1, angle2):
                            image1 = TfPoseEstimator.draw_humans3(image1, humans, imgcopy=False)
                            if lungesDoneScore(angle1, angle2):
                                image1 = TfPoseEstimator.draw_humans4(image1, humans, imgcopy=False)
                                cv2.putText(image1, "Powrot do gory!", (20, 80), cv2.FONT_HERSHEY_TRIPLEX, 1,
                                            color=(255, 255, 255))

                counter += 1
                if (time.time() - start_time) > x:
                    print("FPS: ", counter / (time.time() - start_time))
                    counter = 0
                    start_time = time.time()

                qImg1 = QImage(image1.data, width1, height1, step1, QImage.Format_BGR888)
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
                image1 = TfPoseEstimator.draw_humans(image1, pose, imgcopy=False)
                image = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
                height1, width1, channel1 = image.shape
                step1 = channel1 * width1
                if len(pose) > 0:
                    # katy
                    angle1 = cosAngle(findPoint(pose, 4), findPoint(pose, 3), findPoint(pose, 2))
                    angle2 = cosAngle(findPoint(pose, 7), findPoint(pose, 6), findPoint(pose, 5))
                    angle3 = cosAngle(findPoint(pose, 8), findPoint(pose, 9), findPoint(pose, 10))
                    angle4 = cosAngle(findPoint(pose, 11), findPoint(pose, 12), findPoint(pose, 13))
                    angle5 = cosAngle(findPoint(pose, 1), findPoint(pose, 8), findPoint(pose, 9))
                    angle6 = cosAngle(findPoint(pose, 1), findPoint(pose, 11), findPoint(pose, 12))
                    angle7 = cosAngle(findPoint(pose, 8), findPoint(pose, 1), findPoint(pose, 0))
                    angle8 = cosAngle(findPoint(pose, 11), findPoint(pose, 1), findPoint(pose, 0))

                    if angle3 < 133:
                        cv2.putText(image1, "Nie zginaj kolan!", (20, 50), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                    color=(0, 0, 255))
                    if angle5 < 148:
                        cv2.putText(image1, "Tylek nizej!", (20, 70), cv2.FONT_HERSHEY_TRIPLEX, 0.75, color=(0, 0, 255))
                    if angle7 < 128:
                        cv2.putText(image1, "Patrz przed siebie!", (20, 90), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                    color=(0, 0, 255))

                    if pushUps(angle1, angle2, angle3, angle4, angle5, angle6, angle7, angle8):
                        image1 = TfPoseEstimator.draw_humans2(image1, pose, imgcopy=False)
                        if pushUpsDone(angle1, angle2):
                            image1 = TfPoseEstimator.draw_humans3(image1, pose, imgcopy=False)
                            if pushUpsDoneScore(angle1, angle2):
                                image1 = TfPoseEstimator.draw_humans4(image1, pose, imgcopy=False)
                                cv2.putText(image1, "Powrot do gory!", (20, 80), cv2.FONT_HERSHEY_TRIPLEX, 1,
                                            color=(255, 255, 255))
                qImg2 = QImage(image1.data, width1, height1, step1, QImage.Format_BGR888)
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
                image1 = TfPoseEstimator.draw_humans(image1, pose, imgcopy=False)
                image = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
                height1, width1, channel1 = image.shape
                step1 = channel1 * width1
                if len(pose) > 0:
                    # katy
                    angle1 = cosAngle(findPoint(pose, 10), findPoint(pose, 9), findPoint(pose, 8))
                    angle2 = cosAngle(findPoint(pose, 13), findPoint(pose, 12), findPoint(pose, 11))
                    angle3 = cosAngle(findPoint(pose, 8), findPoint(pose, 1), findPoint(pose, 0))
                    angle4 = cosAngle(findPoint(pose, 11), findPoint(pose, 1), findPoint(pose, 0))
                    # dystanse
                    wrist_hipR = int(euclidianDistance(findPoint(pose, 4), findPoint(pose, 8)))
                    wrist_hipL = int(euclidianDistance(findPoint(pose, 7), findPoint(pose, 11)))
                    wrist_noseR = int(euclidianDistance(findPoint(pose, 4), findPoint(pose, 0)))
                    wrist_noseL = int(euclidianDistance(findPoint(pose, 7), findPoint(pose, 0)))

                    if angle1 < 78 or angle2 < 78:
                        cv2.putText(image1, "Zachowaj kat prosty w kolanie!", (20, 50), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                    color=(0, 0, 255))
                    if angle3 < 98 or angle4 > 148:
                        cv2.putText(image1, "Patrz przed siebie!", (20, 70), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                    color=(0, 0, 255))
                    if wrist_hipR > wrist_noseR:
                        cv2.putText(image1, "TNie podnos rak za wysoko!", (20, 90), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                    color=(0, 0, 255))
                    if wrist_hipR < wrist_hipL:
                        cv2.putText(image1, "Nie podnos rak za wysoko!", (20, 110), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                    color=(0, 0, 255))

                    if lungesStart(angle1, angle2, angle3, angle4) and (
                            wrist_hipL < wrist_noseL or wrist_hipR < wrist_noseR):
                        image1 = TfPoseEstimator.draw_humans2(image1, pose, imgcopy=False)
                        if lungesDone(angle1, angle2):
                            image1 = TfPoseEstimator.draw_humans3(image1, pose, imgcopy=False)
                            if lungesDoneScore(angle1, angle2):
                                image1 = TfPoseEstimator.draw_humans4(image1, pose, imgcopy=False)
                                cv2.putText(image1, "Powrot do gory!", (20, 80), cv2.FONT_HERSHEY_TRIPLEX, 1,
                                            color=(255, 255, 255))
                qImg3 = QImage(image1.data, width1, height1, step1, QImage.Format_BGR888)
                self.changePixmap.emit(qImg3)
                self.out.write(image1)

    def stop(self):
        self.out.release()
        self.cap.release()


class Squats(QThread):
    changePixmap = pyqtSignal(QImage)

    def __init__(self, **kwargs):
        super().__init__()

    def run(self):
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
                image1 = TfPoseEstimator.draw_humans(image1, pose, imgcopy=False)
                image = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
                height1, width1, channel1 = image.shape
                step1 = channel1 * width1
                if len(pose) > 0:
                    # dystans
                    foot_distance = int(euclidianDistance(findPoint(pose, 10), findPoint(pose, 13)))
                    knee_distance = int(euclidianDistance(findPoint(pose, 9), findPoint(pose, 12)))
                    ankles_distance = int(euclidianDistance(findPoint(pose, 2), findPoint(pose, 5)))
                    # katy
                    angle1 = cosAngle(findPoint(pose, 11), findPoint(pose, 12), findPoint(pose, 13))
                    angle2 = cosAngle(findPoint(pose, 8), findPoint(pose, 9), findPoint(pose, 10))
                    angle3 = cosAngle(findPoint(pose, 8), findPoint(pose, 1), findPoint(pose, 0))
                    angle4 = cosAngle(findPoint(pose, 11), findPoint(pose, 1), findPoint(pose, 0))

                    if angle3 < 120:
                        cv2.putText(image1, "Glowa przed siebie!", (20, 50), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                    color=(0, 0, 255))
                    if foot_distance < 0.60 * ankles_distance:
                        cv2.putText(image1, "Rozszerz stopy!", (20, 70), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                    color=(0, 0, 255))
                    if foot_distance > 1.55 * ankles_distance:
                        cv2.putText(image1, "Stopy za szeroko!", (20, 90), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                    color=(0, 0, 255))

                    if squats(angle1, angle2, angle3, angle4) and (
                            foot_distance >= 0.4 * knee_distance) and (
                            foot_distance <= 1.6 * knee_distance) \
                            and (foot_distance >= 0.4 * ankles_distance) and (
                            foot_distance <= 1.95 * ankles_distance):

                        image1 = TfPoseEstimator.draw_humans2(image1, humans, imgcopy=False)
                        if squatsDone(angle1, angle2):
                            image1 = TfPoseEstimator.draw_humans3(image1, humans, imgcopy=False)
                            if squatDoneScore(angle1, angle2):
                                image1 = TfPoseEstimator.draw_humans4(image1, humans, imgcopy=False)
                                cv2.putText(image1, "Powrot do gory!", (20, 80), cv2.FONT_HERSHEY_TRIPLEX, 1,
                                            color=(255, 255, 255))
                qImg4 = QImage(image1.data, width1, height1, step1, QImage.Format_BGR888)
                self.changePixmap.emit(qImg4)
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

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setVideoOutput(self.ui.video_label)
        print("--- %s seconds ---" % (time.time() - start_time))

    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, directory="Wideo/")
        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))

    def close(self):
        if os.path.exists("output.avi"):
            os.remove('output.avi')

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
            self.th4 = Squats()
            self.th4.changePixmap.connect(self.setImage4)
            self.th4.start()
            self.ui.pushButton16.setText("Zakończ\nnagrywanie")
        else:
            self.ui.image_label_7.clear()
            self.th4.changePixmap.disconnect(self.setImage4)
            self.saveTimer4.stop()
            self.th4.stop()
            self.ui.pushButton16.setText("Rozpocznij\nnagrywanie")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
