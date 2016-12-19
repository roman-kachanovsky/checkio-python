# -*- coding: utf-8 -*-

import unittest

from solutions.polygon.remove_accents import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution(u'préfèrent'), u'preferent')
        self.assertEqual(my_solution(u'loài trăn lớn'), u'loai tran lon')
        self.assertEqual(my_solution(u'完好無缺'), u'完好無缺')


if __name__ == '__main___':
    unittest.main()
