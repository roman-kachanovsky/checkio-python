import unittest

from solutions.elementary.the_most_numbers import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):

        def _almost_equal(checked, correct, significant_digits):
            precision = 0.1 ** significant_digits
            return correct - precision < checked < correct + precision

        self.assertTrue(_almost_equal(my_solution(1, 2, 3), 2, 3))
        self.assertTrue(_almost_equal(my_solution(5, -5), 10, 3))
        self.assertTrue(_almost_equal(my_solution(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3))
        self.assertTrue(_almost_equal(my_solution(), 0, 3))


if __name__ == '__main___':
    unittest.main()
