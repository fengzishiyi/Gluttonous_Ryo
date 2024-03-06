import random
from PySide6.QtCore import QObject, Qt
from PySide6.QtGui import QPixmap, QPen
from PySide6.QtWidgets import *
from config import *
from signals import Signals


class Snake(QObject):
    def __init__(self, game):
        super().__init__()
        self.dir = None
        self.game = game
        self.scene = self.game.scene
        self.pos_list = []
        self.color_list = [BLOCK_COLOR, BLOCK_COLOR, BLOCK_COLOR]
        self.snake_items_list = []
        self.signals = Signals()
        self.speed = INTERVAL
        
    def init_snake(self):
        self.pos_list = []
        self.speed = INTERVAL
        self.color_list = [BLOCK_COLOR, BLOCK_COLOR, BLOCK_COLOR]

        x, y = self.get_random_pos()
        self.pos_list.append([x,y])

        while True:
            num = random.randint(1,4)
            if num == 1 and x-2 >= AREA_START_X:
                self.pos_list.append([x-1, y])
                self.pos_list.append([x-2, y])
                self.dir = 'right'
                break
            elif num == 2 and x+2 <= AREA_END_X:    # 蛇身朝右，向左移动
                self.pos_list.append([x+1, y])
                self.pos_list.append([x+2, y])
                self.dir = 'left'
                break
            elif num == 3 and y-2 >= AREA_START_Y:  # 蛇身朝上，向下移动
                self.pos_list.append([x, y-1])
                self.pos_list.append([x, y-2])
                self.dir = 'down'
                break
            elif num == 4 and y+2 <= AREA_END_Y:    # 蛇身朝下，向上移动
                self.pos_list.append([x, y+1])
                self.pos_list.append([x, y+2])
                self.dir = 'up'
                break

        self.draw_snake(self.pos_list)

    def get_random_pos(self):
        x = random.randint(AREA_START_X + 3, AREA_END_X - 3)
        y = random.randint(AREA_START_Y + 3, AREA_END_Y - 3)
        return x, y

    def draw_snake(self, pos_list):
        self.clear()

        for i, pos in enumerate(pos_list):
            x = pos[0]
            y = pos[1]
            block = self.draw_block(x * BLOCK_WIDTH, y * BLOCK_WIDTH, i)
            self.snake_items_list.append(block)

    def clear(self):
        for item in self.snake_items_list:
            self.scene.removeItem(item)

        self.snake_items_list = []

    def draw_block(self, x, y, i):
        rect_item2 = QGraphicsRectItem()
        rect_item2.setRect(x + 2, y + 2, BLOCK_WIDTH - 4, BLOCK_WIDTH - 4)
        rect_item2.setBrush(self.color_list[i])
        # rect_item2.setPen(Qt.PenStyle.NoPen)
        rect_item2.setOpacity(0.8)
        self.scene.addItem(rect_item2)
        return rect_item2

    def move(self):
        head_pos = list(self.pos_list[0])
        if self.dir == 'left':
            head_pos[0] -= 1
        elif self.dir == 'right':
            head_pos[0] += 1
        elif self.dir == 'up':
            head_pos[1] -= 1
        elif self.dir == 'down':
            head_pos[1] += 1

        self.check_collision(head_pos)

        if self.game.status == Status.RUN:
            self.pos_list.insert(0,head_pos)

            if head_pos not in self.game.food_pos_list:
                self.pos_list.pop()
            else:
                self.game.point += 1
                if head_pos == self.game.food_pos_list[0]:
                    self.game.bood.spawn()
                    self.color_list.append(BOOD_COLOR)
                    self.signals.eat.emit(0, random.randint(0,LEN_BOOD-1))
                elif head_pos == self.game.food_pos_list[1]:
                    self.game.nood.spawn()
                    self.color_list.append(NOOD_COLOR)
                    self.signals.eat.emit(1, random.randint(0,LEN_NOOD-1))
                elif head_pos == self.game.food_pos_list[2]:
                    self.game.kood.spawn()
                    self.color_list.append(KOOD_COLOR)
                    self.signals.eat.emit(2, random.randint(0,LEN_KOOD-1))

            self.draw_snake(self.pos_list)


    def check_collision(self, head_pos):
        for i, pos in enumerate(self.pos_list):
            if i != 0 and head_pos == pos:
                self.game.lose()
                return

        if head_pos[0] < AREA_START_X or head_pos[0] > AREA_END_X or \
                head_pos[1] < AREA_START_Y or head_pos[1] > AREA_END_Y:
            self.game.lose()

    def do_pills(self, i, j):
        if i == 0:
            if j == 0:
                self.color_list = [BOOD_COLOR] * len(self.color_list)
            if j == 1:
                colors = [BOOD_COLOR,NOOD_COLOR,KOOD_COLOR,BLOCK_COLOR]
                n = len(self.color_list)
                self.color_list = []
                for i in range(n):
                    self.color_list.append(colors[random.randint(0,3)])
        elif i == 1:
            if j == 0:
                self.color_list = [NOOD_COLOR] * len(self.color_list)

        else:
            if j == 0:
                self.speed = max(100,(self.speed - 30))
            elif j == 1:
                self.speed = min(190,(self.speed + 30))
            elif j == 2:
                self.color_list = [KOOD_COLOR] * len(self.color_list)