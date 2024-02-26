from PySide6.QtGui import QColor
from paths import Paths

LOGO_RUN = Paths.icon('logo_run.png')
LOGO_STOP = Paths.icon('logo_stop.png')


# 方块宽度
BLOCK_WIDTH =30

# 水平和垂直方向方块数量
HORIZONTAL_BLOCK_NUM = 40
VERTICAL_BLOCK_NUM = 26

# 屏幕宽高 有 38 * 22 格子
SCENE_WIDTH = BLOCK_WIDTH * HORIZONTAL_BLOCK_NUM  # 30 * 40 1200
SCENE_HEIGHT = BLOCK_WIDTH * VERTICAL_BLOCK_NUM  # 24 * 40 960

# 背景颜色
BG_COLOR = QColor('#6E27A7')

# 蛇蛇颜色#783DAC#F9E7DA
BLOCK_COLOR = QColor('#783DAC')

# 规定贪吃蛇可移动区域的起始和结束坐标,黑边，方块左上角坐标 （1~38，1~22）
AREA_START_X = 1
AREA_START_Y = 3
AREA_END_X = HORIZONTAL_BLOCK_NUM -2
AREA_END_Y = VERTICAL_BLOCK_NUM - 2

# 计时器间隔，用来控制贪吃蛇速度（间隔越小，移动越快）100~200
INTERVAL = 150