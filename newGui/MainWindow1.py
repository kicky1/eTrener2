# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimediaWidgets import QVideoWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(843, 818)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(843, 818))
        MainWindow.setMaximumSize(QtCore.QSize(843, 818))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Downloads/weightlifting.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(246, 255, 231);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(252, 252, 252);")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(30, 20, 761, 771))
        self.stackedWidget.setStyleSheet("background-color: rgb(252, 252, 252);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(-10, 20, 791, 81))
        self.label.setStyleSheet("\n"
"font-family:Tahoma, Helvetica, Arial, Sans-Serif;\n"
"text-align: center;\n"
"font-size: 36px;\n"
"color: #222;\n"
"text-shadow: 0px 2px 3px black;\n"
"\n"
"\n"
"\n"
"")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(230, 570, 321, 181))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(180, 17, 17), stop:1 rgba(255, 144, 146));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 24px;\n"
"padding:10px;\n"
"}\n"
"QPushButton:hover {   \n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 144, 146), stop:1 rgba(180, 17, 17));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 26px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {   \n"
"background-color:rgb(255, 144, 146);\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:14px;\n"
"border-color:rgb(180, 17, 17);\n"
"font:bold 26px;\n"
"padding:10px;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.page)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 170, 321, 181))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(180, 17, 17), stop:1 rgba(255, 144, 146));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 24px;\n"
"padding:10px;\n"
"}\n"
"QPushButton:hover {   \n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 144, 146), stop:1 rgba(180, 17, 17));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 26px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {   \n"
"background-color:rgb(255, 144, 146);\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:14px;\n"
"border-color:rgb(180, 17, 17);\n"
"font:bold 26px;\n"
"padding:10px;\n"
"}\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_13 = QtWidgets.QPushButton(self.page)
        self.pushButton_13.setGeometry(QtCore.QRect(230, 370, 321, 181))
        self.pushButton_13.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(180, 17, 17), stop:1 rgba(255, 144, 146));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 24px;\n"
"padding:10px;\n"
"}\n"
"QPushButton:hover {   \n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 144, 146), stop:1 rgba(180, 17, 17));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 26px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {   \n"
"background-color:rgb(255, 144, 146);\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:14px;\n"
"border-color:rgb(180, 17, 17);\n"
"font:bold 26px;\n"
"padding:10px;\n"
"}\n"
"\n"
"")
        self.pushButton_13.setObjectName("pushButton_13")
        self.stackedWidget.addWidget(self.page)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label_13 = QtWidgets.QLabel(self.page_6)
        self.label_13.setGeometry(QtCore.QRect(-10, 30, 771, 61))
        self.label_13.setStyleSheet("text-align: center;\n"
"font-size: 36px;\n"
"color: #222;\n"
"text-shadow: 0px 2px 3px black;")
        self.label_13.setObjectName("label_13")
        self.image_label_11 = QtWidgets.QLabel(self.page_6)
        self.image_label_11.setGeometry(QtCore.QRect(60, 110, 661, 511))
        self.image_label_11.setAutoFillBackground(False)
        self.image_label_11.setStyleSheet("\n"
"background-color: black;\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:gray;\n"
"font:bold 50px;\n"
"padding:10px;\n"
"text-align:center\n"
"")
        self.image_label_11.setLineWidth(3)
        self.image_label_11.setMidLineWidth(2)
        self.image_label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label_11.setObjectName("image_label_11")
        self.pushButton19_4 = QtWidgets.QPushButton(self.page_6)
        self.pushButton19_4.setGeometry(QtCore.QRect(200, 650, 181, 101))
        self.pushButton19_4.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(180, 17, 17), stop:1 rgba(255, 144, 146));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"QPushButton:hover {   \n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 144, 146), stop:1 rgba(180, 17, 17));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 18px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {   \n"
"background-color:rgb(255, 144, 146);\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:14px;\n"
"border-color:rgb(180, 17, 17);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"")
        self.pushButton19_4.setObjectName("pushButton19_4")
        self.pushButton20_7 = QtWidgets.QPushButton(self.page_6)
        self.pushButton20_7.setGeometry(QtCore.QRect(410, 650, 181, 101))
        self.pushButton20_7.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(180, 17, 17), stop:1 rgba(255, 144, 146));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"QPushButton:hover {   \n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 144, 146), stop:1 rgba(180, 17, 17));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 18px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {   \n"
"background-color:rgb(255, 144, 146);\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:14px;\n"
"border-color:rgb(180, 17, 17);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"")
        self.pushButton20_7.setObjectName("pushButton20_7")
        self.stackedWidget.addWidget(self.page_6)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.image_label = QtWidgets.QLabel(self.page_2)
        self.image_label.setGeometry(QtCore.QRect(60, 120, 661, 511))
        self.image_label.setAutoFillBackground(False)
        self.image_label.setStyleSheet("\n"
"background-color: black;\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:gray;\n"
"font:bold 16px;\n"
"padding:10px")
        self.image_label.setLineWidth(3)
        self.image_label.setMidLineWidth(2)
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 660, 181, 101))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(180, 17, 17), stop:1 rgba(255, 144, 146));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"QPushButton:hover {   \n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 144, 146), stop:1 rgba(180, 17, 17));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 18px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {   \n"
"background-color:rgb(255, 144, 146);\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:14px;\n"
"border-color:rgb(180, 17, 17);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_4.setGeometry(QtCore.QRect(300, 660, 181, 101))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(180, 17, 17), stop:1 rgba(255, 144, 146));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"QPushButton:hover {   \n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 144, 146), stop:1 rgba(180, 17, 17));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 18px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {   \n"
"background-color:rgb(255, 144, 146);\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:14px;\n"
"border-color:rgb(180, 17, 17);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_5.setGeometry(QtCore.QRect(520, 660, 181, 101))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(180, 17, 17), stop:1 rgba(255, 144, 146));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"QPushButton:hover {   \n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 144, 146), stop:1 rgba(180, 17, 17));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 18px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {   \n"
"background-color:rgb(255, 144, 146);\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:14px;\n"
"border-color:rgb(180, 17, 17);\n"
"font:bold 14px;\n"
"padding:10px;\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label6_2 = QtWidgets.QLabel(self.page_2)
        self.label6_2.setGeometry(QtCore.QRect(0, 40, 761, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label6_2.setFont(font)
        self.label6_2.setStyleSheet("QLabel{\n"
"\n"
"text-align: center;\n"
"font-size: 36px;\n"
"color: #222;\n"
"text-shadow: 0px 2px 3px black;\n"
"}\n"
"\n"
"\n"
"")
        self.label6_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label6_2.setObjectName("label6_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page7 = QtWidgets.QWidget()
        self.page7.setObjectName("page7")
        self.label_11 = QtWidgets.QLabel(self.page7)
        self.label_11.setGeometry(QtCore.QRect(0, 40, 771, 61))
        self.label_11.setStyleSheet("text-align: center;\n"
"font-size: 36px;\n"
"color: #222;\n"
"text-shadow: 0px 2px 3px black;")
        self.label_11.setObjectName("label_11")
        self.pushButton19 = QtWidgets.QPushButton(self.page7)
        self.pushButton19.setGeometry(QtCore.QRect(300, 660, 181, 101))
        self.pushButton19.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(180, 17, 17), stop:1 rgba(255, 144, 146));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"QPushButton:hover {   \n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 144, 146), stop:1 rgba(180, 17, 17));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 18px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {   \n"
"background-color:rgb(255, 144, 146);\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:14px;\n"
"border-color:rgb(180, 17, 17);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"")
        self.pushButton19.setObjectName("pushButton19")
        self.pushButton20 = QtWidgets.QPushButton(self.page7)
        self.pushButton20.setGeometry(QtCore.QRect(520, 660, 181, 101))
        self.pushButton20.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(180, 17, 17), stop:1 rgba(255, 144, 146));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"QPushButton:hover {   \n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 144, 146), stop:1 rgba(180, 17, 17));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 18px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {   \n"
"background-color:rgb(255, 144, 146);\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:14px;\n"
"border-color:rgb(180, 17, 17);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"")
        self.pushButton20.setObjectName("pushButton20")
        self.video_label = QVideoWidget(self.page7)
        self.video_label.setGeometry(QtCore.QRect(60, 120, 661, 511))
        self.video_label.setAutoFillBackground(False)
        self.video_label.setStyleSheet("\n"
"background-color: black;\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:gray;\n"
"font:bold 16px;\n"
"padding:10px")
        self.video_label.setObjectName("image_label_8")
        self.pushButton20_2 = QtWidgets.QPushButton(self.page7)
        self.pushButton20_2.setGeometry(QtCore.QRect(80, 660, 181, 101))
        self.pushButton20_2.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(180, 17, 17), stop:1 rgba(255, 144, 146));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"QPushButton:hover {   \n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 144, 146), stop:1 rgba(180, 17, 17));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 18px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {   \n"
"background-color:rgb(255, 144, 146);\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:14px;\n"
"border-color:rgb(180, 17, 17);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"")
        self.pushButton20_2.setObjectName("pushButton20_2")
        self.stackedWidget.addWidget(self.page7)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(-10, 50, 781, 61))
        self.label_3.setStyleSheet("text-align: center;\n"
"font-size: 36px;\n"
"color: #222;\n"
"text-shadow: 0px 2px 3px black;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_9 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_9.setGeometry(QtCore.QRect(80, 160, 271, 221))
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(255, 255, 0), stop:1 rgb(255, 255, 203));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 20px;\n"
"color: black;\n"
"padding:10px;}\n"
"\n"
"QPushButton:hover {   \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(255, 255, 203), stop:1 rgb(255, 255, 0));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 24px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {   \n"
"background-color:rgb(255, 255, 203);\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 255, 203);\n"
"font:bold 24px;\n"
"padding:10px;\n"
"}\n"
"\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_6.setGeometry(QtCore.QRect(80, 460, 271, 221))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(255, 61, 236), stop:1 rgb(255, 221, 254));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 20px;\n"
"color: black;\n"
"padding:10px}\n"
"\n"
"QPushButton:hover {   \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(255, 221, 254) , stop:1 rgb(255, 61, 236));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(198, 255, 255);\n"
"font:bold 24px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {   \n"
"background-color:rgb(255, 221, 254);\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 221, 254);\n"
"font:bold 24px;\n"
"padding:10px;\n"
"}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_7.setGeometry(QtCore.QRect(420, 160, 271, 221))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(75, 252, 255), stop:1 rgb(198, 255, 255));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 20px;\n"
"color: black;\n"
"padding:10px}\n"
"\n"
"QPushButton:hover {   \n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(198, 255, 255), stop:1 rgb(75, 252, 255));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(198, 255, 255);\n"
"font:bold 24px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {   \n"
"background-color:rgb(198, 255, 255);\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 255, 203);\n"
"font:bold 24px;\n"
"padding:10px;\n"
"}\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_8.setGeometry(QtCore.QRect(420, 460, 271, 221))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(17, 220, 51), stop:1 rgb(210, 255, 223));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 20px;\n"
"color: black;\n"
"padding:10px;}\n"
"\n"
"QPushButton:hover {   \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(210, 255, 223) , stop:1 rgb(17, 220, 51) );\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(198, 255, 255);\n"
"font:bold 24px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {   \n"
"background-color:rgb(210, 255, 223);\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:24px;\n"
"border-color:rgb(255, 221, 254);\n"
"font:bold 16px;}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_4 = QtWidgets.QLabel(self.page_4)
        self.label_4.setGeometry(QtCore.QRect(0, 40, 761, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
"\n"
"text-align: center;\n"
"font-size: 36px;\n"
"color: #222;\n"
"text-shadow: 0px 2px 3px black;\n"
"}\n"
"\n"
"\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.image_label_2 = QtWidgets.QLabel(self.page_4)
        self.image_label_2.setGeometry(QtCore.QRect(60, 120, 661, 511))
        self.image_label_2.setAutoFillBackground(False)
        self.image_label_2.setStyleSheet("\n"
"background-color: black;\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:gray;\n"
"font:bold 16px;\n"
"padding:10px")
        self.image_label_2.setLineWidth(3)
        self.image_label_2.setMidLineWidth(2)
        self.image_label_2.setText("")
        self.image_label_2.setObjectName("image_label_2")
        self.pushButton_10 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_10.setGeometry(QtCore.QRect(80, 660, 181, 101))
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(180, 17, 17), stop:1 rgba(255, 144, 146));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"QPushButton:hover {   \n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 144, 146), stop:1 rgba(180, 17, 17));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 18px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {   \n"
"background-color:rgb(255, 144, 146);\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:14px;\n"
"border-color:rgb(180, 17, 17);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_11.setGeometry(QtCore.QRect(300, 660, 181, 101))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(180, 17, 17), stop:1 rgba(255, 144, 146));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"QPushButton:hover {   \n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 144, 146), stop:1 rgba(180, 17, 17));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 18px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {   \n"
"background-color:rgb(255, 144, 146);\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:14px;\n"
"border-color:rgb(180, 17, 17);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_12.setGeometry(QtCore.QRect(520, 660, 181, 101))
        self.pushButton_12.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(180, 17, 17), stop:1 rgba(255, 144, 146));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"QPushButton:hover {   \n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 144, 146), stop:1 rgba(180, 17, 17));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 18px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {   \n"
"background-color:rgb(255, 144, 146);\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:14px;\n"
"border-color:rgb(180, 17, 17);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"")
        self.pushButton_12.setObjectName("pushButton_12")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_5 = QtWidgets.QLabel(self.page_5)
        self.label_5.setGeometry(QtCore.QRect(0, 40, 751, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{\n"
"\n"
"text-align: center;\n"
"font-size: 36px;\n"
"color: #222;\n"
"text-shadow: 0px 2px 3px black;\n"
"}\n"
"\n"
"\n"
"")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.image_label_3 = QtWidgets.QLabel(self.page_5)
        self.image_label_3.setGeometry(QtCore.QRect(60, 120, 661, 511))
        self.image_label_3.setAutoFillBackground(False)
        self.image_label_3.setStyleSheet("\n"
"background-color: black;\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:gray;\n"
"font:bold 16px;\n"
"padding:10px")
        self.image_label_3.setLineWidth(3)
        self.image_label_3.setMidLineWidth(2)
        self.image_label_3.setText("")
        self.image_label_3.setObjectName("image_label_3")
        self.pushButton13 = QtWidgets.QPushButton(self.page_5)
        self.pushButton13.setGeometry(QtCore.QRect(80, 660, 181, 101))
        self.pushButton13.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(180, 17, 17), stop:1 rgba(255, 144, 146));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"QPushButton:hover {   \n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 144, 146), stop:1 rgba(180, 17, 17));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 18px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {   \n"
"background-color:rgb(255, 144, 146);\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:14px;\n"
"border-color:rgb(180, 17, 17);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"")
        self.pushButton13.setObjectName("pushButton13")
        self.pushButton14 = QtWidgets.QPushButton(self.page_5)
        self.pushButton14.setGeometry(QtCore.QRect(300, 660, 181, 101))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton14.setFont(font)
        self.pushButton14.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(180, 17, 17), stop:1 rgba(255, 144, 146));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"QPushButton:hover {   \n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 144, 146), stop:1 rgba(180, 17, 17));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 18px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {   \n"
"background-color:rgb(255, 144, 146);\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:14px;\n"
"border-color:rgb(180, 17, 17);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"")
        self.pushButton14.setObjectName("pushButton14")
        self.pushButton15 = QtWidgets.QPushButton(self.page_5)
        self.pushButton15.setGeometry(QtCore.QRect(520, 660, 181, 101))
        self.pushButton15.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(180, 17, 17), stop:1 rgba(255, 144, 146));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"QPushButton:hover {   \n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 144, 146), stop:1 rgba(180, 17, 17));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 18px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {   \n"
"background-color:rgb(255, 144, 146);\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:14px;\n"
"border-color:rgb(180, 17, 17);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"")
        self.pushButton15.setObjectName("pushButton15")
        self.stackedWidget.addWidget(self.page_5)
        self.page6 = QtWidgets.QWidget()
        self.page6.setObjectName("page6")
        self.image_label_7 = QtWidgets.QLabel(self.page6)
        self.image_label_7.setGeometry(QtCore.QRect(60, 120, 661, 511))
        self.image_label_7.setAutoFillBackground(False)
        self.image_label_7.setStyleSheet("\n"
"background-color: black;\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:gray;\n"
"font:bold 16px;\n"
"padding:10px")
        self.image_label_7.setLineWidth(3)
        self.image_label_7.setMidLineWidth(2)
        self.image_label_7.setText("")
        self.image_label_7.setObjectName("image_label_7")
        self.label6 = QtWidgets.QLabel(self.page6)
        self.label6.setGeometry(QtCore.QRect(0, 40, 761, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label6.setFont(font)
        self.label6.setStyleSheet("QLabel{\n"
"\n"
"text-align: center;\n"
"font-size: 36px;\n"
"color: #222;\n"
"text-shadow: 0px 2px 3px black;\n"
"}\n"
"\n"
"\n"
"")
        self.label6.setAlignment(QtCore.Qt.AlignCenter)
        self.label6.setObjectName("label6")
        self.pushButton16 = QtWidgets.QPushButton(self.page6)
        self.pushButton16.setGeometry(QtCore.QRect(80, 660, 181, 101))
        self.pushButton16.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(180, 17, 17), stop:1 rgba(255, 144, 146));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"QPushButton:hover {   \n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 144, 146), stop:1 rgba(180, 17, 17));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 18px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {   \n"
"background-color:rgb(255, 144, 146);\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:14px;\n"
"border-color:rgb(180, 17, 17);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"")
        self.pushButton16.setObjectName("pushButton16")
        self.pushButton17 = QtWidgets.QPushButton(self.page6)
        self.pushButton17.setGeometry(QtCore.QRect(300, 660, 181, 101))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton17.setFont(font)
        self.pushButton17.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(180, 17, 17), stop:1 rgba(255, 144, 146));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"QPushButton:hover {   \n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 144, 146), stop:1 rgba(180, 17, 17));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 18px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {   \n"
"background-color:rgb(255, 144, 146);\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:14px;\n"
"border-color:rgb(180, 17, 17);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"")
        self.pushButton17.setObjectName("pushButton17")
        self.pushButton18 = QtWidgets.QPushButton(self.page6)
        self.pushButton18.setGeometry(QtCore.QRect(520, 660, 181, 101))
        self.pushButton18.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(180, 17, 17), stop:1 rgba(255, 144, 146));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"QPushButton:hover {   \n"
"background-color:rgb(255, 144, 146);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 144, 146), stop:1 rgba(180, 17, 17));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:14px;\n"
"border-color:rgb(255, 202, 203);\n"
"font:bold 18px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:pressed {   \n"
"background-color:rgb(255, 144, 146);\n"
"color:white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:14px;\n"
"border-color:rgb(180, 17, 17);\n"
"font:bold 16px;\n"
"padding:10px;\n"
"}\n"
"")
        self.pushButton18.setObjectName("pushButton18")
        self.stackedWidget.addWidget(self.page6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "eTrener"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">e-Trener</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Wyjdź"))
        self.pushButton_2.setText(_translate("MainWindow", "Trening dokładności"))
        self.pushButton_13.setText(_translate("MainWindow", "Pomiar refleksu"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:27pt;\">Sprawdź swój refleks</span></p></body></html>"))
        self.image_label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.pushButton19_4.setText(_translate("MainWindow", "Start"))
        self.pushButton20_7.setText(_translate("MainWindow", "Powrót"))
        self.pushButton_3.setText(_translate("MainWindow", "Rozpocznij \n"
" nagrywanie"))
        self.pushButton_4.setText(_translate("MainWindow", "Sprawdź"))
        self.pushButton_5.setText(_translate("MainWindow", "Powrót do \n"
" menu"))
        self.label6_2.setText(_translate("MainWindow", "Wykroki"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Powtórka ćwiczenia</p><p align=\"center\"><br/></p></body></html>"))
        self.pushButton19.setText(_translate("MainWindow", "Start"))
        self.pushButton20.setText(_translate("MainWindow", "Powrót do menu"))
        self.pushButton20_2.setText(_translate("MainWindow", "Wybierz plik"))
        self.label_3.setText(_translate("MainWindow", "Wybierz trening"))
        self.pushButton_9.setText(_translate("MainWindow", "Wykroki"))
        self.pushButton_6.setText(_translate("MainWindow", "Pompki"))
        self.pushButton_7.setText(_translate("MainWindow", "Przysiady"))
        self.pushButton_8.setText(_translate("MainWindow", "Plank"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt;\">Plank</span></p></body></html>"))
        self.pushButton_10.setText(_translate("MainWindow", "Rozpocznij \n"
" nagrywanie"))
        self.pushButton_11.setText(_translate("MainWindow", "Sprawdź"))
        self.pushButton_12.setText(_translate("MainWindow", "Powrót do \n"
" menu"))
        self.label_5.setText(_translate("MainWindow", "Pompki"))
        self.pushButton13.setText(_translate("MainWindow", "Rozpocznij \n"
" nagrywanie"))
        self.pushButton14.setText(_translate("MainWindow", "Sprawdź"))
        self.pushButton15.setText(_translate("MainWindow", "Powrót do \n"
" menu"))
        self.label6.setText(_translate("MainWindow", "Przysiady"))
        self.pushButton16.setText(_translate("MainWindow", "Rozpocznij \n"
" nagrywanie"))
        self.pushButton17.setText(_translate("MainWindow", "Sprawdź"))
        self.pushButton18.setText(_translate("MainWindow", "Powrót do \n"
" menu"))
