from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtMultimedia import *
from paths import Paths
from config import *


class AudioSource(QSoundEffect):
    def __init__(self):
        super().__init__()
        self.url = None
        self.ds = [BOOD_SOUND, NOOD_SOUND, KOOD_SOUND]

    def define(self, i, name):
        d = self.ds[i]
        self.url = QUrl.fromLocalFile(d[name])
        self.setSource(self.url)
        self.play()
        print(name)
