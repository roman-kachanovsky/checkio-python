import unittest

from solutions.codeship.golden_pyramid import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution(
            (
                (1,),
                (2, 3),
                (3, 3, 1),
                (3, 1, 5, 4),
                (3, 1, 3, 1, 3),
                (2, 2, 2, 2, 2, 2),
                (5, 6, 4, 5, 6, 4, 3)
            )
        ), 23)
        self.assertEqual(my_solution(
            (
                (1,),
                (2, 1),
                (1, 2, 1),
                (1, 2, 1, 1),
                (1, 2, 1, 1, 1),
                (1, 2, 1, 1, 1, 1),
                (1, 2, 1, 1, 1, 1, 9)
            )
        ), 15)
        self.assertEqual(my_solution(
            (
                (9,),
                (2, 2),
                (3, 3, 3),
                (4, 4, 4, 4)
            )
        ), 18)


if __name__ == '__main___':
    unittest.main()
