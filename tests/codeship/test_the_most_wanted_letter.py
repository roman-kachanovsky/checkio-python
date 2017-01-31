import unittest

from solutions.codeship.the_most_wanted_letter import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution('Hello World!'), 'l')
        self.assertEqual(my_solution('How do you do?'), 'o')
        self.assertEqual(my_solution('One'), 'e')
        self.assertEqual(my_solution('Oops!'), 'o')
        self.assertEqual(my_solution('AAaooo!!!!'), 'a')
        self.assertEqual(my_solution('abe'), 'a')
        self.assertEqual(my_solution('fsbd'), 'b')
        self.assertEqual(my_solution('a' * 9000 + 'b' * 1000), 'a')


if __name__ == '__main___':
    unittest.main()
