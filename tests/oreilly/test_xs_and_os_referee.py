import unittest

from solutions.oreilly.xs_and_os_referee import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution(['X.O', 'XX.', 'XOO']), 'X')
        self.assertEqual(my_solution(['OO.', 'XOX', 'XOX']), 'O')
        self.assertEqual(my_solution(['OOX', 'XXO', 'OXX']), 'D')
        self.assertEqual(my_solution(['O.X', 'XX.', 'XOO']), 'X')


if __name__ == '__main___':
    unittest.main()
