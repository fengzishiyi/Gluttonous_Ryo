from PySide6.QtCore import Signal, QObject


class Signals(QObject):
    complete = Signal()
    clicked = Signal()
    doubleclicked = Signal()
