import unittest

from solutions.electronic_station.brackets import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertTrue(my_solution('((5+3)*2+1)'))
        self.assertTrue(my_solution('{[(3+1)+2]+}'))
        self.assertFalse(my_solution('(3+{1-1)}'))
        self.assertTrue(my_solution('[1+1]+(2*2)-{3/3}'))
        self.assertFalse(my_solution('(({[(((1)-2)+3)-3]/3}-3)'))
        self.assertTrue(my_solution('2+3'))


if __name__ == '__main___':
    unittest.main()
