import unittest
from lab1 import *

class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        tlist = None
        elist = []
        list1 = [1, 2, 3]
        list2 = [3, 1, 2]
        list3 = [1, 3, 2]
        list4 = [1, 1, 2]
        list5 = [2, 1, 1]
        list6 = [2, 2, 1]
        list7 = [2, 1, 2]
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
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_rec([3, 1, 2, 0]), [0, 2, 1, 3])
        self.assertEqual(reverse_rec([1, 1, 1]), [1, 1, 1])
        self.assertEqual(reverse_rec([2, 2, 1]), [1, 2, 2])
        self.assertEqual(reverse_rec([1, 2, 2]), [2, 2, 1])
        self.assertEqual(reverse_rec([]), [])
        with self.assertRaises(ValueError):
            reverse_rec(None)

    def test_bin_search(self):
        list_val =[0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), 4)
        self.assertEqual(bin_search(3, 0, 3, list_val), 3)
        self.assertEqual(bin_search(5, 1, 4, list_val), None)
        with self.assertRaises(ValueError):
            bin_search(5, 0, 4, None)
if __name__ == "__main__":
        unittest.main()

    
