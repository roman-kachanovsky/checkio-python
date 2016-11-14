import unittest

from solutions.scientific_expedition.morse_clock import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution('10:37:49'), '.- .... : .-- .--- : -.. -..-')
        self.assertEqual(my_solution('21:34:56'), '-. ...- : .-- .-.. : -.- .--.')
        self.assertEqual(my_solution('00:1:02'), '.. .... : ... ...- : ... ..-.')
        self.assertEqual(my_solution('23:59:59'), '-. ..-- : -.- -..- : -.- -..-')


if __name__ == '__main___':
    unittest.main()
