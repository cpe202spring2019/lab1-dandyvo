import unittest
from lab1 import *

class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        tlist = None        
        elist = []      
        list1 = [1, 2, 3]       # ascending list
        list2 = [3, 1, 2]       # highest val first
        list3 = [1, 3, 2]       # highest val middle
        list4 = [1, 1, 2]       # highest val last, duplicate numbers
        list5 = [2, 1, 1]       # highest val first, duplicate numbers
        list6 = [2, 2, 1]       # highest val first two
        list7 = [2, 1, 2]       # highest val on boundaries
        self.assertEqual(max_list_iter(list1), 3)
        self.assertEqual(max_list_iter(list2), 3)
        self.assertEqual(max_list_iter(list3), 3)
        self.assertEqual(max_list_iter(list4), 2)
        self.assertEqual(max_list_iter(list5), 2)
        self.assertEqual(max_list_iter(list6), 2)
        self.assertEqual(max_list_iter(list7), 2)
        self.assertEqual(max_list_iter(elist), None)
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1]) # ascending order
        self.assertEqual(reverse_rec([3, 1, 2, 0]), [0, 2, 1, 3])   # random numbers
        self.assertEqual(reverse_rec([1, 1, 1]), [1, 1, 1]) # identical numbers
        self.assertEqual(reverse_rec([2, 2, 1]), [1, 2, 2]) # duplicate numbers
        self.assertEqual(reverse_rec([1, 2, 2]), [2, 2, 1]) 
        self.assertEqual(reverse_rec([]), [])
        with self.assertRaises(ValueError):
            reverse_rec(None)

    def test_bin_search(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        self.assertEqual(bin_search(4, 0, 8, list_val), 4) # middle
        self.assertEqual(bin_search(3, 0, 3, list_val), 3)  # upper boundary
        self.assertEqual(bin_search(4, 4, 8, list_val), 4)  # lower boundary
        self.assertEqual(bin_search(5, 1, 4, list_val), None)   # val not in low-high
        self.assertEqual(bin_search(9, 0, 8, list_val), 7)  # upper half
        self.assertEqual(bin_search(3, 0, 8, list_val), 3)  # lower half
        with self.assertRaises(ValueError):
            bin_search(5, 0, 4, None)


if __name__ == "__main__":
        unittest.main()

    
