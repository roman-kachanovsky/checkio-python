import unittest

from solutions.github.black_holes import my_solution


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(my_solution([(2, 4, 2), (3, 9, 3)]), [(2, 4, 2), (3, 9, 3)])
        self.assertEqual(my_solution([(0, 0, 2), (-1, 0, 2)]), [(0, 0, 2), (-1, 0, 2)])
        self.assertEqual(my_solution([(4, 3, 2), (2.5, 3.5, 1.4)]), [(4, 3, 2.44)])
        self.assertEqual(my_solution([(3, 3, 3), (2, 2, 1), (3, 5, 1.5)]), [(3, 3, 3.5)])


if __name__ == '__main___':
    unittest.main()
