import unittest

from solutions.alice_in_wonderland.humpty_dumpty_form import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution(4, 2), [8.38, 21.48])
        self.assertEqual(my_solution(2, 2), [4.19, 12.57])
        self.assertEqual(my_solution(2, 4), [16.76, 34.69])


if __name__ == '__main___':
    unittest.main()
