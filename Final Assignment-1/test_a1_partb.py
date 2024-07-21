#
#   Author: Catherine Leung
#   These are the unit tests for functions and classes of assingment1
#   To use this, run: python test_a1_partb.py

import unittest
from a1_partb import DoublyLinked

class A1BTestCase(unittest.TestCase):
    """These are the test cases for functions and classes of a1"""
    
    def test_init_get_len_empty(self):
        my_list = DoublyLinked()
        self.assertEqual(len(my_list), 0)
        self.assertEqual(my_list.is_empty(), True)
        self.assertEqual(my_list.get_front(), None)
        self.assertEqual(my_list.get_back(), None)
 
    def test_push_front(self):
        my_list = DoublyLinked()
        my_list.push_front(1)
        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 1)
        self.assertNotEqual(my_list.get_front(), None)
        self.assertNotEqual(my_list.get_back(), None)
        self.assertEqual(my_list.get_front().get_data(), 1)
        self.assertEqual(my_list.get_back().get_data(), 1)

        my_list.push_front(5)
        self.assertEqual(len(my_list), 2)
        self.assertEqual(my_list.get_front().get_data(), 5)
        self.assertEqual(my_list.get_back().get_data(), 1)
        self.assertEqual(my_list.get_front().get_next().get_data(), 1)
        self.assertEqual(my_list.get_back().get_previous().get_data(), 5)


        my_list.push_front(3)
        self.assertEqual(len(my_list), 3)
        self.assertEqual(my_list.get_front().get_data(), 3)
        self.assertEqual(my_list.get_back().get_data(), 1)
        self.assertEqual(my_list.get_front().get_next().get_data(), 5)
        self.assertEqual(my_list.get_front().get_next().get_next().get_data(), 1)
        self.assertEqual(my_list.get_front().get_next().get_previous().get_data(), 3)
        self.assertEqual(my_list.get_back().get_previous().get_data(), 5)

        my_list.push_front(15)
        self.assertEqual(len(my_list), 4)
        self.assertEqual(my_list.get_front().get_data(), 15)
        self.assertEqual(my_list.get_back().get_data(), 1)
        self.assertEqual(my_list.get_front().get_next().get_data(), 3)
        self.assertEqual(my_list.get_front().get_next().get_next().get_data(), 5)
        self.assertEqual(my_list.get_front().get_next().get_previous().get_data(), 15)
        self.assertEqual(my_list.get_back().get_previous().get_data(), 5)


 
    def test_push_back(self):
        my_list = DoublyLinked()
        my_list.push_back(1)
        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 1)
        self.assertEqual(my_list.get_front().get_data(), 1)
        self.assertEqual(my_list.get_back().get_data(), 1)

        my_list.push_back(5)
        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 2)
        self.assertEqual(my_list.get_front().get_data(), 1)
        self.assertEqual(my_list.get_back().get_data(), 5)
        self.assertEqual(my_list.get_front().get_next().get_data(), 5)
        self.assertEqual(my_list.get_back().get_previous().get_data(), 1)


        my_list.push_back(3)
        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 3)
        self.assertEqual(my_list.get_front().get_data(), 1)
        self.assertEqual(my_list.get_back().get_data(), 3)
        self.assertEqual(my_list.get_front().get_next().get_data(), 5)
        self.assertEqual(my_list.get_back().get_previous().get_data(), 5)
        self.assertEqual(my_list.get_back().get_previous().get_previous().get_data(), 1)
        self.assertEqual(my_list.get_back().get_previous().get_next().get_data(), 3)

        my_list.push_back(15)
        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 4)
        self.assertEqual(my_list.get_front().get_data(), 1)
        self.assertEqual(my_list.get_back().get_data(), 15)
        self.assertEqual(my_list.get_front().get_next().get_data(), 5)
        self.assertEqual(my_list.get_back().get_previous().get_data(), 3)
        self.assertEqual(my_list.get_back().get_previous().get_previous().get_data(), 5)
        self.assertEqual(my_list.get_back().get_previous().get_next().get_data(), 15)


    def test_pop_front(self):
        my_list = DoublyLinked()
        my_list.push_front(15)
        my_list.push_back(24)
        my_list.push_front(31)
        my_list.push_back(9)

        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 4)


        rc = my_list.pop_front()
        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 3)
        self.assertEqual(rc, 31)
        self.assertEqual(my_list.get_front().get_data(), 15)
        self.assertEqual(my_list.get_front().get_next().get_data(), 24)
        self.assertEqual(my_list.get_front().get_next().get_next().get_data(), 9)
        self.assertEqual(my_list.get_back().get_data(), 9)
        self.assertEqual(my_list.get_back().get_previous().get_data(), 24)
        self.assertEqual(my_list.get_back().get_previous().get_previous().get_data(), 15)


        rc = my_list.pop_front()
        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 2)
        self.assertEqual(rc, 15)
        self.assertEqual(my_list.get_front().get_data(), 24)
        self.assertEqual(my_list.get_front().get_next().get_data(), 9)
        self.assertEqual(my_list.get_back().get_data(), 9)
        self.assertEqual(my_list.get_back().get_previous().get_data(), 24)


        rc = my_list.pop_front()
        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 1)
        self.assertEqual(rc, 24)
        self.assertEqual(my_list.get_front().get_data(), 9)
        self.assertEqual(my_list.get_back().get_data(), 9)


        rc = my_list.pop_front()
        self.assertEqual(my_list.is_empty(), True)
        self.assertEqual(len(my_list), 0)
        self.assertEqual(rc, 9)
        self.assertEqual(my_list.get_front(), None)
        self.assertEqual(my_list.get_back(), None)

        with self.assertRaises(IndexError) as cm:
            rc = my_list.pop_front()
        self.assertEqual(str(cm.exception), 'pop_front() used on empty list')

 
    def test_pop_back(self):
        my_list = DoublyLinked()
        my_list.push_front(15)
        my_list.push_back(24)
        my_list.push_front(31)
        my_list.push_back(9)

        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 4)


        rc = my_list.pop_back()
        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 3)
        self.assertEqual(rc, 9)
        self.assertEqual(my_list.get_front().get_data(), 31)
        self.assertEqual(my_list.get_front().get_next().get_data(), 15)
        self.assertEqual(my_list.get_front().get_next().get_next().get_data(), 24)
        self.assertEqual(my_list.get_back().get_data(), 24)
        self.assertEqual(my_list.get_back().get_previous().get_data(), 15)
        self.assertEqual(my_list.get_back().get_previous().get_previous().get_data(), 31)


        rc = my_list.pop_back()
        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 2)
        self.assertEqual(rc, 24)
        self.assertEqual(my_list.get_front().get_data(), 31)
        self.assertEqual(my_list.get_front().get_next().get_data(), 15)
        self.assertEqual(my_list.get_back().get_data(), 15)
        self.assertEqual(my_list.get_back().get_previous().get_data(), 31)


        rc = my_list.pop_back()
        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 1)
        self.assertEqual(rc, 15)
        self.assertEqual(my_list.get_front().get_data(), 31)
        self.assertEqual(my_list.get_back().get_data(), 31)


        rc = my_list.pop_back()
        self.assertEqual(my_list.is_empty(), True)
        self.assertEqual(len(my_list), 0)
        self.assertEqual(rc, 31)
        self.assertEqual(my_list.get_front(), None)
        self.assertEqual(my_list.get_back(), None)

        with self.assertRaises(IndexError) as cm:
            rc = my_list.pop_back()
        self.assertEqual(str(cm.exception), 'pop_back() used on empty list')


    def test_search(self):
        my_list = DoublyLinked()
        my_list.push_back(1)
        my_list.push_front(15)
        my_list.push_back(24)
        my_list.push_front(31)
        my_list.push_back(9)

        rc = my_list.search(55)
        self.assertEqual(rc, None)

        rc = my_list.search(1)
        self.assertEqual(rc.get_data(), 1)
        self.assertEqual(rc.get_next().get_data(), 24)
        self.assertEqual(rc.get_previous().get_data(), 15)

        rc = my_list.search(15)
        self.assertEqual(rc.get_data(), 15)
        self.assertEqual(rc.get_next().get_data(), 1)
        self.assertEqual(rc.get_previous().get_data(), 31)


        rc = my_list.search(24)
        self.assertEqual(rc.get_data(), 24)
        self.assertEqual(rc.get_next().get_data(), 9)
        self.assertEqual(rc.get_previous().get_data(), 1)

        rc = my_list.search(31)
        self.assertEqual(rc.get_data(), 31)
        self.assertEqual(rc.get_next().get_data(), 15)

        rc = my_list.search(9)
        self.assertEqual(rc.get_data(), 9)
        self.assertEqual(rc.get_previous().get_data(), 24)


    def test_insert_after(self):
        my_list = DoublyLinked()
        my_list.push_back(1)
        my_list.push_front(15)
        my_list.push_back(24)
        my_list.push_front(31)
        my_list.push_back(9)

        
        loc = my_list.search(1)
        my_list.insert_after(23,loc)
        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 6)

        self.assertEqual(loc.get_next().get_data(), 23)
        self.assertEqual(loc.get_next().get_next().get_data(), 24)
        self.assertEqual(loc.get_next().get_previous().get_data(), 1)
        self.assertEqual(loc.get_next().get_next().get_previous().get_data(), 23)


        my_list.insert_after(36,my_list.get_back())

        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 7)

        self.assertEqual(my_list.get_back().get_data(), 36)
        self.assertEqual(my_list.get_back().get_previous().get_data(),9)
        self.assertEqual(my_list.get_back().get_previous().get_next(), my_list.get_back())


        my_list.insert_after(17,my_list.get_front())

        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 8)

        self.assertEqual(my_list.get_front().get_data(), 31)
        self.assertEqual(my_list.get_front().get_next().get_data(),17)
        self.assertEqual(my_list.get_front().get_next().get_previous(), my_list.get_front())



        my_list.insert_after(42,None)

        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 9)

        self.assertEqual(my_list.get_front().get_data(), 42)
        self.assertEqual(my_list.get_front().get_next().get_data(),31)
        self.assertEqual(my_list.get_front().get_next().get_previous(), my_list.get_front())


    def test_is_palindrome(self):
        my_list = DoublyLinked()
        self.assertEqual(my_list.is_palindrome(), True)

        my_list.push_back(5)
        self.assertEqual(my_list.is_palindrome(), True)

        my_list.push_back(5)
        self.assertEqual(my_list.is_palindrome(), True)

        my_list.push_back(5)
        self.assertEqual(my_list.is_palindrome(), True)


        my_list.push_back(2)
        self.assertEqual(my_list.is_palindrome(), False)
        my_list.push_front(2)
        self.assertEqual(my_list.is_palindrome(), True)


        my_list.push_front(1)
        self.assertEqual(my_list.is_palindrome(), False)
        my_list.push_back(1)
        self.assertEqual(my_list.is_palindrome(), True)


        my_list.push_back(42)
        self.assertEqual(my_list.is_palindrome(), False)
        my_list.push_front(42)
        self.assertEqual(my_list.is_palindrome(), True)


        my_list.push_back(16)
        self.assertEqual(my_list.is_palindrome(), False)
        my_list.push_front(16)
        self.assertEqual(my_list.is_palindrome(), True)


        my_list2 = DoublyLinked()
        for i in range (1, 100):
            my_list2.push_front(i)
        for i in range (3, 100):
            my_list2.push_back(i)
        self.assertEqual(my_list2.is_palindrome(), False)

        loc = my_list2.search(1)
        my_list2.insert_after(2,loc)
        self.assertEqual(my_list2.is_palindrome(), True)

        my_list2.insert_after(1,loc)
        self.assertEqual(my_list2.is_palindrome(), True)


if __name__ == '__main__':
    unittest.main()
