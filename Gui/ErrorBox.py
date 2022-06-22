from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie, QFont

bottom_style_1 = """QPushButton{
                        background-color: rgba(255,0,0,130);
                        color: rgba(255,255,255,180);
                        border-radius:10
                        }

                        QPushButton:pressed{
                        background-color:rgba(255,0,0,255);
                        color:white;
                        }"""

# label style

labelStyle = "background-color:rgba(255,0,0,130);color:rgba(255,255,255," \
             "180);border-style:solid;border-radius:5;  text-align: center;"

# font

labelFont = QtGui.QFont()
labelFont.setFamily("Segoe UI Black")
labelFont.setPointSize(15)
labelFont.setBold(True)
labelFont.setWeight(75)

# Push Button Style

pushButtonStyle = "QPushButton{background-color:rgba(255,0,0,130);color:rgba(255,255,255," \
                  "180);border-style:solid;border-radius:5}\n " \
                  "QPushButton:pressed{background-color:rgba(255,0,0,255);color:rgba(255,255,255," \
                  "255);border-style:solid;border-radius:5}"


_translate = QtCore.QCoreApplication.translate

class ErrorBoxWidget(QtWidgets.QWidget):
    def __init__(self, message):
        super(ErrorBoxWidget, self).__init__()

        self.setWindowTitle("ERROR")
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(0)
        self.setStyleSheet("background-color:rgba(22,5,12,255)")

        # message
        self.label2 = QtWidgets.QLabel(self)
        if message is not None:
            self.label2.setText(_translate("ERRORBOX", message))
        self.label2.setFont(labelFont)
        self.label2.setStyleSheet(labelStyle)
        self.label2.setContentsMargins(30, 30, 30, 30)
        self.layout.addWidget(self.label2)

        # Gif Player

        self.label1 = QtWidgets.QLabel(self)
        self.gif = QMovie('images/RedCal.gif')
        self.label1.setMovie(self.gif)
        self.layout.addWidget(self.label1,alignment=Qt.AlignCenter)
        self.gif.start()

        # Ok button

        self.OkButton2 = QtWidgets.QPushButton(self, clicked=lambda: self.close())
        self.OkButton2.setFont(labelFont)
        self.OkButton2.setText("Ok")
        self.OkButton2.setStyleSheet(bottom_style_1)
        self.layout.addWidget(self.OkButton2)
        self.layout.setStretch(0, 1)
        self.layout.setStretch(1, 5)
        self.layout.setStretch(2, 1)
        # verticallayout



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    error_box = ErrorBoxWidget("holis")
    error_box.show()
    sys.exit(app.exec_())
