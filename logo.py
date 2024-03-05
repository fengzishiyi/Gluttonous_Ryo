from PySide6.QtWidgets import QGraphicsItem,QGraphicsPixmapItem
from PySide6.QtGui import QPixmap

from config import *
from signals import Signals

class Logo(QGraphicsPixmapItem):
    def __init__(self):
        super().__init__()

        self.status = Status.STOP
        self.signals = Signals()

        self.load_images()
        self.setOpacity(0.8)

    def load_images(self):
        self.run = QPixmap(LOGO_RUN)

        self.stop = QPixmap(LOGO_STOP)

    def turn_stop(self):
        self.status = Status.STOP
        self.setPixmap(self.stop)

    def turn_run(self):
        self.status = Status.RUN
        self.setPixmap(self.run)

    @property
    def is_run(self):
        return self.status == Status.RUN

    def mousePressEvent(self, event):
        self.signals.clicked.emit()
        self.update_pix()
        # super().mousePressEvent(event)

    def update_pix(self):
        if not self.is_run:
            self.turn_run()
        else:
            self.turn_stop()

        # print("logo-status: ", self.status)




