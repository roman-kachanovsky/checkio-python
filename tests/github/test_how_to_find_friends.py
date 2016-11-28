import unittest

from solutions.github.how_to_find_friends import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertTrue(my_solution(
            (
                'dr101-mr99', 'mr99-out00', 'dr101-out00', 'scout1-scout2',
                'scout3-scout1', 'scout1-scout4', 'scout4-sscout', 'sscout-super'
            ),
            'scout2', 'scout3'))
        self.assertTrue(my_solution(
            (
                'dr101-mr99', 'mr99-out00', 'dr101-out00', 'scout1-scout2',
                'scout3-scout1', 'scout1-scout4', 'scout4-sscout', 'sscout-super'
            ),
            'super', 'scout2'))
        self.assertFalse(my_solution(
            (
                'dr101-mr99', 'mr99-out00', 'dr101-out00', 'scout1-scout2',
                'scout3-scout1', 'scout1-scout4', 'scout4-sscout', 'sscout-super'
            ),
            'dr101', 'sscout'))


if __name__ == '__main___':
    unittest.main()
