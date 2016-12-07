import unittest

from solutions.dropbox.moore_neighbourhood import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution(
            (
                (1, 0, 0, 1, 0),
                (0, 1, 0, 0, 0),
                (0, 0, 1, 0, 1),
                (1, 0, 0, 0, 0),
                (0, 0, 1, 0, 0),
            ),
            1, 2), 3)
        self.assertEqual(my_solution(
            (
                (1, 0, 0, 1, 0),
                (0, 1, 0, 0, 0),
                (0, 0, 1, 0, 1),
                (1, 0, 0, 0, 0),
                (0, 0, 1, 0, 0)
            ),
            0, 0), 1)
        self.assertEqual(my_solution(
            (
                (1, 1, 1),
                (1, 1, 1),
                (1, 1, 1)
            ),
            0, 2), 3)
        self.assertEqual(my_solution(
            (
                (0, 0, 0),
                (0, 1, 0),
                (0, 0, 0)
            ),
            1, 1), 0)


if __name__ == '__main___':
    unittest.main()
