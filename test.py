import sys

from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtWidgets import QApplication, QWidget, QPushButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.sound = QSoundEffect()
        url = QUrl.fromLocalFile('i_found_pills.wav')
        self.sound.setSource(url)
        # 1

        self.play_btn = QPushButton('Play Sound', self)
        self.play_btn.clicked.connect(self.sound.play)      # 2


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())