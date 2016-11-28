import unittest

from solutions.github.house_password import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertFalse(my_solution('A1213pokl'))
        self.assertTrue(my_solution('bAse730onE4'))
        self.assertFalse(my_solution('asasasasasasasaas'))
        self.assertFalse(my_solution('QWERTYqwerty'))
        self.assertFalse(my_solution('123456123456'))
        self.assertTrue(my_solution('QwErTy911poqqqq'))


if __name__ == '__main___':
    unittest.main()
