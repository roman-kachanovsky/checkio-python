import unittest

from solutions.elementary.index_power import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution([1, 2, 3, 4], 2), 9)
        self.assertEqual(my_solution([1, 3, 10, 100], 3), 1000000)
        self.assertEqual(my_solution([0, 1], 0), 1)
        self.assertEqual(my_solution([1, 2], 3), -1)


if __name__ == '__main___':
    unittest.main()
