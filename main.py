import sys
import time

# pyinstaller --windowed --add-data "icons:icons" --add-data "sounds:sounds" -n "Gluttonous_Ryo" -i D:\my_python\Gluttonous_Ryo\icons\icon32.ico main.py

from PySide6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsSimpleTextItem
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon, QFont

from config import *

from scene import Scene
from view import View
from logo import Logo
from snake import Snake
from bood import Bood
from nood import Nood
from kood import Kood
from sound import AudioSource

try:
    from ctypes import windll # Only exists on Windows.
    myappid = "FengZiShiYi"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.luck = 3
        self.status = Status.STOP
        self.time = 0
        self.point = 0

        self.scene = Scene()
        view = View()


        view.setScene(self.scene)

        self.logo = Logo()
        self.scene.addItem(self.logo)
        self.logo.turn_stop()
        self.logo.signals.clicked.connect(self.trigger)
        self.logo.setPos(SCENE_WIDTH/2 - self.logo.boundingRect().width()/2, BLOCK_WIDTH/2)

        self.clock = QGraphicsSimpleTextItem()
        self.score = QGraphicsSimpleTextItem()
        self.speed_l = QGraphicsSimpleTextItem()

        f = self.font()
        f.setPointSize(24)
        f.setWeight(QFont.Weight.Normal)

        self.clock.setFont(f)
        self.score.setFont(f)
        self.speed_l.setFont(f)
        self.clock.setOpacity(0.3)
        self.score.setOpacity(0.3)
        self.speed_l.setOpacity(0.3)
        self.clock.setText('time: 000')
        self.score.setText('score: 000')
        self.speed_l.setText('speed: 50')
        self.scene.addItem(self.clock)
        self.scene.addItem(self.score)
        self.scene.addItem(self.speed_l)
        self.clock.setPos(35, 30)
        self.score.setPos(205, 30)
        self.speed_l.setPos(390, 30)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)

        self.audio = AudioSource()

        self.snake = Snake(self)
        self.snake.init_snake()
        self.snake.signals.eat.connect(
            self.update_eat
        )
        self.dir_temp = self.snake.dir

        self.speed = QTimer(self)
        self.speed.timeout.connect(self.update_game)
        self.speed.start(INTERVAL)

        self.food_pos_list = [0] * 3
        self.bood = Bood(self)
        self.nood = Nood(self)
        self.kood = Kood(self)
        self.bood.spawn()
        self.nood.spawn()
        self.kood.spawn()

        self.setGeometry(160, 50, SCENE_WIDTH + 5, SCENE_HEIGHT + 5)
        self.setFixedSize(self.width(), self.height())
        self.setCentralWidget(view)
        self.setWindowTitle('Gluttonous_Ryo')
        self.setWindowIcon(QIcon(Paths.icon('icon64.ico')))
        self.show()

    def update_eat(self, i, j):
        if self.time % self.luck == 0:
            self.snake.do_pills(i, j)
            self.audio.play_audio(i, j)

    def trigger(self, *args):
        if self.status == Status.STOP:
            self.update_status(Status.RUN)
            self.timer.start()
        elif self.status == Status.RUN:
            self.update_status(Status.STOP)
            self.timer.stop()

    def update_game(self):
        if self.status == Status.RUN:
            self.snake.dir = self.dir_temp
            # print('snake.dir',self.snake.dir)
            self.snake.move()
            self.update_score()
            self.update_speed()

    def update_score(self):
        if self.status == Status.RUN:
            # print('score: ', self.point)
            self.score.setText("score: %03d" % self.point)


    def update_timer(self):
        if self.status == Status.RUN:
            # print('time: ', self.time)
            self.time += 1
            self.clock.setText("time: %03d" % self.time)

    def update_status(self, status):
        self.status = status
        # print('main-status: ',self.status)

    def update_speed(self):
        if self.status == Status.RUN:
            if self.snake.speed > 200:
                self.speed_l.setText("speed: 0")
            else:
                self.speed_l.setText("speed: %d" % (200 - self.snake.speed))
            self.speed.setInterval(self.snake.speed)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            self.logo.signals.clicked.emit()
            self.logo.update_pix()
            return
        if self.status == Status.RUN:
            if event.key() == Qt.Key.Key_W and self.snake.dir != 'down':
                self.dir_temp = 'up'
            elif event.key() == Qt.Key.Key_S and self.snake.dir != 'up':
                self.dir_temp = 'down'
            elif event.key() == Qt.Key.Key_A and self.snake.dir != 'right':
                self.dir_temp = 'left'
            elif event.key() == Qt.Key.Key_D and self.snake.dir != 'left':
                self.dir_temp = 'right'
            # print('dir_temp', self.dir_temp)
        if event.key() == Qt.Key_R and self.status == Status.FAILED:
            self.restart()

    def lose(self):
        self.update_status(Status.FAILED)
        self.timer.stop()

    def restart(self):
        self.status = Status.STOP
        self.logo.turn_stop()
        self.snake.init_snake()
        self.dir_temp = self.snake.dir
        self.bood.spawn()
        self.nood.spawn()
        self.kood.spawn()
        self.time = 0
        self.point = 0
        self.clock.setText('time: 000')
        self.score.setText('score: 000')
        self.timer.start()
        # print('restart')

    def excited(self):
        self.snake.speed = 30
        QTimer.singleShot(6000, self.recover)

    def paralysis(self):
        self.snake.speed = 10000
        QTimer.singleShot(3000, self.recover)

    def drowsy(self):
        self.snake.speed = 500
        QTimer.singleShot(12000, self.recover)

    def recover(self):
        self.snake.speed = INTERVAL





app = QApplication(sys.argv)
w = MainWindow()
app.exec()
