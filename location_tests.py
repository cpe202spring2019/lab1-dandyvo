import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        loc1 = Location("ATL", 500.5, -253.3)
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")
        self.assertEqual(repr(loc1), "Location('ATL', 500.5, -253.3)")
    
    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7) 
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("ATL", 500.5, -253.3)
        self.assertEqual(loc, loc1)
        self.assertNotEqual(loc, loc2)
        self.assertNotEqual(loc1, loc2)

if __name__ == "__main__":
        unittest.main()
