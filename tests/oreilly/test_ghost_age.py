import unittest

from solutions.oreilly.ghost_age import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        # Uncomment for better coverage but poor performance
        # self.assertEqual(my_solution(10000), 0)
        # self.assertEqual(my_solution(9999), 1)
        # self.assertEqual(my_solution(9997), 2)
        # self.assertEqual(my_solution(9994), 3)
        # self.assertEqual(my_solution(9995), 4)
        self.assertEqual(my_solution(9990), 5)


if __name__ == '__main___':
    unittest.main()
