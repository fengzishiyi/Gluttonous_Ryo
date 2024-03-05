from PySide6.QtWidgets import QGraphicsScene, QGraphicsRectItem
from PySide6.QtGui import QColor, QPen

from config import *

class Scene(QGraphicsScene):

    def __init__(self):
        super().__init__()

        self.setSceneRect(0, 0, SCENE_WIDTH, SCENE_HEIGHT)
        self.draw_scene()

    def draw_scene(self):
        self._draw_bg()
        self.draw_move_area()
        self.draw_move_area_frame()

    def _draw_bg(self):
        self.setBackgroundBrush(BG_COLOR)

    def draw_move_area(self):
        """绘制贪吃蛇可移动的区域"""
        for x in range(HORIZONTAL_BLOCK_NUM):
            for y in range(VERTICAL_BLOCK_NUM):
                if AREA_START_X <= x <= AREA_END_X and AREA_START_Y <= y <= AREA_END_Y:
                    self.draw_block(x * BLOCK_WIDTH, y * BLOCK_WIDTH)

    def draw_block(self, x, y):
        rect_item1 = QGraphicsRectItem()
        rect_item2 = QGraphicsRectItem()
        rect_item1.setRect(x, y, BLOCK_WIDTH, BLOCK_WIDTH)
        rect_item2.setRect(x + 2, y + 2, BLOCK_WIDTH - 4, BLOCK_WIDTH - 4)

        rect_item1.setBrush(BG_COLOR)
        rect_item2.setBrush(BG_COLOR)
        rect_item1.setOpacity(0.04)
        rect_item2.setOpacity(0.04)
        self.addItem(rect_item1)
        self.addItem(rect_item2)

        return (rect_item1, rect_item2)

    def draw_move_area_frame(self):
        """绘制区域边框"""
        rect_item = QGraphicsRectItem()

        offset = 3
        x = AREA_START_X * BLOCK_WIDTH - offset #pos
        y = AREA_START_Y * BLOCK_WIDTH - offset #pos
        width = AREA_END_X * BLOCK_WIDTH + offset * 2
        height = (AREA_END_Y - AREA_START_Y + 1) * BLOCK_WIDTH + offset * 2
        rect_item.setRect(x, y, width, height)
        rect_item.setOpacity(0.3)
        self.addItem(rect_item)








