import unittest

from solutions.electronic_station.binary_count import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution(4), 1)
        self.assertEqual(my_solution(15), 4)
        self.assertEqual(my_solution(1), 1)
        self.assertEqual(my_solution(1022), 9)


if __name__ == '__main___':
    unittest.main()
