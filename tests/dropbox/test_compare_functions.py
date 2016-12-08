import unittest

from solutions.dropbox.compare_functions import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution(
            lambda x, y: x + y,
            lambda x, y: (x ** 2 - y ** 2) / (x - y)
        )(1, 3), (4, 'same'))
        self.assertEqual(my_solution(
            lambda x, y: x + y,
            lambda x, y: (x ** 2 - y ** 2) / (x - y)
        )(1, 2), (3, 'same'))
        self.assertEqual(my_solution(
            lambda x, y: x + y,
            lambda x, y: (x ** 2 - y ** 2) / (x - y)
        )(1, 1.01), (2.01, 'different'))
        self.assertEqual(my_solution(
            lambda x, y: x + y,
            lambda x, y: (x ** 2 - y ** 2) / (x - y)
        )(1, 1), (2, 'g_error'))

        f = lambda nums: [x for x in nums if ~x % 2]

        def g(nums):
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    nums.pop(i)
            return nums

        self.assertEqual(my_solution(f, g)([2, 4, 6, 8]), ([2, 4, 6, 8], 'same'))
        self.assertEqual(my_solution(f, g)([2, 3, 4, 6, 8]), ([2, 4, 6, 8], 'g_error'))

        self.assertEqual(my_solution(
            lambda n: ("Fizz " * (1 - n % 3) + "Buzz " * (1 - n % 5))[:-1] or str(n),
            lambda n: ('Fizz' * (n % 3 == 0) + ' ' + 'Buzz' * (n % 5 == 0)).strip()
        )(6), ('Fizz', 'same'))
        self.assertEqual(my_solution(
            lambda n: ("Fizz " * (1 - n % 3) + "Buzz " * (1 - n % 5))[:-1] or str(n),
            lambda n: ('Fizz' * (n % 3 == 0) + ' ' + 'Buzz' * (n % 5 == 0)).strip()
        )(30), ('Fizz Buzz', 'same'))
        self.assertEqual(my_solution(
            lambda n: ("Fizz " * (1 - n % 3) + "Buzz " * (1 - n % 5))[:-1] or str(n),
            lambda n: ('Fizz' * (n % 3 == 0) + ' ' + 'Buzz' * (n % 5 == 0)).strip()
        )(7), ('7', 'different'))


if __name__ == '__main___':
    unittest.main()
