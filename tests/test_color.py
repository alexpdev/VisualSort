from unittest import TestCase
from turtleSort.prep import gen_gradient

class TestColors(TestCase):

    def setUp(self):
        self.color1 = (0,0,0)
        self.color2 = (255,255,255)

    def test_gradient(self):
        for i in gen_gradient(self.color1,self.color2,100):
            print(i)
            self.assertLess(i[0],256)
            self.assertLess(i[1],256)
            self.assertLess(i[2],256)
