import unittest
from Bowling import Bowling

class TestBowling(unittest.TestCase):
    def test_valid(self):
        b = Bowling()
        b.roll = [[5,2],[8,1],[6,4],[10],[0,5],[2,6],[8,1],[5,3],[6,1],[10,2,6]]
        b.findsum()
    def input_valid(self):
        b = Bowling()
        self.assertTrue(b.input_roll(['5,2', '8,1', '6,4', '10', '0,5', '2,6', '8,1', '5,3', '6,1', '10,2,6']))
        self.assertFalse(b.input_roll(['5,2', '8,1', '6,4', '10', '0,5', '2,6', '8,1', '5,3', '6,1', '10,2,6,4']))
        self.assertFalse(b.input_roll('5,2'))

if __name__ == '__main__':
    t = TestBowling()
    t.test_valid()
    t.input_valid()

