import unittest

from solutions.alice_in_wonderland.digits_doublets import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution([123, 991, 323, 321, 329, 121, 921, 125, 999]),
                         [123, 121, 921, 991, 999])
        self.assertEqual(my_solution([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]),
                         [111, 121, 127, 727, 777])
        self.assertEqual(my_solution([456, 455, 454, 356, 656, 654]),
                         [456, 454, 654])
        self.assertEqual(my_solution([555, 545]),
                         [555, 545])


if __name__ == '__main___':
    unittest.main()
