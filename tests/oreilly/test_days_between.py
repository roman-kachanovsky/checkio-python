import unittest

from solutions.oreilly.days_between import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution((1982, 4, 19), (1982, 4, 22)), 3)
        self.assertEqual(my_solution((2014, 1, 1), (2014, 8, 27)), 238)
        self.assertEqual(my_solution((2014, 8, 27), (2014, 1, 1)), 238)


if __name__ == '__main___':
    unittest.main()
