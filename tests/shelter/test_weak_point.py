import unittest

from solutions.shelter.weak_point import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertIsInstance(my_solution([[1]]), (list, tuple))
        self.assertEqual(my_solution([
            [7, 2, 7, 2, 8],
            [2, 9, 4, 1, 7],
            [3, 8, 6, 2, 4],
            [2, 5, 2, 9, 1],
            [6, 6, 5, 4, 5]
        ]), [3, 3])
        self.assertEqual(my_solution([
            [7, 2, 4, 2, 8],
            [2, 8, 1, 1, 7],
            [3, 8, 6, 2, 4],
            [2, 5, 2, 9, 1],
            [6, 6, 5, 4, 5]
        ]), [1, 2])
        self.assertEqual(my_solution([
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]), [0, 0])


if __name__ == '__main___':
    unittest.main()
