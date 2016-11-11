import unittest

from solutions.scientific_expedition.the_angles_of_a_triangle import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution(4, 4, 4), [60, 60, 60])
        self.assertEqual(my_solution(3, 4, 5), [37, 53, 90])
        self.assertEqual(my_solution(2, 2, 5), [0, 0, 0])
        self.assertEqual(my_solution(10, 20, 30), [0, 0, 0])


if __name__ == '__main___':
    unittest.main()
