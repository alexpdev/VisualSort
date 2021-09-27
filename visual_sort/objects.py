from turtle import RawTurtle
from visual_sort import utils

class Block(RawTurtle):

    def new(self, index=None):
        screen = self.screen
        index = index if index else self.index
        base = self.base
        height = self.height
        parent = self.stage
        color = self.__color
        self.clear()
        block = Block(screen, index, base, height, parent, color)
        block.draw()
        return block

    def __init__(self, screen, index=0, base=0, height=0, parent=None, color="#000"):
        RawTurtle.__init__(self,screen)
        self.base = base
        self.height = height
        self.__color = color
        self.color(color)
        self.value = str(height)
        self.stage = parent
        self.speed(screen.speed)
        self.index = index
        self.ht()
        self.up()

    def __str__(self):
        return f"block[{self.value}]"

    def __repr__(self):
        return repr(self.value)

    def __eq__(self, other):
        self.screen.update()
        if isinstance(other, type(self)):
            return other.height == self.height
        return False

    def __gt__(self, other):
        self.screen.update()
        return self.height > other.height

    def __ge__(self, other):
        self.screen.update()
        return self.height >= other.height

    def __lt__(self, other):
        self.screen.update()
        return self.height < other.height

    def __le__(self, other):
        self.screen.update()
        return self.height <= other.height

    def __ne__(self, other):
        self.screen.update()
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
            color = next(screen.gradient)
            block = Block(screen, base=base, index=i, height=height, parent=stage, color=color)
            stage.blocks.append(block)
            block.draw()
            start = stop + 1
        stage.get_pen()
        return stage

    def append(self, other):
        if other.index:
            other.clear()
        l = len(self)
        other.index = (l)
        self.blocks.append()

    def slice(self, *args):
        if len(args) > 2: raise Exception
        if len(args) == 2: start, stop = args
        if len(args) == 1: start, stop = 0, args[0]
        if len(args) == 0: start, stop = 0, len(self.blocks)
        stage = Stage(self.screen)
        for idx, i in enumerate(range(start,stop)):
            stage.positions.append(self.positions[i])
            block = self.blocks[i].new()
            block.index = idx
            stage.blocks.append(block)
        return stage

    def __init__(self, screen):
        self.screen = screen
        self.positions = []
        self.blocks = []
        self.operations = 0
        self.pen = None

    def get_pen(self):
        self.pen = RawTurtle(self.screen)
        self.pen.color("#f0d1bf")
        xpos = 0
        ypos = self.screen.height - 30
        self.pen.up()
        self.pen.ht()
        self.pen.goto(xpos, ypos)
        self.pen.down()

    def __getitem__(self, idx):
        # self.operations += 1
        return self.blocks[idx]

    def __setitem__(self, idx, other):
        # self.operations += 1
        if other.index not in [idx, None]:
            other.clear()
            self.blocks[other.index] = None
        if self.blocks[idx] != None:
            self.blocks[idx].clear()
            self.blocks[idx].delindex()
        self.blocks[idx] = other
        self.blocks[idx].setindex(idx)
        other.draw()
        # if self.operations % 100 == 0:
        # self.screen.update()

    def __str__(self):
        return str([i.value for i in self.blocks])

    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(self.blocks)

    def __iter__(self):
        self.iterable = iter(self.blocks)
        return self.iterable

    def __next__(self):
        try:
            block = next(self.iterable)
            return block
        except StopIteration:
            raise StopIteration
