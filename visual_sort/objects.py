import weakref
import random as rand
from turtle import RawTurtle
from visual_sort import conf

def gen_color():
    chars = "123456789ABCDEF"
    return "#" + "".join([rand.choice(chars) for i in range(6)])

class Position:
    def __init__(self, index, start, stop, base):
        self.index = self.num = index
        self.start = start
        self.stop = stop
        self.base = base

    def __str__(self):
        return "{" + f"{self.num}: {self.start}, {self.stop}" + "}"

    def __repr__(self):
        return repr(str(self))


class Block(RawTurtle):
    def __init__(self, screen, base, height, parent=None):
        RawTurtle.__init__(self,screen)
        self.base = base
        self.height = height
        self.value = str(height)
        self.stage = parent
        self.ht()
        self.up()

    def __str__(self):
        return f"block[{self.value}]"

    def __repr__(self):
        return repr(self.value)

    def __eq__(self, other):
        return other.height == self.height

    def __gt__(self, other):
        return self.height > other.height

    def __ge__(self, other):
        return self.height >= other.height

    def __lt__(self, other):
        return self.height < other.height

    def __le__(self, other):
        return self.height <= other.height

    def __le__(self, other):
        return self.height <= other.height

    def __ne__(self, other):
        return self.height != other.height

    def yends(self):
        top = self.base + self.height
        return (top, self.base)

    def xends(self):
        return self.stage.find_positions(self.value)

    def corners(self):
        left, right = self.xends()
        top, bottom = self.yends()
        return [(left,bottom),(right,bottom),(right,top),(left,top)]

    def draw(self):
        self.up()
        corners = self.corners()
        x,y = corners[-1]
        self.goto(x,y)
        self.down()
        self.begin_fill()
        for corner in corners:
            self.goto(*corner)
        self.end_fill()
        self.up()


class Stage:

    def __init__(self, screen):
        self.screen = screen
        self.positions = dict()
        self.blocks = dict()
        self.idx = dict()
        self.keys = dict()
        self.cached = None

    def __str__(self):
        return str([self.idx[k] for k in range(len(self.idx))])

    def __repr__(self):
        return str(self)

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.idx[key]
        return self.keys[key]

    def __setitem__(self, key, block):
        block.clear()
        if item := self.idx[key]:
            item.clear()
            self.keys[item.value] = None
            self.cached = (key, item.value)
        self.idx[key] = block
        self.keys[block.value] = key
        block.draw()
        return

    def __delitem__(self, key):
        block = self.idx[key]
        self.idx[key] = None
        self.keys[block.value] = None
        block.clear()
        self.cached = (key, block.value)

    def __len__(self):
        return len(self.positions)

    def __contains__(self, block):
        if isinstance(block, str):
            return self.keys[block] is not None
        return self.keys[block.value] is not None

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n >= len(self.positions) or self.n < 0:
            raise StopIteration
        block = self.idx[self.n]
        self.n += 1
        return (block)

    def find_positions(self, value):
        idx = self.keys[value]
        pos = self.positions[idx]
        return pos.start, pos.stop

    def update(self):
        self.screen.update()

    def clear(self):
        for block in self.idx.values():
            block.clear()

    def get_block(self, i, screen):
        increment = screen.blockHeight * (i+1)
        block = Block(screen, -screen.base, increment, parent=self)
        block.color(gen_color())
        block.speed(conf.SPEED)
        self.blocks[block.value] = block
        return block

    @classmethod
    def create(cls, screen):
        stage = Stage(screen)
        t = screen.tracer()
        screen.tracer(15)
        start = screen.start
        length = screen.blocks
        for i in range(screen.blocks):
            stop = start + screen.blockWidth
            stage.positions[i] = Position(i, start, stop, -screen.base)
            block = stage.idx[i] = stage.get_block(i, screen)
            stage.keys[block.value] = i
            block.draw()
            start = stop + 2
        screen.tracer(t)
        return stage

