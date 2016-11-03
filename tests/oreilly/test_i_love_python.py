import unittest

from solutions.oreilly.i_love_python import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution(), 'I love Python!')


if __name__ == '__main___':
    unittest.main()
