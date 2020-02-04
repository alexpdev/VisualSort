from unittest import TestCase
# from turtleSort.utils.prep import gen_gradient
from prep import gen_gradient

class TestColors(TestCase):

    def setUp(self):
        color1 = (0,0,0)
        color2 = (255,255,255)

    def test_gradient(self):
        for i in gen_gradient(self.color1,self.color2):
            print(i)
            self.assertLess(255,i[0])
            self.assertLess(255,i[1])
            self.assertLess(255,i[2])

color1 = (0,0,0)
color2 = (255,255,255)

test_gradient(color1,color2)
