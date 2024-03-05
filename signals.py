from PySide6.QtCore import Signal, QObject


class Signals(QObject):
    clicked = Signal()
    eat = Signal(int,str)