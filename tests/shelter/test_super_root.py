import unittest

from solutions.shelter.super_root import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        def check_result(func, n):
            result = func(n)

            if not isinstance(result, (int, float)):
                return False

            return n - 0.001 < result ** result < n + 0.001

        self.assertTrue(check_result(my_solution, 4))
        self.assertTrue(check_result(my_solution, 9))
        self.assertTrue(check_result(my_solution, 27))
        self.assertTrue(check_result(my_solution, 81))
        self.assertTrue(check_result(my_solution, 10000000000))
        self.assertTrue(check_result(my_solution, 9999999999))


if __name__ == '__main___':
    unittest.main()
