import unittest

from solutions.home.cipher_map import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution(
            (
                'X...',
                '..X.',
                'X..X',
                '....'
            ),
            (
                'itdf',
                'gdce',
                'aton',
                'qrdi'
            )), 'icantforgetiddqd'
        )
        self.assertEqual(my_solution(
            (
                '....',
                'X..X',
                '.X..',
                '...X'
            ),
            (
                'xhwc',
                'rsqx',
                'xqzz',
                'fyzr'
            )), 'rxqrwsfzxqxzhczy'
        )


if __name__ == '__main___':
    unittest.main()
