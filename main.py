import sys

from PySide6.QtWidgets import QApplication,QGraphicsScene,QGraphicsView
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon

from config import *

from scene import Scene
from view import View


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.scene = Scene(self)
        self.view = View(self.scene, self)

        self.setGeometry(160, 50, SCENE_WIDTH + 5, SCENE_HEIGHT + 5)
        self.setFixedSize(self.width(), self.height())
        self.setCentralWidget(self.view)
        self.setWindowTitle('Gluttonous_Ryo')
        self.show()

app = QApplication(sys.argv)
w = MainWindow()
app.exec()
