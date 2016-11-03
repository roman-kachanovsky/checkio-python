import unittest

from solutions.elementary.right_to_left import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution(("left", "right", "left", "stop")), "left,left,left,stop")
        self.assertEqual(my_solution(("bright aright", "ok")), "bleft aleft,ok")
        self.assertEqual(my_solution(("brightness wright",)), "bleftness wleft")
        self.assertEqual(my_solution(("enough", "jokes")), "enough,jokes")


if __name__ == '__main___':
    unittest.main()
