import unittest

from solutions.alice_in_wonderland.the_rows_of_cakes import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]), 2)
        self.assertEqual(my_solution(
            [
                [2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2],
                [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]
            ]
        ), 6)
        self.assertEqual(my_solution([[1, 1], [1, 3], [3, 3], [1, 7], [5, 7], [7, 7]]), 3)


if __name__ == '__main___':
    unittest.main()
