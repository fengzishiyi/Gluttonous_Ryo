import sys

from PySide6.QtWidgets import QApplication,QGraphicsScene,QGraphicsView
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self)

        self.view.setScene(self.scene)
        self.view.setDragMode(QGraphicsView.RubberBandDrag)

        self.setMinimumWidth(500)
        self.setMinimumHeight(500)

        self.setCentralWidget(self.view)
        self.setWindowTitle('Gluttonous_Ryo')

        self.show()

app = QApplication(sys.argv)
w = MainWindow()
app.exec()
