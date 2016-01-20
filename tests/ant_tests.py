import unittest

import sys
sys.path.append("..")

from ant import *

class AntTest(unittest.TestCase):
    def testDirection(self):
        nant = Ant('N', (0,0))
        self.assertEquals(nant.getDirection(), 'N')


    def testLambda(self):
        def turntest(start, d, end):
            nant = Ant(start, (0,0))
            nant.turn(d)
            self.assertEquals(nant.getDirection(), end)
            
        turns = [['N','E'], ['E','S'], ['S','W'], ['W','N']]
        for s,e in turns:
            turntest(s,'R',e)
            turntest(e,'L',s)
            

    def testForwards(self):
        nant = Ant('N', (0,0))
        nant.goForwards()
        self.assertTupleEqual(nant.position, (0,1))

        nant = Ant('W', (-17,12))
        nant.goForwards()
        self.assertTupleEqual(nant.position, (-18,12))
        

if __name__ == '__main__':
    unittest.main()