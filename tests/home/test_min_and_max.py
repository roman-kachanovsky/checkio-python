import unittest

from solutions.home.min_and_max import my_solution_min, my_solution_max


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution_max(3, 2), 3)
        self.assertEqual(my_solution_min(3, 2), 2)
        self.assertEqual(my_solution_max([1, 2, 0, 3, 4]), 4)
        self.assertEqual(my_solution_min('hello'), 'e')
        self.assertEqual(my_solution_min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]), [9, 0])
        self.assertEqual(my_solution_max(2.2, 5.6, 5.9, key=int), 5.6)


if __name__ == '__main___':
    unittest.main()
