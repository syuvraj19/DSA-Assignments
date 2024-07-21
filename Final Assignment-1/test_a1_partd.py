#
#   Author: Catherine Leung
#   These are the unit tests for functions and classes of assingment1
#   To use this, run: python test_a1_partd.py

import unittest
from collections import Counter
from a1_partd import get_overflow_list, overflow
from a1_partc import Queue

class A1DTestCase(unittest.TestCase):
    """These are the test cases for functions and classes of a1"""
    
    def test_get_overflow_list(self):

        def gen_id(row,col):
            return row * 100 + col

        grid =[[0, 0, 0, 0, 0, 0 ,0],
               [0, 0, 0, 0, 0, 0 ,0],
               [0, 0, 0, 0, 0, 0 ,0],
               [0, 0, 0, 0, 0, 0 ,0],
               [0, 0, 0, 0, 0, 0 ,0], 
               [0, 0, 0, 0, 0, 0 ,0]
               ]
        result = get_overflow_list(grid)
        self.assertEqual(result, None)


        grid =[[1, 2, 2, 2, 2, 2 , 2, 1],
               [2, 3, 3, 3, 3, 3 , 3, 2],
               [2, 3, 3, 3, 3, 3 , 3, 2],
               [2, 3, 3, 3, 3, 3 , 3, 2],
               [2, 3, 3, 3, 3, 3 , 3, 2],
               [2, 3, 3, 3, 3, 3 , 3, 2],
               [1, 2, 2, 2, 2, 2 , 2, 1]
               ]

        result = get_overflow_list(grid)
        self.assertEqual(result, None)



        grid =[[-1, -2, -2, -2, -2, -2 , -2, -1],
               [-2, -3, -3, -3, -3, -3 , -3, -2],
               [-2, -3, -3, -3, -3, -3 , -3, -2],
               [-2, -3, -3, -3, -3, -3 , -3, -2],
               [-2, -3, -3, -3, -3, -3 , -3, -2],
               [-2, -3, -3, -3, -3, -3 , -3, -2],
               [-1, -2, -2, -2, -2, -2 , -2, -1]
               ]

        result = get_overflow_list(grid)
        self.assertEqual(result, None)


        grid =[[2,  0,  0, 0, 0],
                [0, -3,  0, 0, 0],
                [0,  0, -2, 0, 0],
                [-1, 0,  0, 0, 3]
                ]
        correct = [(0,0),(3,4)]
        overflow_hash = Counter()
        for coord in correct:
            overflow_hash[gen_id(coord[0],coord[1])] += 1

        result = get_overflow_list(grid)

        self.assertEqual(len(correct), len(result))

        for coord in result:
            self.assertEqual(overflow_hash[gen_id(coord[0],coord[1])], 1)
            overflow_hash[gen_id(coord[0],coord[1])] += 1

        grid =[[-2,  0,  0, 0, 0],
                [0, 3,  0, 0, 0],
                [0,  0, 2, 0, 0],
                [1, 0,  0, 0, -3]
                ]

        correct = [(0,0),(3,4)]
        overflow_hash = Counter()
        for coord in correct:
            overflow_hash[gen_id(coord[0],coord[1])] += 1

        result = get_overflow_list(grid)

        self.assertEqual(len(correct), len(result))

        for coord in result:
            self.assertEqual(overflow_hash[gen_id(coord[0],coord[1])], 1)
            overflow_hash[gen_id(coord[0],coord[1])] += 1



        grid =[
                [2, 3, 3, 3, 3, 2],
                [3, 4, 4, 4, 4, 3],
                [3, 4, 4, 4, 4, 3],
                [3, 4, 4, 4, 4, 3],
                [2, 3, 3, 3, 3, 2]

            ]

                                                        
        correct = [(0,0), (0,1), (0,2), (0,3),(0,4),(0,5),
                   (1,0), (1,1), (1,2), (1,3),(1,4),(1,5),
                   (2,0), (2,1), (2,2), (2,3),(2,4),(2,5),
                   (3,0), (3,1), (3,2), (3,3),(3,4),(3,5),
                   (4,0), (4,1), (4,2), (4,3),(4,4),(4,5)
                 ]
        overflow_hash = Counter()
        for coord in correct:
            overflow_hash[gen_id(coord[0],coord[1])] += 1

        result = get_overflow_list(grid)
        self.assertEqual(len(correct), len(result))

        for coord in result:
            self.assertEqual(overflow_hash[gen_id(coord[0],coord[1])], 1)
            overflow_hash[gen_id(coord[0],coord[1])] += 1



    def test_overflow(self):


        grid =[ 
                [-2,  2, -3,  0,  0],
                [ 0, -4,  0,  0,  0],
                [ 0,  0,  3,  0,  1],
                [-1,  0,  0,  0,  1]
              ]


        grid_2 =[
                    [-1,  3,   3,  0,  0],
                    [ 0, -3,   0,  0,  0],
                    [ 0,  0,  -3,  0,  2],
                    [-1,  0,  -2, -2,  2]
                ]


        steps = [
                    [
                     [  0,  -5,  0,  -1,  0 ],
                     [ -2,   0, -2,   0,  0 ],
                     [  0,  -1,  3,   0,  1 ],
                     [ -1,   0,  0,   0,  1 ]
                    ],
                    [
                     [ -1,   0,  -1,  -1,  0 ],
                     [ -2,  -1, -2,   0,  0 ],
                     [  0,  -1,  3,   0,  1 ],
                     [ -1,   0,  0,   0,  1 ]
                    ],
                    [
                     [  2,   1,  1,  1,  0 ],
                     [  0,   4,  1,  0,  0 ],
                     [  0,   0, -3,  0,  3 ],
                     [ -1,   0, -2,  3,  0 ]
                    ],
                    [
                     [  0,   3,  1,  1,  0 ],
                     [  2,   0,  2,  0,  1 ],
                     [  0,   1, -3,  2,  0 ],
                     [ -1,   0,  3,  0,  2 ]
                    ],
                    [
                     [  1,   0,  2,  1,  0 ],
                     [  2,   1,  2,  0,  1 ],
                     [  0,   1,  4,  2,  1 ],
                     [ -1,   1,  0,  2,  0 ]
                    ],

                    [
                     [  1,   0,  2,  1,  0 ],
                     [  2,   1,  3,  0,  1 ],
                     [  0,   2,  0,  3,  1 ],
                     [ -1,   1,  1,  2,  0 ]
                    ]


                ]



        the_queue = Queue()

        rc = overflow(grid,the_queue)

        self.assertEqual(rc, 2)
        rc = overflow(grid_2,the_queue)

        self.assertEqual(rc, 4)

        for i in range(len(steps)):
            tmp = the_queue.dequeue()
            self.assertEqual(tmp,steps[i])



if __name__ == '__main__':
    unittest.main()
