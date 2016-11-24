import unittest

from solutions.alice_in_wonderland.saw_the_stick import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution(10), [1, 3, 6])
        self.assertEqual(my_solution(64), [15, 21, 28])
        self.assertEqual(my_solution(371), [36, 45, 55, 66, 78, 91])
        self.assertEqual(my_solution(225), [105, 120])
        self.assertEqual(my_solution(882), [])


if __name__ == '__main___':
    unittest.main()
