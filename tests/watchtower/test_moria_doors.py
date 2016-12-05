import unittest

from solutions.watchtower.moria_doors import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution('Speak friend and enter.'), 'friend')
        self.assertEqual(my_solution('Friend Fred and friend Ted.'), 'friend')
        self.assertEqual(my_solution('Beard and Bread'), 'bread')
        self.assertEqual(my_solution('The Doors of Durin, Lord of Moria. Speak friend and enter. '
                                     'I Narvi made them. Celebrimbor of Hollin drew these signs'), 'durin')
        self.assertEqual(my_solution('Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy.'
                                     ' According to a researcher at Cambridge University.'), 'according')
        self.assertEqual(my_solution('One, two, two, three, three, three.'), 'three')


if __name__ == '__main___':
    unittest.main()
