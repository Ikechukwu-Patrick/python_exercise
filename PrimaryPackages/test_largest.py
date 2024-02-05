import unittest
import TaskFour


class GetLargest(unittest.TestCase):

    def test_large_number(self):
        list1 = [34, 54, 67, 89, 76, 56, 98]
        result = TaskFour.get_largest(list1)
        self.assertEqual(98, result)


#if __name__ == '__main__':
    #unittest.main
