import unittest

from solutions.github.ore_in_the_desert import my_solution


class TestSolution(unittest.TestCase):
    def test_solution(self):
        def check(func, ore):
            recent_data = []
            for step in xrange(4):
                row, col = func([d[:] for d in recent_data])
                if row < 0 or row > 9 or col < 0 or col > 9:
                    return False
                if (row, col) == ore:
                    return True
                dist = round(((row - ore[0]) ** 2 + (col - ore[1]) ** 2) ** 0.5)
                recent_data.append([row, col, dist])
            return False

        self.assertTrue(check(my_solution, (1, 1)))
        self.assertTrue(check(my_solution, (9, 9)))
        self.assertTrue(check(my_solution, (6, 6)))
        self.assertTrue(check(my_solution, (5, 5)))


if __name__ == '__main___':
    unittest.main()
