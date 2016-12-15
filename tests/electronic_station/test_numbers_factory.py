import unittest

from solutions.electronic_station.numbers_factory import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution(20), 45)
        self.assertEqual(my_solution(21), 37)
        self.assertEqual(my_solution(17), 0)
        self.assertEqual(my_solution(33), 0)
        self.assertEqual(my_solution(3125), 55555)
        self.assertEqual(my_solution(9973), 0)
        self.assertEqual(my_solution(560), 2578)


if __name__ == '__main___':
    unittest.main()

