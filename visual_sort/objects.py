import weakref
import random as rand
from turtle import Screen, RawTurtle
from visual_sort import conf

def gen_color():
    chars = "123456789ABCDEF"
    return "#" + "".join([rand.choice(chars) for i in range(6)])

class Block(RawTurtle):
    def __init__(self, screen, base, height, stage, position):
        RawTurtle.__init__(self,screen)
        self.base = base
        self.value = str(height)
        self.height = height
        self.stage = stage
        self._space = position
        self.ht()
        self.up()

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

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        txt = f"<Block: {self.value}, {self.index}>"
        return txt

    def index(self):
        if self.space:
            return self.space.index

    @property
    def space(self):
        self.check()
        return self._space

    def check(self):
        position = self.stage()[self.value]
        if not self._space is position:
            self._space = position

    def yends(self):
        top = self.base + self.height
        return (top, self.base)

    def xends(self):
        if self.space:
            left = self._space.start
            right = self._space.stop
            return left,right
        raise Exception

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

class Position:
    def __init__(self, index, start, stop, base):
        self.index = self.num = index
        self.start = start
        self.stop = stop
        self.base = base

class Stage:

    def __init__(self, screen, block_width, block_height):
        self.screen = screen
        self.bwidth = block_width
        self.bheight = block_height
        self.blocks = []
        self.positions = []
        self.mapping = {}
        self.gen_stage(screen)

    def __setitem__(self, key, block):
        if isinstance(key, int):
            self.mapping[block.value] = self.positions[key]
            self.mapping[key] = block
            block.draw()
        else: raise Exception

    def __getitem__(self, idx):
        return self.mapping[idx]

    def __len__(self):
        return self.length

    def __next__(self):
        return next(self.iterator)

    def __contains__(self,value):
        for block in self.blocks:
            if block.value == value:
                return True
        return False

    def __iter__(self):
        for i in range(len(self)):
            yield self.blocks[i]

    def update(self):
        self.screen.update()

    def gen_stage(self,screen):
        width = screen.halfw
        height = screen.halfh
        blkwdth = self.bwidth + 2
        self.length = int(((width * 2) - (blkwdth * 3)) // blkwdth)
        start = -width + self.bwidth
        base = -height
        for i in range(self.length):
            stop = start + self.bwidth
            pos = Position(i, start, stop, base)
            block = self.get_pen(i, base, pos)
            self.positions.append(pos)
            self.blocks.append(block)
            self.mapping[i] = block
            self.mapping[block.value] = pos
            block.draw()
            start = stop + 2

    def get_pen(self, i, base, pos):
        height = self.bheight * (i + 1)
        wkref = weakref.ref(self)
        block = Block(self.screen, base, height, wkref, pos)
        block.color(gen_color())
        block.speed(conf.SPEED)
        return block

    def indexof(self, val):
        return self.mapping[val]

    def clear(self):
        for bar in self.blocks:
            bar.clear()

    def insert(self, idx, block):
        current_pos = self[block.space.index]
        block.clear()
        for i in range(current_pos,idx):
            self[i] = self[i+1]
        self[idx] = block

    def settracer(self, num):
        self.screen.tracer(num)

    def __delitem__(self, num):
        block = self.mapping[num]
        block.clear()
        val = block.value
        self.mapping[num] = None
        self.mapping[val] = None

def get_screen(screen_size, background, tracer, delay):
    screen = Screen()
    screen.setup(*screen_size)
    screen.bgcolor(background)
    screen.tracer(tracer)
    screen.delay(delay)
    winHeight = screen.window_height()*.95
    winWidth = screen.window_width()*.95
    screen.halfh = winHeight // 2
    screen.halfw = winWidth // 2
    return screen


if __name__ == '__main__':
    args = [conf.SCREEN_SIZE, conf.BACKGROUND, conf.TRACER, conf.DELAY]
    screen = get_screen(*args)
    stage = Stage(screen,conf.BLOCK_WIDTH, conf.BLOCK_HEIGHT)
    stage.clear()
