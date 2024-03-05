import os

class Paths:
    base = os.path.dirname(__file__) # 返回父目录
    icons = os.path.join(base,'icons')
    sounds = os.path.join(base,'sounds')

    @classmethod
    def icon(cls,filename):
        return os.path.join(cls.icons,filename) # 类属性 cls.a

    @classmethod
    def sound(cls,filename):
        return os.path.join(cls.sounds,filename) # 类属性 cls.a