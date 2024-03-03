from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtGui import QColor, QPen

from config import *

class Scene(QGraphicsScene):

    def __init__(self):
        super().__init__()

        self.setSceneRect(0, 0, SCENE_WIDTH, SCENE_HEIGHT)
        self.draw_scene()

    def draw_scene(self):
        self._draw_bg()

    def _draw_bg(self):
        self.setBackgroundBrush(BG_COLOR)








