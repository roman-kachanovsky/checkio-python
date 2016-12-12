import unittest

from solutions.codeship.the_end_of_other import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertTrue(my_solution({'hello', 'lo', 'he'}))
        self.assertFalse(my_solution({'hello', 'la', 'hellow', 'cow'}))
        self.assertTrue(my_solution({'walk', 'duckwalk'}))
        self.assertFalse(my_solution({'one'}))
        self.assertFalse(my_solution({'helicopter', 'li', 'he'}))


if __name__ == '__main___':
    unittest.main()
