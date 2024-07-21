#
#   Author: Catherine Leung
#   These are the unit tests for functions and classes of lab 0
#   To use this, run: python test_lab0.py
#   Tested using Python 3.10
#

import unittest
from lab0 import sum

class Lab0TestCase(unittest.TestCase):
    """These are the test cases for functions and classes of lab0"""
    
    def test_sum(self):
        self.assertEqual(sum(3,4),7)
        self.assertEqual(sum(2,-10),-8)
        self.assertEqual(sum(12, 6),18)
        self.assertEqual(sum(8,7),15)

 
if __name__ == '__main__':
    unittest.main()
