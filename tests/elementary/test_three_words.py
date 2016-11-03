import unittest

from solutions.elementary.three_words import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertTrue(my_solution('Hello World hello'))
        self.assertFalse(my_solution('He is 123 man'))
        self.assertFalse(my_solution('1 2 3 4'))
        self.assertTrue(my_solution('bla bla bla bla'))
        self.assertFalse(my_solution('Hi'))


if __name__ == '__main___':
    unittest.main()
