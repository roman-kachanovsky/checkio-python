import unittest

from solutions.oreilly.median import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution([1, 2, 3, 4, 5]), 3)
        self.assertEqual(my_solution([3, 1, 2, 5, 3]), 3)
        self.assertEqual(my_solution([1, 300, 2, 200, 1]), 2)
        self.assertEqual(my_solution([3, 6, 20, 99, 10, 15]), 12.5)
        self.assertEqual(my_solution(xrange(1000000)), 499999.5)


if __name__ == '__main___':
    unittest.main()
