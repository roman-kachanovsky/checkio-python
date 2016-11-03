import unittest

from solutions.elementary.fizz_buzz import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution(15), 'Fizz Buzz')
        self.assertEqual(my_solution(6), 'Fizz')
        self.assertEqual(my_solution(5), 'Buzz')
        self.assertEqual(my_solution(7), '7')
        self.assertEqual(my_solution(0), 'Fizz Buzz')
        self.assertEqual(my_solution(-1), '-1')


if __name__ == '__main___':
    unittest.main()
