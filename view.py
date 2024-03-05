from PySide6.QtWidgets import QGraphicsScene, QGraphicsView
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPen, QPainter

from config import *

from logo import Logo


class View(QGraphicsView):
    
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 设置渲染属性
        self.setRenderHints(QPainter.Antialiasing |  # 抗锯齿
                            QPainter.TextAntialiasing |  # 文字抗锯齿
                            QPainter.SmoothPixmapTransform |  # 使图元变换更加平滑
                            QPainter.LosslessImageRendering)
        # 视窗更新模式
        self.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.FullViewportUpdate)
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setDragMode(QGraphicsView.DragMode.RubberBandDrag)




    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_Enter():
    #         pass
    #
    # def mousePressEvent(self, event):
    #     super().mousePressEvent(event)
    #     if event.button() == Qt.LeftButton:
    #         item = self.get_item_at_click(event)
    #         if isinstance(item, LogoItem):
    #             pass
    #
    # def get_item_at_click(self,event):
    #     pos = event.pos()
    #     item = self.itemAt(pos)
    #     return item

