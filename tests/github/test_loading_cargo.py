import unittest

from solutions.github.loading_cargo import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution([10, 10]), 0)
        self.assertEqual(my_solution([10]), 10)
        self.assertEqual(my_solution([5, 8, 13, 27, 14]), 3)
        self.assertEqual(my_solution([5, 5, 6, 5]), 1)
        self.assertEqual(my_solution([12, 30, 30, 32, 42, 49]), 9)
        self.assertEqual(my_solution([1, 1, 1, 3]), 0)


if __name__ == '__main___':
    unittest.main()
