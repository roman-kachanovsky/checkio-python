import unittest

from solutions.elementary.digits_multiplication import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution(123405), 120)
        self.assertEqual(my_solution(999), 729)
        self.assertEqual(my_solution(1000), 1)
        self.assertEqual(my_solution(1111), 1)


if __name__ == '__main___':
    unittest.main()
