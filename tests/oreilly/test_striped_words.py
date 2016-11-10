import unittest

from solutions.oreilly.striped_words import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution('My name is ...'), 3)
        self.assertEqual(my_solution('Hello world'), 0)
        self.assertEqual(my_solution('A quantity of striped words.'), 1)
        self.assertEqual(my_solution('Dog,cat,mouse,bird.Human.'), 3)
        self.assertEqual(my_solution('1st 2a ab3er root rate'), 1)


if __name__ == '__main___':
    unittest.main()
