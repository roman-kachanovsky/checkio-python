import unittest

from solutions.dropbox.the_most_frequent_weekdays import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution(2399), ['Friday'])
        self.assertEqual(my_solution(1152), ['Tuesday', 'Wednesday'])
        self.assertEqual(my_solution(56), ['Saturday', 'Sunday'])
        self.assertEqual(my_solution(2909), ['Tuesday'])


if __name__ == '__main___':
    unittest.main()
