import unittest

from solutions.mine.count_inversion import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution((1, 2, 5, 3, 4, 7, 6)), 3)
        self.assertEqual(my_solution((0, 1, 2, 3)), 0)
        self.assertEqual(my_solution((99, -99)), 1)
        self.assertEqual(my_solution((5, 3, 2, 1, 0)), 10)


if __name__ == '__main___':
    unittest.main()
