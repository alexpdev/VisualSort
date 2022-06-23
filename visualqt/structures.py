from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
try:
    from visualqt.utils import GradientGen
except ImportError:
    from utils import GradientGen

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


class ListMixin:

    def __len__(self):
        return len(self.seq)

    def __getitem__(self, index):
        return self.seq.__getitem__(index)

    def __setitem__(self, index, other):
        self.seq.__setitem__(index, other)

    def __iter__(self):
        self.iterator = self.seq.__iter__()
        return self

    def __next__(self):
        try:
            return next(self.seq)
        except StopIteration as err:
            raise StopIteration from err

    def append(self, item):
        size = len(self.seq)
        self.deque.append((self.sched.addItem,(size,item)))
        self.seq.append(item)
        self.app.processEvents()

    def __getitem__(self, key):
        return self.seq[key]

    def __add__(self, other):
        return self.seq + other

    def swap(self, idx1, idx2):
        item1 = self.seq[idx1]
        item2 = self.seq[idx2]
        # self.scene.removeItem(item1)
        self.deque.append((self.sched.removeItem,(item1,)))
        self.app.processEvents()
        # self.scene.removeItem(item2)
        self.deque.append((self.sched.removeItem,(item2,)))
        self.app.processEvents()
        # self.scene.additem(idx2, item1)
        self.deque.append((self.sched.addItem,(idx2,item1)))
        self.app.processEvents()
        # self.scene.additem(idx1, item2)
        self.deque.append((self.sched.addItem,(idx1,item2)))
        self.app.processEvents()
        self.seq[idx1] = item2
        self.seq[idx2] = item1

    def insert(self, index, item):
        start = index
        item2 = item
        while start < len(self.scene.pos) - 1:
            temp = self.seq[start]
            # self.scene.signaler.remove.emit(temp)
            self.deque.append((self.sched.removeItem,(temp,)))
            self.app.processEvents()
            self.app.processEvents()
            # self.scene.signaler.add.emit(start, item2)
            self.deque.append((self.sched.addItem,(start,item2)))
            self.app.processEvents()
            item2 = temp
            start += 1
        self.seq.insert(index,item)
        self.app.processEvents()

    def pop(self, index):
        item = self.seq[index]
        # self.scene.removeItem(item)
        self.deque.append((self.sched.removeItem,(item,)))
        start = index
        while start < len(self.seq) - 1:
            item2 = self.seq[start+1]
            self.deque.append((self.sched.removeItem, (item2, )))
            # self.scene.signaler.remove.emit(item2)
            # self.scene.signaler.add.emit(start, item2)
            self.deque.append((self.sched.addItem,(start,item2)))
            start += 1
            self.app.processEvents()
        item = self.seq.pop(index)
        self.app.processEvents()
        return item
