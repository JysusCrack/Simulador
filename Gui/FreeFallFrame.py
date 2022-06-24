
from PyQt5 import QtCore, QtGui, QtWidgets


class FreeFallFrame(QtWidgets.QFrame):

    def __init__(self, Qparent):
        super(FreeFallFrame, self).__init__(Qparent)
        self.bottomstyle1 = """QRadioButton{
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

        self.layout = QtWidgets.QHBoxLayout(self)

        self.frame1 = QtWidgets.QFrame(self)
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1Layout = QtWidgets.QVBoxLayout(self.frame1)
        self.starting_speed_label = QtWidgets.QLabel(self.frame1)
        self.starting_speed_label.setFont(self.labelFont)
        self.starting_speed_label.setStyleSheet(self.labelStyle)
        self.starting_speed_label.setObjectName("StartingSpeedLabel")
        self.frame1Layout.addWidget(self.starting_speed_label)
        self.speed_text_edit = QtWidgets.QTextEdit(self.frame1)
        self.speed_text_edit.setMaximumSize(QtCore.QSize(16000, 40))
        self.speed_text_edit.setStyleSheet(self.labelStyle)
        self.speed_text_edit.setObjectName("SpeedTextEdit")
        self.frame1Layout.addWidget(self.speed_text_edit)
        self.layout.addWidget(self.frame1)

        "mass frame"
        self.frame2 = QtWidgets.QFrame(self)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2Layout = QtWidgets.QVBoxLayout(self.frame2)

        self.mass_label = QtWidgets.QLabel(self.frame2)
        self.mass_label.setFont(self.labelFont)
        self.mass_label.setStyleSheet(self.labelStyle)
        self.mass_label.setObjectName("MassLabel")
        self.frame2Layout.addWidget(self.mass_label)
        self.mass_text_edit = QtWidgets.QTextEdit(self.frame2)
        self.mass_text_edit.setMaximumSize(QtCore.QSize(16000, 40))
        self.mass_text_edit.setStyleSheet(self.labelStyle)
        self.mass_text_edit.setObjectName("MassTextEdit")
        self.frame2Layout.addWidget(self.mass_text_edit)
        self.layout.addWidget(self.frame2)

        "height frame"

        self.frame3 = QtWidgets.QFrame(self)
        self.frame3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame3Layout = QtWidgets.QVBoxLayout(self.frame3)

        self.height_label = QtWidgets.QLabel(self.frame3)
        self.height_label.setFont(self.labelFont)
        self.height_label.setStyleSheet(self.labelStyle)
        self.height_label.setObjectName("HeightLAbel")
        self.frame3Layout.addWidget(self.height_label)
        self.height_text_edit = QtWidgets.QTextEdit(self.frame3)
        self.height_text_edit.setMaximumSize(QtCore.QSize(16000, 40))
        self.height_text_edit.setStyleSheet(self.labelStyle)
        self.height_text_edit.setObjectName("HeightTextEdit")
        self.frame3Layout.addWidget(self.height_text_edit)
        self.layout.addWidget(self.frame3)

        self.frame_4 = QtWidgets.QFrame(self)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1_Layout = QtWidgets.QVBoxLayout(self.frame_4)

        self.gravity_label = QtWidgets.QLabel(self.frame_4)
        self.gravity_label.setFont(self.labelFont)
        self.gravity_label.setStyleSheet(self.labelStyle)
        self.gravity_label.setObjectName("MassLabel")
        self.frame_1_Layout.addWidget(self.gravity_label)
        self.gravity_text_edit = QtWidgets.QTextEdit(self.frame_4)
        self.gravity_text_edit.setMaximumSize(QtCore.QSize(16000, 40))
        self.gravity_text_edit.setStyleSheet(self.labelStyle)
        self.gravity_text_edit.setObjectName("MassTextEdit")
        self.frame_1_Layout.addWidget(self.gravity_text_edit)
        self.layout.addWidget(self.frame_4)

        "translate or set text on labels"
        _translate = QtCore.QCoreApplication.translate

        self.gravity_label.setText(_translate("FreeFall", "<html><head/><body><p align=\"center\">GRAVITY"
                                                          "<br/>G("
                                                          "m/s²)</span></p></body></html>"))
        self.starting_speed_label.setText(
            _translate("FreeFall", "<html><head/><body><p align=\"center\">STARTING SPEED "
                                   "<br/>Vo( "
                                   "m/s)</span></p></body></html>"))
        self.mass_label.setText(_translate("FreeFall", "<html><head/><body><p align=\"center\">MASS("
                                                       "kg)</span></p></body></html>"))
        self.height_label.setText(_translate("FreeFall", "<html><head/><body><p align=\"center\">HEIGHT("
                                                         "m)</span></p></body></html>"))

    def getText(self):
        starting_speed = self.speed_text_edit.toPlainText()
        mass = self.mass_text_edit.toPlainText()
        height = self.height_text_edit.toPlainText()
        try:
            lista = float(starting_speed), float(mass), float(height)
        except ValueError:
            return None
        return lista

