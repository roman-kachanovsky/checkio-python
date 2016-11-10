import unittest

from solutions.scientific_expedition.common_words import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution('hello,world', 'hello,earth'), 'hello')
        self.assertEqual(my_solution('one,two,three', 'four,five,six'), '')
        self.assertEqual(my_solution('one,two,three', 'four,five,one,two,six,three'), 'one,three,two')


if __name__ == '__main___':
    unittest.main()
