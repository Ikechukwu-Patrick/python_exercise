import unittest
import Task_Five


class MyTestCase(unittest.TestCase):
    def test_something(self):
        list = [234, 56, 78, 990, 45, 78, 65, 34, 567]
        result = Task_Five.smallest_elements(list)
        self.assertEqual(34, result)  # add assertion here
