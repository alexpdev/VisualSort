# -*- coding: utf-8 -*-
# turtleSort.utils.classes
from turtle import RawTurtle, Screen

class NotAssigned(Exception):
    pass

class Section(RawTurtle):

    def __init__(self,screen):
        RawTurtle.__init__(self,screen)
        self.screen = screen
        self.value = None
        self.loc = None
        self.trace = True
        self._color = None
        self.width = None
        self._speed = None

    def __str__(self):
        return f"<section>{str(self.value)},{str(self.loc)}"

    def __repr__(self):
        return f"<section:{str(self.value)}>"

    @classmethod
    def create(cls,screen,**kwargs):
        section = cls(screen)
        section.ht()
        section._color = kwargs["color"]
        section.width = kwargs["width"]
        section.value = kwargs["value"]
        section.trace = kwargs["trace"]
        section._speed = kwargs["speed"]
        section.speed(section._speed)
        section.color(section._color)
        return section

    @property
    def xy(self):
        if self.loc:
            return self.loc.xy
        raise NotAssigned

    @property
    def idx(self):
        if self.loc:
            return self.loc.idx
        raise NotAssigned

    @property
    def poly(self):
        x,y = self.xy
        val,width = self.value,self.width
        cords = [(x+width,y),(x+width,y+val),(x,y+val),(x,y)]
        return cords

    def remove(self,shuffle=False):
        self.clear()
        if not shuffle and not self.trace:
            self.screen.update()
        return

    def draw(self,shuffle=False):
        self.down()
        self.begin_fill()
        for xy in self.poly:
            self.goto(xy)
        self.end_fill()
        if not self.trace and not shuffle:
            self.screen.update()
        return

    def assign(self,loc):
        loc.sect = self
        self.loc = loc
        self.up()
        self.goto(self.xy)
        self.down()

    def carbon_copy(self):
        kwargs = {
            "value" : self.value,
            "color" : self._color,
            "width" : self.width,
            "speed" : self._speed,
            "trace" : self.trace
        }
        sect = Section.create(self.screen,**kwargs)
        return sect


class Location:

    def __init__(self,xy,index):
        self.index = index
        self.x,self.y = xy
        self.xy = xy
        self.sect = None

    def __str__(self):
        return f"<location {str(self.index)},{str(self.xy)}>"

    def __repr__(self):
        return str(self)

    @property
    def value(self):
        if self.sect:
            return self.sect.value
        else:
            raise NotAssigned

    def assign(self,sect):
        self.sect = sect
        sect.loc = self
        self.sect.up()
        self.sect.goto(self.xy)
        self.sect.down()

    def draw(self,shuffle=False):
        if self.sect:
            self.sect.draw(shuffle)
        else:
            raise NotAssigned

    def remove(self,shuffle=False):
        if self.sect:
            self.sect.remove(shuffle)
        else:
            raise NotAssigned

    def carbon_copy(self):
        loc = Location(self.xy,self.index)
        return loc