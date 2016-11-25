import unittest

from solutions.alice_in_wonderland.multiplication_table import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution(4, 6), 38)
        self.assertEqual(my_solution(2, 7), 28)
        self.assertEqual(my_solution(7, 2), 18)


if __name__ == '__main___':
    unittest.main()
