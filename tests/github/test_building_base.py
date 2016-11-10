import unittest

from solutions.github.building_base import MyBuilding


class TestSolution(unittest.TestCase):

    def test_solution(self):
        def json_dict(d):
            return dict((k, list(v)) for k, v in d.items())

        b1 = MyBuilding(1, 2, 2, 3)
        b2 = MyBuilding(1, 2, 2, 3, 5)

        self.assertEqual(
            json_dict(b1.corners()),
            {
                'north-east': [4, 4], 'south-east': [1, 4],
                'south-west': [1, 2], 'north-west': [4, 2]
            }
        )
        self.assertEqual(b1.area(), 6)
        self.assertEqual(b1.volume(), 60)
        self.assertEqual(b2.volume(), 30)
        self.assertEqual(str(b1), 'Building(1, 2, 2, 3, 10)')


if __name__ == '__main___':
    unittest.main()
