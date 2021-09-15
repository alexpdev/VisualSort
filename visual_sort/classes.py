from turtle import RawTurtle
from visual_sort import utils

class Block(RawTurtle):

    def __init__(self, screen, stage, height, base, color):
        RawTurtle.__init__(self,screen)
        self._color_ = color
        self.color(color)
        self.speed(10)
        self.height = height
        self.value = str(height)
        self.stage = stage
        self.base = base
        self.ypos = (self.base, self.base + self.height)
        self.ht()
        self.up()

    def __gt__(self, other):
        return self.height > other.height

    def __lt__(self, other):
        return self.height < other.height

    def __le__(self, other):
        return self.height <= other.height

    def __ge__(self, other):
        return self.height >= other.height

    def __eq__(self, other):
        return self.height == other.height

    def __ne__(self, other):
        return self.height != other.height

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self.height)

    @property
    def index(self):
        return self.stage.index(self)

    def position(self):
        return self.stage.pos(self.index)

    def corners(self, pos=None):
        y1, y2 = self.ypos
        if pos:
            x1, x2 = pos
        else:
            x1, x2 = self.position()
        return [(x1,y1),(x2,y1),(x2,y2),(x1,y2)]


    def draw(self, pos=None):
        corners = self.corners(pos=pos)
        start = corners[-1]
        self.goto(*start)
        self.down()
        self.begin_fill()
        for corner in corners:
            self.goto(*corner)
        self.end_fill()
        self.up()

    @classmethod
    def new(cls, block):
        screen = block.screen
        stage = block.stage
        height = block.height
        base = block.base
        color = block._color_
        block2 = cls(screen, stage, height, base, color)
        block.clear()
        del block
        return block2

class Stage(list):

    def __init__(self, arg=[]):
        super().__init__(arg)
        self.screen = None
        self.positions = []

    @classmethod
    def create(cls, screen):
        stage = cls()
        stage.positions = []
        stage.screen = screen
        start = screen.start
        for i in range(screen.blocks):
            stop = start + screen.blockwidth
            position = (start,stop)
            stage.positions.append(position)
            start = stop + 2
            height = screen.increment * (i+1)
            color = utils.gen_color()
            block = Block(screen, stage, height, -screen.base, color)
            block.draw(pos=position)
            stage.append(block)
        return stage

    def __setitem__(self, idx, other):
        self[idx].clear()
        other.clear()
        other = Block.new(other)
        super().__setitem__(idx, other)
        self[idx].draw(pos=self.positions[idx])

    def __delitem__(self, idx):
        self[idx].clear()

    def pos(self,idx):
        return self.positions[idx]

    def __contains__(self,other):
        return other.value in [i.value for i in self]

    def index(self, item):
        for i in range(len(self)):
            if self[i].value == item.value:
                return i
        return None

    def extend(self, other):
        for i in range(len(other)):
            self.positions.append(other.positions[i])
            self.append(other[i])
