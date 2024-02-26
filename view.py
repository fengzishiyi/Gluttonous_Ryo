from PySide6.QtWidgets import QGraphicsScene, QGraphicsView
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPen, QPainter

from config import *

from logo import LogoItem


class View(QGraphicsView):
    
    def __init__(self, v_scene, parent=None):
        super().__init__(parent)
        
        self.v_scene = v_scene

        self.init_ui()

    def init_ui(self):
        # 设置渲染属性
        self.setRenderHints(QPainter.Antialiasing |  # 抗锯齿
                            QPainter.TextAntialiasing |  # 文字抗锯齿
                            QPainter.SmoothPixmapTransform |  # 使图元变换更加平滑
                            QPainter.LosslessImageRendering)
        # 视窗更新模式
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setDragMode(QGraphicsView.RubberBandDrag)

        self.setScene(self.v_scene)

        logo = LogoItem()
        logo.setPos(SCENE_WIDTH/2 - logo.boundingRect().width()/2, BLOCK_WIDTH/2)
        self.v_scene.addItem(logo)

