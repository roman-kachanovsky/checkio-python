import unittest

from solutions.polygon.the_flat_dictionary import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution({'key': 'value'}), {'key': 'value'})
        self.assertEqual(my_solution({'key': {'deeper': {'more': {'enough': 'value'}}}}),
                         {'key/deeper/more/enough': 'value'})
        self.assertEqual(my_solution({'empty': {}}), {'empty': ''})
        self.assertEqual(my_solution(
            {
                'name': {
                    'first': 'One',
                    'last': 'Drone'
                },
                'job': 'scout',
                'recent': {},
                'additional': {
                    'place': {
                        'zone': '1',
                        'cell': '2'
                    }
                }
            }
        ), {
            'name/first': 'One',
            'name/last': 'Drone',
            'job': 'scout',
            'recent': '',
            'additional/place/zone': '1',
            'additional/place/cell': '2'
        })


if __name__ == '__main___':
    unittest.main()
