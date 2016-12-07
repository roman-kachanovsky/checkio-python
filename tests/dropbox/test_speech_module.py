import unittest

from solutions.dropbox.speech_module import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution(4), 'four')
        self.assertEqual(my_solution(133), 'one hundred thirty three')
        self.assertEqual(my_solution(12), 'twelve')
        self.assertEqual(my_solution(101), 'one hundred one')
        self.assertEqual(my_solution(212), 'two hundred twelve')
        self.assertEqual(my_solution(40), 'forty')
        self.assertFalse(my_solution(212).endswith(' '))


if __name__ == '__main___':
    unittest.main()
