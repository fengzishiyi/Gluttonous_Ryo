from PySide6.QtWidgets import QGraphicsItem,QGraphicsPixmapItem
from PySide6.QtGui import QPixmap

from config import *

class LogoItem(QGraphicsPixmapItem):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pix = QPixmap(LOGO_STOP)
        # self.width = 64
        # self.height = 64
        self.setPixmap(self.pix)
        self.setOpacity(0.8)
        self.setFlag(QGraphicsItem.ItemIsSelectable)