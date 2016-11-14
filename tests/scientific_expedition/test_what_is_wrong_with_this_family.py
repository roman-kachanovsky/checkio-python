import unittest

from solutions.scientific_expedition.what_is_wrong_with_this_family import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertTrue(my_solution([['Logan', 'Mike']]))
        self.assertTrue(my_solution([
            ['Logan', 'Mike'],
            ['Logan', 'Jack']
        ]))
        self.assertTrue(my_solution([
            ['Logan', 'Mike'],
            ['Logan', 'Jack'],
            ['Mike', 'Alexander']
        ]))
        self.assertFalse(my_solution([
            ['Logan', 'Mike'],
            ['Logan', 'Jack'],
            ['Mike', 'Jack']
        ]))
        self.assertFalse(my_solution([
            ['Logan', 'William'],
            ['Logan', 'Jack'],
            ['Mike', 'Alexander']
        ]))
        self.assertFalse(my_solution([
            ['Logan', 'Mike'],
            ['Logan', 'Jack'],
            ['Mike', 'Logan']
        ]))


if __name__ == '__main___':
    unittest.main()
