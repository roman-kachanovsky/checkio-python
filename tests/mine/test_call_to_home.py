import unittest

from solutions.mine.call_to_home import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution(
            (
                '2014-01-01 01:12:13 181',
                '2014-01-02 20:11:10 600',
                '2014-01-03 01:12:13 6009',
                '2014-01-03 12:13:55 200'
            )
        ), 124)
        self.assertEqual(my_solution(
            (
                '2014-02-05 01:00:00 1',
                '2014-02-05 02:00:00 1',
                '2014-02-05 03:00:00 1',
                '2014-02-05 04:00:00 1'
            )
        ), 4)
        self.assertEqual(my_solution(
            (
                '2014-02-05 01:00:00 60',
                '2014-02-05 02:00:00 60',
                '2014-02-05 03:00:00 60',
                '2014-02-05 04:00:00 6000'
            )
        ), 106)


if __name__ == '__main___':
    unittest.main()
