import unittest

from solutions.dropbox.inside_block import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertTrue(my_solution(((1, 1), (1, 3), (3, 3), (3, 1)), (2, 2)))
        self.assertFalse(my_solution(((1, 1), (1, 3), (3, 3), (3, 1)), (4, 2)))
        self.assertTrue(my_solution(((1, 1), (4, 1), (2, 3)), (3, 2)))
        self.assertFalse(my_solution(((1, 1), (4, 1), (1, 3)), (3, 3)))
        self.assertTrue(my_solution(((2, 1), (4, 1), (5, 3), (3, 4), (1, 3)), (4, 3)))
        self.assertFalse(my_solution(((2, 1), (4, 1), (3, 2), (3, 4), (1, 3)), (4, 3)))
        self.assertTrue(my_solution(((1, 1), (3, 2), (5, 1), (4, 3), (5, 5), (3, 4), (1, 5), (2, 3)), (3, 3)))
        self.assertFalse(my_solution(((1, 1), (1, 5), (5, 5), (5, 4), (2, 4), (2, 2), (5, 2), (5, 1)), (4, 3)))
        self.assertTrue(my_solution(((3, 4), (4, 2), (2, 1), (1, 3)), (2, 2)))
        self.assertTrue(my_solution(((1, 1), (1, 3), (3, 3), (3, 1)), (1, 1)))
        self.assertTrue(my_solution(((0, 0), (0, 2), (2, 2), (2, 0)), (1, 0)))


if __name__ == '__main___':
    unittest.main()


