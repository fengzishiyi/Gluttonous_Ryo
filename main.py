import sys
import time

from PySide6.QtWidgets import QApplication,QGraphicsScene,QGraphicsView
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon

from config import *

from scene import Scene
from view import View
from logo import Logo
from clock import Clock


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.status = Status.READY
        self.time_cnt = 0

        view = View()
        self.scene = Scene()

        view.setScene(self.scene)

        self.logo = Logo()
        self.scene.addItem(self.logo)
        self.logo.turn_stop()
        self.logo.signals.clicked.connect(self.trigger)
        self.logo.setPos(500,0)

        self.clock = Clock()
        self.scene.addItem(self.clock)
        self.clock.setPos(20,20)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)


        self.setGeometry(160, 50, SCENE_WIDTH + 5, SCENE_HEIGHT + 5)
        self.setFixedSize(self.width(), self.height())
        self.setCentralWidget(view)
        self.setWindowTitle('Gluttonous_Ryo')
        self.show()

    def update_timer(self):
        if self.status == Status.RUN:
            n_secs = self.time_cnt - 0
            print('time: ', n_secs)
            self.time_cnt += 1
            self.clock.setText("time: %03d" % n_secs)


    def trigger(self, *args):
        if self.status == Status.READY:
            # First click.
            self.update_status(Status.RUN)
            # Start timer.
        elif self.status == Status.STOP:
            self.update_status(Status.RUN)
            self.timer.start()
        elif self.status == Status.RUN:
            self.update_status(Status.STOP)
            self.timer.stop()

    def update_status(self, status):
        self.status = status
        print('main-status: ',self.status)


app = QApplication(sys.argv)
w = MainWindow()
app.exec()
