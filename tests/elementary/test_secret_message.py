import unittest

from solutions.elementary.secret_message import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution('How are you? Eh, ok. Low or Lower? Ohhh.'), 'HELLO')
        self.assertEqual(my_solution('hello world!'), '')
        self.assertEqual(my_solution('HELLO WORLD!!!'), 'HELLOWORLD')


if __name__ == '__main___':
    unittest.main()
