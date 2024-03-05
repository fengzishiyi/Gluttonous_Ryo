from PySide6.QtCore import QUrl
from PySide6.QtGui import QColor
from PySide6.QtMultimedia import QSoundEffect

from paths import Paths
from enum import IntEnum


LOGO_RUN = Paths.icon('logo_run.png')
LOGO_STOP = Paths.icon('logo_stop.png')
BODY = Paths.icon('snake_body.png')
BOOD = Paths.icon('Bood25.png')
NOOD = Paths.icon('Nood25.png')
KOOD = Paths.icon('Kood25.png')

# 方块宽度
BLOCK_WIDTH =30

# 水平和垂直方向方块数量
HORIZONTAL_BLOCK_NUM = 40
VERTICAL_BLOCK_NUM = 26

# 屏幕宽高 有 38 * 22 格子
SCENE_WIDTH = BLOCK_WIDTH * HORIZONTAL_BLOCK_NUM  # 30 * 40 1200
SCENE_HEIGHT = BLOCK_WIDTH * VERTICAL_BLOCK_NUM  # 24 * 40 960

# 背景颜色
BG_COLOR = QColor('#742faa')

# 蛇蛇颜色
BLOCK_COLOR = QColor('#5561A2')
BOOD_COLOR = QColor('#FF9CB6')
NOOD_COLOR = QColor('#E9EA68')
KOOD_COLOR = QColor('#D6304A')


BOOD_SOUND = {
    'i_found_pills': Paths.sound('i_found_pills.wav')
}
NOOD_SOUND = {
    'range_up': Paths.sound('range_up.wav')
}
KOOD_SOUND = {
    'speed_up': Paths.sound('speed_up.wav')
}

# 规定贪吃蛇可移动区域的起始和结束坐标,黑边，方块左上角坐标 （1~38，1~22）
AREA_START_X = 1
AREA_START_Y = 3
AREA_END_X = HORIZONTAL_BLOCK_NUM -2
AREA_END_Y = VERTICAL_BLOCK_NUM - 2

# 计时器间隔，用来控制贪吃蛇速度（间隔越小，移动越快）100~200
INTERVAL = 150

# 运行状态
class Status(IntEnum):
    RUN = 0
    STOP = 1
    FAILED = 2

