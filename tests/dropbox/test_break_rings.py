import unittest

from solutions.dropbox.break_rings import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {4, 6}, {6, 5})), 3)
        self.assertEqual(my_solution(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})), 3)
        self.assertEqual(my_solution(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})), 3)
        self.assertEqual(my_solution(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4},
                                      {4, 5}, {5, 6}, {6, 7}, {8, 7})), 5)
        self.assertEqual(my_solution(({3, 4}, {1, 6}, {1, 2}, {9, 5}, {2, 5}, {9, 2}, {8, 3},
                                      {2, 4}, {8, 4}, {1, 3}, {8, 1}, {1, 7}, {6, 7})), 6)


if __name__ == '__main___':
    unittest.main()


