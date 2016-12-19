import unittest

from solutions.mine.pearls_in_the_box import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution('bbw', 3), 0.48)
        self.assertEqual(my_solution('wwb', 3), 0.52)
        self.assertEqual(my_solution('www', 3), 0.56)
        self.assertEqual(my_solution('bbbb', 1), 0)
        self.assertEqual(my_solution('wwbb', 4), 0.5)
        self.assertEqual(my_solution('bwbwbwb', 5), 0.48)


if __name__ == '__main___':
    unittest.main()
