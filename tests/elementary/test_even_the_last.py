import unittest

from solutions.elementary.even_the_last import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution([0, 1, 2, 3, 4, 5]), 30)
        self.assertEqual(my_solution([1, 3, 5]), 30)
        self.assertEqual(my_solution([6]), 36)
        self.assertEqual(my_solution([]), 0)


if __name__ == '__main___':
    unittest.main()
