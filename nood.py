from PySide6.QtGui import QPainter, QPixmap, Qt
from PySide6.QtWidgets import QWidget, QGraphicsPixmapItem
from config import *
import random


class Nood(QWidget):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.scene = self.game.scene

        self.food_pos = []  # 食物坐标
        self.food_item = None # picture in scene


    # 生成
    def spawn(self):
        self.clear()
        x, y = self.get_random_pos()
        self.food_item = self.draw_block(x * BLOCK_WIDTH, y * BLOCK_WIDTH)  # 已经画出来了


    def clear(self):
        self.scene.removeItem(self.food_item)

    # 不冲突坐标
    def get_random_pos(self):
        while True:
            x = random.randint(AREA_START_X, AREA_END_X)  # [,]
            y = random.randint(AREA_START_Y, AREA_END_Y)
            self.food_pos = [x, y]

            # 食物不能和贪吃蛇和其他食物的任何方块重合
            if self.food_pos not in self.game.snake.pos_list \
               and self.food_pos not in self.game.food_pos_list:
                self.game.food_pos_list[1] = [x, y]
                return x, y

    # 食物方块
    def draw_block(self, x, y):
        pixmap_item = QGraphicsPixmapItem()
        pixmap_item.setPixmap(QPixmap(NOOD))
        pixmap_item.setPos(x+2, y+2)
        self.scene.addItem(pixmap_item)

        return pixmap_item

