import random

class GradientGen:

    def __init__(self, start=None, count=5):
        self.start = start if start else self.geninit()
        self.count = count
        self.combinations = {0:[0], 1:[1], 2:[2], 3:[1,0], 4:[0,2], 5:[2,1]}
        self.channels = []
        self.combo = self.getcomb()

    def geninit(self):
        return [random.randint(20,254) for i in range(3)]

    def getcomb(self):
        comb = self.combinations[random.randint(0,5)]
        return {i:random.randint(0,1) for i in comb}

    def hexlify(self):
        out = "#"
        for val in self.start:
            out += hex(val).upper()[2:].rjust(2,"0")
        return out

    def __iter__(self):
        return self

    def __next__(self):
        self.increment()
        return self.hexlify()

    def decrease(self, index, count):
        if self.start[index] - count >= 0:
            self.start[index] -= count
            return True
        self.start[index] = 0
        return False

    def increase(self, index, count):
        if self.start[index] + count <= 255:
            self.start[index] += count
            return True
        self.start[index] = 255
        return False

    def increment(self):
        complete = False
        while not complete:
            for key, value in self.combo.items():
                if value and self.increase(key, self.count):
                    complete = True
                elif not value and self.decrease(key, self.count):
                    complete = True
                else:
                    complete = False
                    self.combo = self.getcomb()
                    break
