import unittest

from solutions.codeship.monkey_typing import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution('How aresjfhdskfhskd you?',
                                     {'how', 'are', 'you', 'hello'}), 3)
        self.assertEqual(my_solution('Bananas, give me bananas!!!',
                                     {'banana', 'bananas'}), 2)
        self.assertEqual(my_solution('Lorem ipsum dolor sit amet, consectetuer adipiscing elit.',
                                     {'sum', 'hamlet', 'infinity', 'anything'}), 1)


if __name__ == '__main___':
    unittest.main()
