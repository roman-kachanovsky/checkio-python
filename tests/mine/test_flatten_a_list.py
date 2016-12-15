import unittest

from solutions.mine.flatten_a_list import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution([1, 2, 3]), [1, 2, 3])
        self.assertEqual(my_solution([1, [2, 2, 2], 4]), [1, 2, 2, 2, 4])
        self.assertEqual(my_solution([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]), [2, 4, 5, 6, 6, 6, 6, 6, 7])
        self.assertEqual(my_solution([-1, [1, [-2], 1], -1]), [-1, 1, -2, 1, -1])


if __name__ == '__main___':
    unittest.main()
