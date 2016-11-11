import unittest

from solutions.electronic_station.restricted_sum import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution([1, 2, 3]), 6)
        self.assertEqual(my_solution([4, 8, 1, 2, 5]), 20)
        self.assertEqual(my_solution([9, 0, 1, 1]), 11)
        self.assertEqual(my_solution([3, 3, 3]), 9)
        self.assertEqual(my_solution([8, ]), 8)


if __name__ == '__main___':
    unittest.main()
