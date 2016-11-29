import unittest

from solutions.github.determine_the_order import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution(['acb', 'bd', 'zwa']), 'zwacbd')
        self.assertEqual(my_solution(['klm', 'kadl', 'lsm']), 'kadlsm')
        self.assertEqual(my_solution(['a', 'b', 'c']), 'abc')
        self.assertEqual(my_solution(['aazzss']), 'azs')
        self.assertEqual(my_solution(['dfg', 'frt', 'tyg']), 'dfrtyg')
        self.assertEqual(my_solution(['is', 'not', 'abc', 'nots', 'iabcn']), 'iabcnots')


if __name__ == '__main___':
    unittest.main()
