import random
import sys
import time
try:
    from visualqt.utils import GradientGen
    from visualqt.algorithms import bubblesort
except ImportError:
    from utils import GradientGen
    from algorithms import bubblesort
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

gradient1 = GradientGen()
gradient2 = GradientGen()

class Rect(QGraphicsRectItem):

    def __init__(self, value):
        super().__init__()
        self.value = value
        self.setBrush(QBrush(next(gradient1)))
        self.setPen(QPen(next(gradient2)))
        flag = self.GraphicsItemFlag
        self.setFlags(
            flag.ItemIsSelectable | flag.ItemIsFocusable | flag.ItemIsMovable
        )
        self.value

    def __str__(self):
        return f"Rect({self.value})"

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        if isinstance(other, Rect):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            raise TypeError

    def __lt__(self, other):
        if isinstance(other, Rect):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            raise TypeError

    def __gt__(self, other):
        if isinstance(other, Rect):
            return self.value > other.value
        elif isinstance(other, int):
            return self.value > other
        else:
            raise TypeError

    def __ge__(self, other):
        if isinstance(other, Rect):
            return self.value >= other.value
        elif isinstance(other, int):
            return self.value >= other
        else:
            raise TypeError

    def __le__(self, other):
        if isinstance(other, Rect):
            return self.value <= other.value
        elif isinstance(other, int):
            return self.value <= other
        else:
            raise TypeError

    def __eq__(self, other):
        if isinstance(other, Rect):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            raise TypeError

    def __ne__(self, other):
        if isinstance(other, Rect):
            return self.value != other.value
        elif isinstance(other, int):
            return self.value != other
        else:
            raise TypeError


class Signaler(QObject):

    wait = Signal([int])
    add = Signal()
    remove = Signal()


    def __init__(self, scene):
        super().__init__()
        self.scene = scene
        self.wait.connect(self.sleep)
        self.add.connect(self.addItem)
        self.remove.connect(self.removeItem)

    def sleep(self, num=0):
        then = time.time()
        while time.time() - then < num:
            pass
        return

    def addItem(self):
        args = self.scene.args
        self.scene.additem(*args)

    def removeItem(self):
        args = self.scene.args
        self.scene.removeItem(*args)

class Scene(QGraphicsScene):

    def __init__(self):
        super().__init__()
        self.signaler = Signaler(self)
        self.width = 800
        self.height = 400
        self._args = None
        self.widget = None
        self.app = None
        self.setSceneRect(0, 0, self.width, self.height)

    @property
    def args(self):
        return self._args

    @args.setter
    def args(self, vals):
        self._args = vals

    def additem(self, pos, item):
        x,y = pos
        self.addItem(item)
        item.setPos(x,y-item.value)
        self.app.processEvents()

    def emit(self, signal, args=None):
        self.args = args
        signal.emit()

    def setWidget(self, widget):
        self.widget = widget
        self.app = self.widget.app


class View(QGraphicsView):

    Pop = Signal([int])
    Insert = Signal([int])
    Append = Signal()
    Swap = Signal([int, int])
    timerStop = Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.wind = parent
        self.app = self.wind.app
        self.originx = self.padding = 20
        self.originy = 380
        self.width = 8
        self.height = 0
        self.scene_ = None
        self.extendy = 0
        self.extendx = self.width + 2
        self.rects = []
        self.positions = []
        self.popfunc = None
        self.extra = []
        self.Append.connect(self.append)
        self.Swap.connect(self.swap)
        self.Insert.connect(self.insert)
        self.Pop.connect(self.pop)

    def pop(self, index):
        item = self.rects[index]
        self.scene_.removeItem(item)
        start = index
        while start < len(self.positions) - 1:
            item2 = self.rects[start+1]
            self.scene_.args = [item2]
            self.scene_.signaler.remove.emit()
            self.scene_.args = [self.positions[start], item2]
            self.scene_.signaler.add.emit()
            start += 1
        item = self.rects.pop(index)
        self.extra.append(item)
        self.app.processEvents()
        return item

    def insert(self, index, item=None):
        if item is None:
            item = self.extra.pop()
        start = index
        item2 = item
        while start < len(self.positions) - 1:
            temp = self.rects[start]
            self.scene_.args = [temp]
            self.scene_.signaler.remove.emit()
            self.scene_.args = [self.positions[start], item2]
            self.scene_.signaler.add.emit()
            item2 = temp
            start += 1
        self.rects.insert(index,item)
        self.app.processEvents()

    def append(self, item=None):
        if item is None:
            item = self.extra.pop()
        size = len(self.rects)
        self.scene_.args = (self.positions[size],item)
        self.scene_.signaler.add.emit()
        self.rects.append(item)
        self.app.processEvents()

    def setScene(self, scene):
        super().setScene(scene)
        self.scene_ = scene
        self.scene_.setWidget(self)
        self.scene_.paren = self
        padding = self.originx * 2
        dist = self.originy - (self.originx // 2)
        xtotal = (self.scene_.width - padding) // self.width
        ytotal = dist // xtotal
        self.height += ytotal
        self.extendy += self.height

    def fill(self):
        if self.popfunc is None:
            self.popfunc = self.populate()
        try:
            next(self.popfunc)
        except StopIteration:
            self.timerStop.emit()

    def populate(self):
        while self.originx < self.scene_.width - self.padding:
            item = Rect(self.height)
            item.setRect(0,0,self.width, self.height)
            self.scene_.addItem(item)
            item.setPos(self.originx, self.originy - self.height)
            self.rects.append(item)
            self.positions.append((self.originx, self.originy))
            self.height += self.extendy
            self.originx += self.extendx
            yield

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        print(event.scenePosition())

    def shuffle(self):
        choices = list(range(len(self.rects)))
        for _ in range(len(self.rects)):
            chosen = random.choice(choices)
            choices.remove(chosen)
            item = self.pop(chosen)
            self.append(item)
            self.app.processEvents()

    def swap(self, idx1, idx2):
        item1 = self.rects[idx1]
        item2 = self.rects[idx2]
        self.scene_.removeItem(item1)
        self.scene_.removeItem(item2)
        self.scene_.additem(self.positions[idx2], item1)
        self.scene_.additem(self.positions[idx1], item2)
        self.rects[idx1] = item2
        self.rects[idx2] = item1
        self.app.processEvents()


class Window(QMainWindow):

    def __init__(self, app) -> None:
        super().__init__()
        self.app = app
        self.layout = QVBoxLayout()
        self.hlayout  = QHBoxLayout()

        self.button1 = QPushButton("shuffle", parent=self)
        self.button2 = QPushButton("bubblesort", parent=self)
        self.button3 = QPushButton("unknown", parent=self)
        self.button4 = QPushButton("populate", parent=self)

        self.xlayout = QHBoxLayout()
        self.ylayout = QHBoxLayout()
        self.group1 = QGroupBox()
        self.group2 = QGroupBox()
        self.group1.setLayout(self.xlayout)
        self.group2.setLayout(self.ylayout)

        self.xlayout.addWidget(self.button1)
        self.xlayout.addWidget(self.button2)
        self.ylayout.addWidget(self.button3)
        self.ylayout.addWidget(self.button4)

        self.hlayout.addWidget(self.group1)
        self.hlayout.addWidget(self.group2)

        self.layout.addLayout(self.hlayout)
        self.graphics = View(parent=self)
        self.layout.addWidget(self.graphics)
        self.scene = Scene()
        self.graphics.setScene(self.scene)
        self.central = QWidget()
        self.central.setLayout(self.layout)
        self.setCentralWidget(self.central)
        self.button1.clicked.connect(self.shuffle)
        self.button2.clicked.connect(self.bubblesort)
        self.button3.clicked.connect(self.plusy)
        self.button4.clicked.connect(self.populate)
        self.graphics.timerStop.connect(self.stopTimer)
        self.px, self.py, self.w, self.h = 10, 300-10, 8, 10

    def stopTimer(self):
        self.timer.stop()

    def shuffle(self):
        self.graphics.shuffle()

    def plusy(self):
        self.graphics.originy += 1
        rect = Rect()
        self.graphics.addItem(rect)

    def bubblesort(self):
        view = self.graphics
        rects = self.graphics.rects
        bubblesort(view, rects)

    def populate(self):
        self.timer = QTimer()
        self.timer.setInterval(70)
        self.timer.timeout.connect(self.graphics.fill)
        self.timer.start()
