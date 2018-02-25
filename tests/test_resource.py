import unittest
from src.resource import Resource
from src.exception import NoPointsError


class TestResource(unittest.TestCase):
    def setUp(self):
        self.res = Resource(10)

    def test_hasPointsLeft_returnsTrue(self):
        self.assertTrue(self.res.has_points_left())

    def test_subtractAllPoints_hasNoPointsLeft(self):
        self.res.subtract(10)
        self.assertFalse(self.res.has_points_left())

    def test_subtractMorePointsThatResourceHas_raiseNoPointsError(self):
        with self.assertRaises(NoPointsError):
            self.res.subtract(14)

    def test_getResourceValue_returnCorrectIntegerValue(self):
        self.assertEquals(self.res.value, 10)
