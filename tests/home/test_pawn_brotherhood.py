import unittest

from solutions.home.pawn_brotherhood import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution({'b4', 'd4', 'f4', 'c3', 'e3', 'g5', 'd2'}), 6)
        self.assertEqual(my_solution({'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'e5'}), 1)


if __name__ == '__main___':
    unittest.main()
