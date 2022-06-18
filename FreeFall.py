# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\FreeFall.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPen, QBrush
from PyQt5.QtCore import Qt, QRectF

from GraphicsDrawer import view


class Ui_FreeFall(QtWidgets.QWidget):

    def __init__(self, Main_W):
        super(Ui_FreeFall, self).__init__()
        "Main Window start"

        self.setObjectName("FreeFall")
        self.resize(1000, 1000)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setStyleSheet("background-color:black;\n"
                                 "border-style:none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LabelFrame = QtWidgets.QFrame(self.frame)
        self.LabelFrame.setMaximumSize(QtCore.QSize(16777215, 80))
        self.LabelFrame.setStyleSheet("background-color:none")
        self.LabelFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LabelFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LabelFrame.setObjectName("LabelFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.LabelFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.FreeFall_2 = QtWidgets.QLabel(self.LabelFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.FreeFall_2.setFont(font)
        self.FreeFall_2.setStyleSheet("color:white")
        self.FreeFall_2.setObjectName("FreeFall_2")
        self.horizontalLayout_2.addWidget(self.FreeFall_2)
        self.Exitbuttom = QtWidgets.QPushButton(self.LabelFrame, clicked=lambda: self.exitbutton(Main_W))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Exitbuttom.setFont(font)
        self.Exitbuttom.setStyleSheet(
            "QPushButton {background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, "
            "stop:0.2 rgba(255, 0, 0, 180), stop:1 rgba(0, 0, 0, 0));\n "
            "color:rgba(255,255,255,150);\n"
            "border-style:solid;}\n"
            "QPushButton:pressed {background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, "
            "fy:0.5, stop:0.2 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));\n "
            "color:rgba(255,255,255,255);\n"
            "border-style:solid;}")
        self.Exitbuttom.setObjectName("Exitbuttom")
        self.horizontalLayout_2.addWidget(self.Exitbuttom)
        self.verticalLayout.addWidget(self.LabelFrame)
        self.FrameGeneral = QtWidgets.QFrame(self.frame)
        self.FrameGeneral.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameGeneral.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameGeneral.setObjectName("FrameGeneral")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.FrameGeneral)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ButtonsFrame = QtWidgets.QFrame(self.FrameGeneral)
        self.ButtonsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ButtonsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ButtonsFrame.setObjectName("ButtonsFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ButtonsFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.StartingSpeedLabel = QtWidgets.QLabel(self.ButtonsFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setBold(True)
        font.setWeight(75)
        self.StartingSpeedLabel.setFont(font)
        self.StartingSpeedLabel.setStyleSheet(
            "background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.2 rgba("
            "255, 0, 0, 180), stop:1 rgba(0, 0, 0, 255));\n "
            "color:rgba(255,255,255,200)")
        self.StartingSpeedLabel.setObjectName("StartingSpeedLabel")
        self.verticalLayout_2.addWidget(self.StartingSpeedLabel)
        self.SpeedTextEdit = QtWidgets.QTextEdit(self.ButtonsFrame)
        self.SpeedTextEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.SpeedTextEdit.setStyleSheet("background-color:rgba(255,255,255,130);\n"
                                         "color:white")
        self.SpeedTextEdit.setObjectName("SpeedTextEdit")
        self.verticalLayout_2.addWidget(self.SpeedTextEdit)
        self.MassLabel = QtWidgets.QLabel(self.ButtonsFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setBold(True)
        font.setWeight(75)
        self.MassLabel.setFont(font)
        self.MassLabel.setStyleSheet(
            "background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.2 rgba("
            "255, 0, 0, 180), stop:1 rgba(0, 0, 0, 255));\n "
            "color:rgba(255,255,255,200)")
        self.MassLabel.setObjectName("MassLabel")
        self.verticalLayout_2.addWidget(self.MassLabel)
        self.MassTextEdit = QtWidgets.QTextEdit(self.ButtonsFrame)
        self.MassTextEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.MassTextEdit.setStyleSheet("background-color:rgba(255,255,255,130);\n"
                                        "color:white")
        self.MassTextEdit.setObjectName("MassTextEdit")
        self.verticalLayout_2.addWidget(self.MassTextEdit)
        self.HeightLAbel = QtWidgets.QLabel(self.ButtonsFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setBold(True)
        font.setWeight(75)
        self.HeightLAbel.setFont(font)
        self.HeightLAbel.setStyleSheet(
            "background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.2 rgba("
            "255, 0, 0, 180), stop:1 rgba(0, 0, 0, 255));\n "
            "color:rgba(255,255,255,200)")
        self.HeightLAbel.setObjectName("HeightLAbel")
        self.verticalLayout_2.addWidget(self.HeightLAbel)
        self.HeightTextEdit = QtWidgets.QTextEdit(self.ButtonsFrame)
        self.HeightTextEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.HeightTextEdit.setStyleSheet("background-color:rgba(255,255,255,130);\n"
                                          "color:white\n"
                                          "")
        self.HeightTextEdit.setObjectName("HeightTextEdit")
        self.verticalLayout_2.addWidget(self.HeightTextEdit)

        "load simulation button"

        self.LoadSImulationBUttom = QtWidgets.QPushButton(self.ButtonsFrame,clicked=lambda:self.loadbuttonpressed())
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.LoadSImulationBUttom.setFont(font)
        self.LoadSImulationBUttom.setStyleSheet(
            "QPushButton {background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, "
            "stop:0.2 rgba(255, 0, 0, 180), stop:1 rgba(0, 0, 0, 255));\n "
            "color:rgba(255,255,255,150);\n"
            "border-style:solid;}\n"
            "QPushButton:pressed {background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, "
            "fy:0.5, stop:0.2 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));\n "
            "color:rgba(255,255,255,255);\n"
            "border-style:solid;}")
        self.LoadSImulationBUttom.setObjectName("LoadSImulationBUttom")
        self.verticalLayout_2.addWidget(self.LoadSImulationBUttom)
        self.horizontalLayout_3.addWidget(self.ButtonsFrame)
        #
        "simulation Frame"

        self.SimulatorFrame = QtWidgets.QFrame(self.FrameGeneral)
        self.SimulatorFrame.setStyleSheet("border-style:inset;\n"
                                          "border-color:rgba(255,0,0,130);\n"
                                          "border-width:5")
        self.SimulatorFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SimulatorFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.SimulatorFrame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.graphicalview = view()
        self.graphicalview.setParent(self.SimulatorFrame)
        self.horizontalLayout_4.addWidget(self.graphicalview)

        self.horizontalLayout_3.addWidget(self.SimulatorFrame)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)
        self.verticalLayout.addWidget(self.FrameGeneral)
        self.verticalLayout_3.addWidget(self.frame)
        #
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, FreeFall):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("FreeFall", "FreeFall"))
        self.FreeFall_2.setText(_translate("FreeFall", "<html><head/><body><p><span style=\" "
                                                       "font-size:14pt;\">PYSIMULATOR<br/>FreeFall</span></p></body"
                                                       "></html>"))
        self.Exitbuttom.setText(_translate("FreeFall", "BACK"))
        self.StartingSpeedLabel.setText(_translate("FreeFall", "<html><head/><body><p align=\"center\"><span style=\" "
                                                               "font-size:10pt;\">STARTING SPEED <br/>Vo("
                                                               "m/s)</span></p></body></html>"))
        self.MassLabel.setText(_translate("FreeFall", "<html><head/><body><p align=\"center\"><span style=\" "
                                                      "font-size:10pt;\">MASS(kg)</span></p></body></html>"))
        self.HeightLAbel.setText(_translate("FreeFall", "<html><head/><body><p align=\"center\"><span style=\" "
                                                        "font-size:10pt;\">HEIGHT(m)</span></p></body></html>"))
        self.LoadSImulationBUttom.setText(_translate("FreeFall", "LOAD"))


    def exitbutton(self, Main_W):
        Main_W.show()
        self.close()
        pass

    def loadbuttonpressed(self):
        self.graphicalview.loadStartingData()
        if self.graphicalview.TimeBar==None:
            self.graphicalview.createTimeBar()
            self.graphicalview.createMovingObject()
        self.graphicalview.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicalview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
