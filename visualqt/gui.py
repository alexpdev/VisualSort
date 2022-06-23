import random
import time
from collections import deque
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
try:
    from visualqt.structures import Rect, Seq
except ImportError:
    from structures import Rect,ListMixin

HEIGHT = 600
WIDTH = 900
RWIDTH = 7
RHEIGHT = 6

class Signaler(QObject):

    wait = Signal([int])
    add = Signal([int, Rect])
    remove = Signal([Rect])

    def __init__(self, scene):
        super().__init__()
        self.scene = scene
        self.wait.connect(self.sleep)
        self.add.connect(self.addItem)
        self.remove.connect(self.removeItem)
        self.deque = deque()
        self.active = False
        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.execute)
        self.timer.start()

    def execute(self):
        if self.active:
            return
        self.active = True
        while len(self.deque) > 0:
            func, args = self.deque.popleft()
            func(*args)
        self.active = False

    def sleep(self, num=0):
        then = time.time()
        while time.time() - then < num:
            pass
        return

    def addItem(self, index, rect):
        self.sleep(.00000001)
        self.scene.additem(index, rect)

    def removeItem(self, item):
        self.sleep(.00000001)
        # args = self.scene.args
        self.scene.removeItem(item)

class Scene(QGraphicsScene):

    def __init__(self, view=None):
        super().__init__()
        self.signaler = Signaler(self)
        self.sched = self.signaler
        self.deque = self.signaler.deque
        self.view = view
        self.app = self.view.app
        self.width = WIDTH
        self.height = HEIGHT
        self.basey = self.view.basey
        self._args = None
        self.pos = []
        self.setSceneRect(0, 0, self.width, self.height)

    @property
    def args(self):
        return self._args

    @args.setter
    def args(self, vals):
        self._args = vals

    def additem(self, index, item):
        x = self.pos[index]
        self.addItem(item)
        item.setPos(x[0],self.basey-item.value)
        self.app.processEvents()

    def emit(self, signal, args=None):
        self.args = args
        signal.emit()

class View(QGraphicsView, ListMixin):

    Pop = Signal([int])
    Insert = Signal([int])
    Append = Signal()
    Swap = Signal([int, int])
    Remove = Signal()
    timerStop = Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.window = parent
        self.app = self.window.app
        self.width, self.height = WIDTH, HEIGHT
        self.rw, self.rh = RWIDTH, RHEIGHT
        self.originx = self.padding = 20
        self.basey = self.height - self.padding
        self.originy = RHEIGHT
        self.fillfunc = None
        self.seq = []
        self.scene = Scene(view=self)
        self.sched = self.scene.sched
        self.deque = self.scene.deque
        self.setScene(self.scene)

    def clear(self):
        while (i := len(self.seq) - 1) >= 0:
            item = self.seq[i]
            # self.scene.removeItem(item)
            self.deque.append((self.sched.removeItem, (item,)))
            del self.scene.pos[i]
            del self.seq[i]
            i -= 1
            self.app.processEvents()
        self.fillfunc = None

    def fill(self):
        if self.fillfunc is None:
            self.fillfunc = self.populate()
        try:
            next(self.fillfunc)
        except StopIteration:
            self.timerStop.emit()

    def populate(self):
        while self.originx < self.width - self.padding:
            item = Rect(self.originy)
            item.setRect(0, 0, RWIDTH, self.originy)
            self.scene.addItem(item)
            # self.deque.append((self.
            # sched.addItem,(item,)))
            self.scene.pos.append((self.originx, self.basey))
            item.setPos(self.originx, self.basey - self.originy)
            self.seq.append(item)
            self.originy += self.rh
            self.originx += self.rw + 2
            yield

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        print(event.scenePosition())

    def shuffle(self):
        choices = list(range(len(self.seq)))
        for _ in range(len(self.seq)):
            chosen = random.choice(choices)
            choices.remove(chosen)
            item = self.pop(chosen)
            self.app.processEvents()
            self.append(item)
            self.app.processEvents()
        choices = list(range(len(self.seq)))
        for i in range(len(self.seq)):
            item = self.pop(i)
            choice = random.choice(choices)
            self.insert(choice, item)
            choices.remove(choice)
