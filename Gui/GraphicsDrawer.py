import sys

from PyQt5.QtGui import QResizeEvent
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsRectItem
from PyQt5.QtCore import Qt, QPointF, QRect, QRectF


class TimeBar(QGraphicsRectItem):
    def __init__(self, lista, size):
        super(TimeBar, self).__init__(0,0, size[0], size[1])
        self.startingSize = size[0], size[1]
        self.startingPos = lista
        self.setPos(lista[0], lista[1])
        self.setPen(Qt.white)
        self.setBrush(Qt.red)
        self.setAcceptHoverEvents(True)

    def setNewScale(self, scalex: float, scaley: float) -> None:
        pass


class TimeBarCursor(QGraphicsRectItem):
    def __init__(self, lista, size, width):
        super(TimeBarCursor, self).__init__(0, 0, size[0], size[1])
        self.startingSize = size
        self.barWidth = width
        self.startingPos= lista[0], lista[1]
        self.setPos(lista[0], lista[1])
        self.setPen(Qt.white)
        self.setBrush(Qt.white)
        self.setAcceptHoverEvents(True)

    def setNewScale(self, scalex: float, scaley: float) -> None:
        pass

    # mouse hover events

    def hoverEnterEvent(self, event: 'QGraphicsSceneHoverEvent') -> None:
        app.instance().setOverrideCursor(Qt.OpenHandCursor)

    def hoverLeaveEvent(self, event: 'QGraphicsSceneHoverEvent') -> None:
        app.instance().restoreOverrideCursor()

    # mouse clicked events

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        pass

    def mouseMoveEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        passPos = event.lastScenePos()
        pressentPos = event.scenePos()
        objectScenePos = self.scenePos()
        pressentPosX = pressentPos.x() - passPos.x() + objectScenePos.x()
        if self.startingPos[0] <= pressentPosX <= self.barWidth:
            self.setPos(QPointF(pressentPosX, self.y()))

    def mouseReleaseEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        pass


class MovingObject(QGraphicsEllipseItem):

    def __init__(self, lista, size):
        super(MovingObject, self).__init__(0, 0, size[0], size[1])
        self.startingSize = size
        self.startingPos=lista
        self.setPos(lista[0], lista[1])
        self.setBrush(Qt.red)
        self.setAcceptHoverEvents(True)

    def setNewScale(self, scalex: float, scaley: float) -> None:
        self.setPos(self.startingPos[0]*scalex,self.startingPos[1]*scaley)


class view(QGraphicsView):
    def __init__(self):
        super(view, self).__init__()
        self.startingRect = None
        self.movingObject = None
        self.TimeBar = None
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setMinimumSize(400, 400)
        self.setStyleSheet("border-style:solid;border-color:rgba(0,0,0,0)")

    def loadStartingData(self):
        self.startingRect = self.rect()

    def resizeEvent(self, event: QResizeEvent) -> None:
        if self.startingRect is not None:
            ScaleX = self.size().width() / self.startingRect.width()
            ScaleY = self.size().height() / self.startingRect.height()
            print(ScaleX,ScaleY)
        if self.TimeBar is not None:
            self.TimeBar.setNewScale(ScaleX,ScaleY)
            self.TimeBarCursor.setNewScale(ScaleX,ScaleY)
        if self.movingObject is not None:
            self.movingObject.setNewScale(ScaleX,ScaleY)

    def createTimeBar(self):
        TimeBarSize = self.size().width() - 40, self.size().height() / 12
        TimeBarPos = self.pos().x() + 20, self.pos().y() + 10
        self.TimeBar = TimeBar(TimeBarPos, TimeBarSize)
        self.scene.addItem(self.TimeBar)
        TimeBarCursorSize = self.size().width() / 20, self.size().height() / 12
        TimeBarCursorPos = self.pos().x() + 20, self.pos().y() + 10
        TimeBarCursorLimit = TimeBarPos[0] + TimeBarSize[0] - TimeBarCursorSize[0]
        self.TimeBarCursor = TimeBarCursor(TimeBarCursorPos, TimeBarCursorSize, TimeBarCursorLimit)
        self.scene.addItem(self.TimeBarCursor)

    def createMovingObject(self):
        startingSize = self.size().width() / 12, self.size().height() / 12
        startingPos = self.pos().x() + self.size().width() / 2 - 40, self.pos().y() + self.size().height() - \
                      startingSize[1] - 40
        self.movingObject = MovingObject(startingPos, startingSize)
        self.scene.addItem(self.movingObject)


app = QApplication
