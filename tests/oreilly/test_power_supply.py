import unittest

from solutions.oreilly.power_supply import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution(
            [['p1', 'c1'], ['c1', 'c2']],
            {'p1': 1}
        ), {'c2'})
        self.assertEqual(my_solution(
            [['c0', 'c1'], ['c1', 'p1'], ['c1', 'c3'], ['p1', 'c4']], {'p1': 1}
        ), {'c0', 'c3'})
        self.assertEqual(my_solution(
            [['p1', 'c1'], ['c1', 'c2'], ['c2', 'c3']], {'p1': 3}
        ), set())
        self.assertEqual(my_solution(
            [['c0', 'p1'], ['p1', 'c2']], {'p1': 0}
        ), {'c0', 'c2'})
        self.assertEqual(my_solution(
            [['p0', 'c1'], ['p0', 'c2'], ['c2', 'c3'], ['c3', 'p4'], ['p4', 'c5']], {'p0': 1, 'p4': 1}
        ), set())
        self.assertEqual(my_solution(
            [['c0', 'p1'], ['p1', 'c2'], ['c2', 'c3'], ['c2', 'c4'], ['c4', 'c5'],
             ['c5', 'c6'], ['c5', 'p7']],
            {'p1': 1, 'p7': 1}
        ), {'c3', 'c4', 'c6'})
        self.assertEqual(my_solution(
            [['p0', 'c1'], ['p0', 'c2'], ['p0', 'c3'],
             ['p0', 'c4'], ['c4', 'c9'], ['c4', 'c10'],
             ['c10', 'c11'], ['c11', 'p12'], ['c2', 'c5'],
             ['c2', 'c6'], ['c5', 'c7'], ['c5', 'p8']],
            {'p0': 1, 'p12': 4, 'p8': 1}
        ), {'c6', 'c7'})
        self.assertEqual(my_solution(
            [['c1', 'c2'], ['c2', 'c3']], {}
        ), {'c1', 'c2', 'c3'})
        self.assertEqual(my_solution(
            [['p1', 'c2'], ['p1', 'c4'], ['c4', 'c3'], ['c2', 'c3']], {'p1': 1}
        ), {'c3'})
        self.assertEqual(my_solution(
            [['p1', 'c2'], ['p1', 'c4'], ['c2', 'c3']], {'p1': 4}
        ), set())


if __name__ == '__main___':
    unittest.main()
