import unittest

from solutions.scientific_expedition.verify_anagrams import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertIsInstance(my_solution('a', 'z'), bool)
        self.assertTrue(my_solution('Programming', 'Gram Ring Mop'))
        self.assertFalse(my_solution('Hello', 'Ole Oh'))
        self.assertTrue(my_solution('Kyoto', 'Tokyo'))


if __name__ == '__main___':
    unittest.main()
