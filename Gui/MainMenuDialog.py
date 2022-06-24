# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtCore import Qt

from FreeFallFrame import FreeFallFrame
from MruaFrame import MruaFrame
from McuaFrames import McuaFrame1, McuaFrame2
from PyQt5 import QtCore, QtGui, QtWidgets
from ErrorBox import ErrorBoxWidget
from GraphicSimulator1 import Program


class Ui_MainSimulatorWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_MainSimulatorWindow, self).__init__()
        self.currentButton: str
        self.currentButton = None
        self.buttons_frame = None

        # error widget
        self.typical_error_message = ErrorBoxWidget("<html><head/><body><p align=\"center\">There's something wrong :("
                                                    "<br/>Please check:\n"
                                                    "<br/>All values should be numbers\n"
                                                    "<br/>Only one number per slot\n"
                                                    "<br/>Decimals might be separated by a dot\n</p></body></html>")

        self.bottom_style_1 = """QRadioButton{
                        background-color: rgba(255,0,0,130);
                        color: rgba(255,255,255,180);
                        border-radius:10
                        }

                        QRadioButton::indicator {
                        width: 11px;
                        height: 11px;
                        border-radius: 5px;
                        color:none;
                        }

                        QRadioButton:checked{
                        background-color:rgba(255,0,0,255);
                        color:white;
                        }"""

        "labels style"

        self.labelStyle = "background-color:rgba(255,0,0,130);color:rgba(255,255,255," \
                          "180);border-style:solid;border-radius:5"

        "Font"

        self.labelFont = QtGui.QFont()
        self.labelFont.setFamily("Segoe UI Black")
        self.labelFont.setPointSize(15)
        self.labelFont.setBold(True)
        self.labelFont.setWeight(75)

        "Push Button Style"

        self.pushButtonStyle = "QPushButton{background-color:rgba(255,0,0,130);color:rgba(255,255,255," \
                               "180);border-style:solid;border-radius:5}\n " \
                               "QPushButton:pressed{background-color:rgba(255,0,0,255);color:rgba(255,255,255," \
                               "255);border-style:solid;border-radius:5}"

        "main start"
        self.setObjectName("MainSimulatorWindow")
        self.resize(650, 600)
        self.setWindowIcon(QtGui.QIcon("images/icons8-newton-64.png"))
        self.simulator = QtWidgets.QWidget(self)
        self.simulator.setObjectName("Simulador")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.simulator)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        "frame1"
        self.frame = QtWidgets.QFrame(self.simulator)
        self.frame.setStyleSheet("background-color:black;\n"
                                 "border-style:none")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        "frame2"

        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_2.setStyleSheet("background-color:none")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setFont(self.labelFont)
        self.label.setStyleSheet("color:white")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        "exit button"

        self.EXITbuttom = QtWidgets.QPushButton(self.frame_2)
        self.EXITbuttom.setFont(self.labelFont)
        self.EXITbuttom.setStyleSheet(self.pushButtonStyle)
        self.EXITbuttom.setObjectName("EXITbuttom")
        self.EXITbuttom.clicked.connect(self.exitButton)

        self.horizontalLayout.addWidget(self.EXITbuttom)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("background-color:none")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setMaximumSize(16000, 50)
        self.frame_4.setStyleSheet("border-style:none\n"
                                   "")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        "Colition radio button"

        """self.COLITIONbuttom = QtWidgets.QRadioButton(self.frame_4)
        self.COLITIONbuttom.setFont(self.labelFont)
        self.COLITIONbuttom.setStyleSheet(self.bottomstyle1)
        self.horizontalLayout_2.addWidget(self.COLITIONbuttom)"""

        "MCUA button"

        self.MCUAbuttom = QtWidgets.QRadioButton(self.frame_4)
        self.MCUAbuttom.setObjectName("McuaButton")
        self.MCUAbuttom.setFont(self.labelFont)
        self.MCUAbuttom.setStyleSheet(self.bottom_style_1)
        self.horizontalLayout_2.addWidget(self.MCUAbuttom)

        "MRUA button"

        self.MRUAbuttom = QtWidgets.QRadioButton(self.frame_4)
        self.MRUAbuttom.setObjectName("MruaButton")
        self.MRUAbuttom.setFont(self.labelFont)
        self.MRUAbuttom.setStyleSheet(self.bottom_style_1)
        self.horizontalLayout_2.addWidget(self.MRUAbuttom)

        "FreeFall button"

        self.FreeFallbuttom = QtWidgets.QRadioButton(self.frame_4)
        self.FreeFallbuttom.setObjectName("FreeFallButton")
        self.FreeFallbuttom.setFont(self.labelFont)
        self.FreeFallbuttom.setStyleSheet(self.bottom_style_1)
        self.horizontalLayout_2.addWidget(self.FreeFallbuttom)

        "buttons actions"

        """self.COLITIONbuttom.toggled.connect(lambda: self.collitionbutton(self.COLITIONbuttom.objectName()))"""
        self.MCUAbuttom.toggled.connect(lambda: self.mcua_button(self.MCUAbuttom.objectName()))
        self.MRUAbuttom.toggled.connect(lambda: self.mrua_button(self.MRUAbuttom.objectName()))
        self.FreeFallbuttom.toggled.connect(lambda: self.free_fall_button(self.FreeFallbuttom.objectName()))

        self.verticalLayout_5.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setStyleSheet("border-style:none")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5_layout = QtWidgets.QVBoxLayout(self.frame_5)
        self.frame_5_layout.setSpacing(0)

        # buttons frame

        self.buttons_frame = QtWidgets.QFrame(self.frame_5)
        self.buttons_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.buttons_frame_2 = QtWidgets.QFrame(self.frame_5)
        self.buttons_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttons_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)

        self.buttons_video_frame = QtWidgets.QFrame(self.frame_5)
        self.buttons_video_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttons_video_frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frame_5_layout.insertWidget(0, self.buttons_frame)
        self.frame_5_layout.insertWidget(1, self.buttons_video_frame)
        self.frame_5_layout.insertWidget(2, self.buttons_frame_2)

        # Load Button Frame

        self.load_button_frame = QtWidgets.QFrame(self.frame_5)
        self.load_button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.load_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.load_button_frame_layout = QtWidgets.QHBoxLayout(self.load_button_frame)

        self.load_button = QtWidgets.QPushButton(self.load_button_frame, clicked=lambda: self.loadButton())
        self.load_button.setFont(self.labelFont)
        self.load_button.setStyleSheet(self.pushButtonStyle)
        self.load_button_frame_layout.addWidget(self.load_button)
        self.frame_5_layout.insertWidget(3, self.load_button_frame)
        self.frame_5_layout.setStretch(0, 1)
        self.frame_5_layout.setStretch(1, 10)
        self.frame_5_layout.setStretch(2, 1)
        self.frame_5_layout.setStretch(3, 1)

        self.verticalLayout_5.addWidget(self.frame_5)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame)
        self.setCentralWidget(self.simulator)

        self.retranslateUi(self)
        self.showMaximized()

    @staticmethod
    def exitButton():
        sys.exit()

    def free_fall_button(self, but):
        self.currentButton = but
        self.frame_5_layout.removeWidget(self.buttons_frame)

        # frame
        self.buttons_frame = FreeFallFrame(self.frame_5)
        self.frame_5_layout.insertWidget(0, self.buttons_frame, alignment=Qt.AlignTop)

    def mcua_button(self, but):
        self.currentButton = but
        # frame
        self.frame_5_layout.removeWidget(self.buttons_frame)
        self.frame_5_layout.removeWidget(self.buttons_frame_2)

        self.buttons_frame = McuaFrame1(self.frame_5)
        self.buttons_frame_2 = McuaFrame2(self.frame_5)
        self.frame_5_layout.insertWidget(0, self.buttons_frame, alignment=Qt.AlignTop)
        self.frame_5_layout.insertWidget(2, self.buttons_frame_2, alignment=Qt.AlignBottom)

    def mrua_button(self, but):
        self.currentButton = but
        self.frame_5_layout.removeWidget(self.buttons_frame)
        self.frame_5_layout.removeWidget(self.buttons_frame_2)

        # frame
        self.buttons_frame = MruaFrame(self.frame_5)
        self.frame_5_layout.insertWidget(0, self.buttons_frame, alignment=Qt.AlignTop)

    def loadButton(self):
        if self.currentButton == "FreeFallButton":
            values = self.buttons_frame.getText()
            values_2 = self.buttons_frame_2.getText()
            if values is not None and values_2 is not None:
                temp_size=(self.buttons_video_frame.size().width(), self.buttons_video_frame.height())
                print((values[0],values[1],values[2],values_2,[500,900]))
                program = Program(values[0],values[1],values[2],values_2,[500,900])
                program.run()
                pass
            else:
                self.typical_error_message.show()
            pass
        elif self.currentButton == "MruaButton":
            values = self.buttons_frame.getText()
            if values is not None :
                pass
            else:
                self.typical_error_message.show()
            pass
        elif self.currentButton == "McuaButton":
            values: list = self.buttons_frame.getText()
            values2: list = self.buttons_frame_2.getText()
            if values is not None ^ values2 is not None:
                pass
            else:
                self.typical_error_message.show()
            pass
        elif self.currentButton == "":
            pass
        elif self.currentButton is None:
            self.message = ErrorBoxWidget("<p align=\"center\">SELECT<br/>MODE</p>")
            self.message.show()

    def retranslateUi(self, MainSimulatorWindow):
        _translate = QtCore.QCoreApplication.translate
        MainSimulatorWindow.setWindowTitle(_translate("MainSimulatorWindow", "PYSIMULATOR"))
        self.label.setText(_translate("MainSimulatorWindow",
                                      "<html><head/><body><p>PYSIMULATOR</span></p></body></html>"))
        self.EXITbuttom.setText(_translate("MainSimulatorWindow", "Exit"))
        """self.COLITIONbuttom.setText(_translate("MainSimulatorWindow", "COLITIONS"))"""
        self.MCUAbuttom.setText(_translate("MainSimulatorWindow", "MCUA"))
        self.MRUAbuttom.setText(_translate("MainSimulatorWindow", "MRUA"))
        self.FreeFallbuttom.setText(_translate("MainSimulatorWindow", "FreeFall"))
        self.load_button.setText(_translate("MainSimulatorWindow", "LOAD"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainSimulatorWindow = Ui_MainSimulatorWindow()
    MainSimulatorWindow.show()
    sys.exit(app.exec_())
