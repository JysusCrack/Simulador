# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MRUA.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class MruaFrame(QtWidgets.QFrame):
    def __init__(self, Qparent):
        super(MruaFrame, self).__init__(Qparent)
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

        _translate = QtCore.QCoreApplication.translate

        # frame1

        self.frame1 = QtWidgets.QFrame(self)
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1layout = QtWidgets.QVBoxLayout(self.frame1)

        self.acceleration_label = QtWidgets.QLabel(self.frame1)
        self.acceleration_label.setFont(self.labelFont)
        self.acceleration_label.setStyleSheet(self.labelStyle)
        self.frame1layout.addWidget(self.acceleration_label)
        self.acceleration_text_edit = QtWidgets.QTextEdit(self.frame1)
        self.acceleration_text_edit.setStyleSheet(self.labelStyle)
        self.acceleration_text_edit.setMaximumSize(16000, 40)
        self.frame1layout.addWidget(self.acceleration_text_edit)
        self.layout.addWidget(self.frame1)

        # frame 2

        self.frame2 = QtWidgets.QFrame(self)
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2layout = QtWidgets.QVBoxLayout(self.frame2)
        self.mass_label = QtWidgets.QLabel(self.frame2)
        self.mass_label.setFont(self.labelFont)
        self.mass_label.setStyleSheet(self.labelStyle)
        self.frame2layout.addWidget(self.mass_label)
        self.mass_text_edit = QtWidgets.QTextEdit(self.frame2)
        self.mass_text_edit.setStyleSheet(self.labelStyle)
        self.mass_text_edit.setMaximumSize(16000, 40)
        self.frame2layout.addWidget(self.mass_text_edit)
        self.layout.addWidget(self.frame2)

        # frame3

        self.frame3 = QtWidgets.QFrame(self)
        self.frame3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame3layout = QtWidgets.QVBoxLayout(self.frame3)
        self.starting_speed_label = QtWidgets.QLabel(self.frame3)
        self.starting_speed_label.setFont(self.labelFont)
        self.starting_speed_label.setStyleSheet(self.labelStyle)
        self.frame3layout.addWidget(self.starting_speed_label)
        self.starting_speed_text_edit = QtWidgets.QTextEdit(self.frame3)
        self.starting_speed_text_edit.setStyleSheet(self.labelStyle)
        self.starting_speed_text_edit.setMaximumSize(16000, 40)
        self.frame3layout.addWidget(self.starting_speed_text_edit)
        self.layout.addWidget(self.frame3)

        # frame 4

        self.frame4 = QtWidgets.QFrame(self)
        self.frame4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame4layout = QtWidgets.QVBoxLayout(self.frame4)
        self.starting_position_label = QtWidgets.QLabel(self.frame4)
        self.starting_position_label.setFont(self.labelFont)
        self.starting_position_label.setStyleSheet(self.labelStyle)
        self.frame4layout.addWidget(self.starting_position_label)
        self.starting_position_text_edit = QtWidgets.QTextEdit(self.frame4)
        self.starting_position_text_edit.setStyleSheet(self.labelStyle)
        self.starting_position_text_edit.setMaximumSize(16000, 40)
        self.frame4layout.addWidget(self.starting_position_text_edit)
        self.layout.addWidget(self.frame4)
        self.layout.setStretch(0, 1)
        self.layout.setStretch(1, 1)
        self.layout.setStretch(2, 1)
        self.layout.setStretch(3, 1)

        # translations

        self.acceleration_label.setText(_translate("MRUA", "<html><head/><body><p align=\"center\">ACCELERATION"
                                                           "<br/>A(m/s²)</span></p></body></html>"))
        self.mass_label.setText(
            _translate("MRUA", "<html><head/><body><p align=\"center\">MASS</span></p></body></html>"))
        self.starting_speed_label.setText(
            _translate("MRUA", "<html><head/><body><p align=\"center\">STARTING SPEED"
                               "<br/>Vo(m/s)</span></p></body></html>"))
        self.starting_position_label.setText(
            _translate("MRUA", "<html><head/><body><p align=\"center\">STARTING POSITION"
                               "<br/>Xo(m)</span></p></body></html>"))

    def getText(self):
        acceleration = self.acceleration_text_edit.toPlainText()
        starting_speed = self.starting_speed_text_edit.toPlainText()
        mass = self.mass_text_edit.toPlainText()
        starting_position = self.starting_position_text_edit.toPlainText()
        try:
            lista: list[float] = float(acceleration), float(starting_speed), float(mass), float(starting_position)

        except ValueError:
            return None
        return lista


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    frame = MruaFrame(widget)
    widget.show()
    sys.exit(app.exec_())