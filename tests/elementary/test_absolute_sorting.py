import unittest

from solutions.elementary.absolute_sorting import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution((-20, -5, 10, 15)), [-5, 10, 15, -20])
        self.assertEqual(my_solution((1, 2, 3, 0)), [0, 1, 2, 3])
        self.assertEqual(my_solution((-1, -2, -3, 0)), [0, -1, -2, -3])


if __name__ == '__main___':
    unittest.main()
