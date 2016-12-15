import unittest

from solutions.electronic_station.largest_rectangle_in_a_histogram import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution([5]), 5)
        self.assertEqual(my_solution([5, 3]), 6)
        self.assertEqual(my_solution([1, 1, 4, 1]), 4)
        self.assertEqual(my_solution([1, 1, 3, 1]), 4)
        self.assertEqual(my_solution([2, 1, 4, 5, 1, 3, 3]), 8)


if __name__ == '__main___':
    unittest.main()
