from PySide6.QtWidgets import QGraphicsItem,QGraphicsSimpleTextItem
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import QObject, Signal

from config import *

class Clock(QGraphicsSimpleTextItem):
    def __init__(self):
        super().__init__()

        f = self.font()
        f.setPointSize(24)
        f.setWeight(QFont.Weight.Normal)
        self.setFont(f)

        self.setText('time: 000')

