import unittest
import random

import sys
sys.path.append("..")

from grid import *
from ant import *

class GridTest(unittest.TestCase):
    def testInit(self):
        nant = Ant('N', (0,0))
        startpts = [(0,5), (2,10)]
        g = Grid(startpts, nant)
        self.assertSetEqual(set(g.points), set([(0,5), (2,10)]))


    def testBlack(self):
        nant = Ant('N', (0,0))
        startpts = [(0,5), (2,10)]
        g = Grid(startpts, nant)
        self.assertTrue(g.squareIsBlack((2,10)))
        self.assertFalse(g.squareIsBlack((1,1)))


    def testForwards(self):
        nant = Ant('N', (0,1))
        startpts = [(0,1)]
        g = Grid(startpts, nant)
        g.stepForward()
        self.assertEquals(nant.getDirection(), 'W')
        self.assertEquals(nant.position, (-1,1))
        self.assertEquals(set(g.points), set([]))

        nant = Ant('N', (0,1))
        startpts = [(2,2)]
        g = Grid(startpts, nant)
        g.stepForward()
        self.assertEquals(nant.getDirection(), 'E')
        self.assertEquals(nant.position, (1,1))
        self.assertSetEqual(set(g.points), set([(0,1),(2,2)]))


    def testRun(self):
        nant = Ant('E', (0,0))
        g = Grid([], nant)
        self.assertEquals(g.score(), 10120)

        nant = Ant('E', (0,0))
        startpts = []
        for i in range(2):
            startpts.append((random.randint(-20,20), random.randint(-20,20)))
            startpts.append((random.randint(-200,200), random.randint(-200,200)))
        startpts = [(-5, 11), (113, -1), (-19, -7), (167, 110)]
        print startpts
        g = Grid(startpts, nant)
        print g.score()
        

if __name__ == '__main__':
    unittest.main()