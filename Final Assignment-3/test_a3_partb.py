#
#   Author: Catherine Leung
#   These are the unit tests for functions and classes of assingment 3 part b
#   To use this, run: python test_a3_partc.py


import unittest
from a3_partb import GameTree

class A2CTestCase(unittest.TestCase):
    """These are the test cases for functions and classes of a2"""
        
    def test_gametree(self):
        
        boards = [[
                    # a board that is one move away from winning for p1
                    [ 0 , 2,  -2, 0, 0,  0],
                    [ 0,  0 , -3,  -1,  0,  0],
                    [ 0,  0,  0,  0,  0, 0],
                    [ 0,  0,  0,  0,  2, 0],
                    [ 0,  0,  0,  2,  0, 0]
                     ],
                    # a board that is one move away from winning for p2
                    [
                    [ 0 , -2, 2, 0, 0,  0],
                    [ 0,  0,  3,  1,  0,  0],
                    [ 0,  0,  -1,  0,  0, 0],
                    [ 0,  0,  0,  0, -2, 0],
                    [ 0,  0,  0,  -2,  0, 0]
                    ],
                    # a board where p1 places piece in any corner will guarantee a win for p2 (p1 must avoid corners)
                    [
                    [ 0 , 0,  0,  0,  0,  0],
                    [ -1, 0,  0,  0,  0,  -1],
                    [ -2, 3,  3,  3,  3, -2],
                    [ -1, 0,  0,  0,  0, -1],
                    [ 0,  0,  -2,  -1,  0,  0]
                    ],
                    # a board where p2 places piece in any corner will guarantee a win for p1 (p2 must avoid corners)
                    [
                    [ 0 , 0,  0,  0,  0,  0],
                    [ 1, 0,  0,  0,  0,  1],
                    [ 2, -3,  -3,  -3,  -3, 2],
                    [ 1, 0,  0,  0,  0, 1],
                    [ 0,  0,  2,  1,  0,  0]
                    ]

        ]

    # ensure bots will always take an obvious winning move
        tree = GameTree(boards[0], 1)
        (row,col) = tree.get_move()
        self.assertEqual((row,col),(0,1))

        tree = GameTree(boards[1], -1)
        (row,col) = tree.get_move()
        self.assertEqual((row,col),(0,1))

    # ensure bots will always avoid obvious losing moves
        tree = GameTree(boards[2], 1)
        (row,col) = tree.get_move()
        self.assertNotEqual((row,col), (0,0))
        self.assertNotEqual((row,col), (0,5))
        self.assertNotEqual((row,col), (4,0))
        self.assertNotEqual((row,col), (4,5))

        tree = GameTree(boards[3], -1)
        (row,col) = tree.get_move()
        self.assertNotEqual((row,col), (0,0))
        self.assertNotEqual((row,col), (0,5))
        self.assertNotEqual((row,col), (4,0))
        self.assertNotEqual((row,col), (4,5))


if __name__ == '__main__':
    unittest.main()
