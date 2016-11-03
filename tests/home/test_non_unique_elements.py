import unittest

from solutions.home.non_unique_elements import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertIsInstance(my_solution([1]), list)
        self.assertEqual(my_solution([1, 2, 3, 1, 3]), [1, 3, 1, 3])
        self.assertEqual(my_solution([1, 2, 3, 4, 5]), [])
        self.assertEqual(my_solution([5, 5, 5, 5, 5]), [5, 5, 5, 5, 5])
        self.assertEqual(my_solution([10, 9, 10, 10, 9, 8]), [10, 9, 10, 10, 9])


if __name__ == '__main___':
    unittest.main()
