from unittest import TestCase
from turtleSort import prep
from turtleSort.config import OPTIONS

class TestPrep(TestCase):

    def setUp(self):
        self.kwargs = OPTIONS

    def test_options(self):
        lst = ["tracer","delay","size","bgcolor"]
        for k in lst:
            self.assertTrue(k in self.kwargs)
        return
