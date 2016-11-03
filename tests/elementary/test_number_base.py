import unittest

from solutions.elementary.number_base import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution("AF", 16), 175)
        self.assertEqual(my_solution("101", 2), 5)
        self.assertEqual(my_solution("101", 5), 26)
        self.assertEqual(my_solution("Z", 36), 35)
        self.assertEqual(my_solution("AB", 10), -1)


if __name__ == '__main___':
    unittest.main()
