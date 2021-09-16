import random as rand
from turtle import RawTurtle
from visual_sort import utils

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
    def __init__(self, screen, index=None, base=None, height=None, parent=None):
        RawTurtle.__init__(self,screen)
        self.base = base
        self.height = height
        self.value = str(height)
        self.stage = parent
        self.index = index
        self.ht()
        self.up()

    def __str__(self):
        return f"block[{self.value}]"

    def __repr__(self):
        return repr(self.value)

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return other.height == self.height
        return False

    def __gt__(self, other):
        return self.height > other.height

    def __ge__(self, other):
        return self.height >= other.height

    def __lt__(self, other):
        return self.height < other.height

    def __le__(self, other):
        return self.height <= other.height

    def __ne__(self, other):
        if isinstance(other, type(self)):
            return self.height != other.height
        return True

    def setindex(self, idx):
        self.index = idx

    def delindex(self):
        self.index = None

    def yends(self):
        top = self.base + self.height
        return (top, self.base)

    def xends(self):
        return self.stage.positions[self.index]

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

    @classmethod
    def create(cls, screen):
        stage = cls(screen)
        start = screen.start
        blocks = screen.blocks
        for i in range(blocks):
            stop = start + screen.blockwidth
            stage.positions.append((start,stop))
            base = -screen.base
            height = screen.increment * (i+1)
            color = utils.gen_color()
            block = Block(screen, base=base, index=i, height=height, parent=stage)
            block.color(color)
            stage.blocks.append(block)
            block.draw()
            start = stop + 2
        return stage

    def __init__(self, screen):
        self.screen = screen
        self.positions = []
        self.blocks = []

    def __getitem__(self, idx):
        return self.blocks[idx]

    def __setitem__(self, idx, other):
        if other.index not in [idx, None]:
            other.clear()
            self.blocks[other.index] = None
        if self.blocks[idx] != None:
            self.blocks[idx].clear()
            self.blocks[idx].delindex()
        self.blocks[idx] = other
        self.blocks[idx].setindex(idx)
        other.draw()

    def __str__(self):
        return str([i.value for i in self.blocks])

    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(self.blocks)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n >= len(self.blocks) or self.n < 0:
            raise StopIteration
        block = self.idx[self.n]
        self.n += 1
        return (block)

