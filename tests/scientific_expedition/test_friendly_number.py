import unittest

from solutions.scientific_expedition.friendly_number import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution(102), '102')
        self.assertEqual(my_solution(10240), '10k')
        self.assertEqual(my_solution(12341234, decimals=1), '12.3M')
        self.assertEqual(my_solution(12461, decimals=1), '12.5k')
        self.assertEqual(my_solution(1024000000, base=1024, suffix='iB'), '976MiB')
        self.assertEqual(my_solution(-155, base=100, decimals=1, powers=['', 'd', 'D']), '-1.6d')
        self.assertEqual(my_solution(255000000000, powers=['', 'k', 'M']), '255000M')
        self.assertEqual(my_solution(10**24), '1Y')


if __name__ == '__main___':
    unittest.main()
