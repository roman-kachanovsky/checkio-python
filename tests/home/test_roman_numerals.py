import unittest

from solutions.home.roman_numerals import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution(1), 'I')
        self.assertEqual(my_solution(6), 'VI')
        self.assertEqual(my_solution(76), 'LXXVI')
        self.assertEqual(my_solution(499), 'CDXCIX')
        self.assertEqual(my_solution(3888), 'MMMDCCCLXXXVIII')


if __name__ == '__main___':
    unittest.main()
