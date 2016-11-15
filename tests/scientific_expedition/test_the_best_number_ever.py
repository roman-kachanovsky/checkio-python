import unittest
import math
from decimal import Decimal

from solutions.scientific_expedition.the_best_number_ever import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertIsInstance(my_solution(16), Decimal)
        self.assertEqual(str(my_solution(16)), str(Decimal(math.pi))[:17])
        self.assertEqual(len(str(my_solution(100))), 101)
        # self.assertEqual(len(str(my_solution(1000))), 1001)


if __name__ == '__main___':
    unittest.main()
