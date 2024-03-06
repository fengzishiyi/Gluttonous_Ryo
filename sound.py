from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtMultimedia import *
from paths import Paths
from config import *
import random


class AudioSource(QSoundEffect):
    def __init__(self):
        super().__init__()
        self.url = None
        self.lists = [BOOD_SOUND, NOOD_SOUND, KOOD_SOUND]

    def play_audio(self, i, j):
        list = self.lists[i]
        self.url = QUrl.fromLocalFile(list[j])
        self.setSource(self.url)
        self.play()
