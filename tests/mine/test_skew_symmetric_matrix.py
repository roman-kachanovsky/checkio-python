import unittest

from solutions.mine.skew_simmetric_matrix import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertTrue(my_solution([
            [0, 1, 2],
            [-1, 0, 1],
            [-2, -1, 0]
        ]))
        self.assertFalse(my_solution([
            [0, 1, 2],
            [-1, 1, 1],
            [-2, -1, 0]
        ]))
        self.assertFalse(my_solution([
            [0, 1, 2],
            [-1, 0, 1],
            [-3, -1, 0]
        ]))


if __name__ == '__main___':
    unittest.main()
