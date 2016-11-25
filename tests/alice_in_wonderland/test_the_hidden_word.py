import unittest

from solutions.alice_in_wonderland.the_hidden_word import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution(
            '''DREAMING of apples on a wall,
            And dreaming often, dear,
            I dreamed that, if I counted all,
            -How many would appear?''', 'ten'
        ), [2, 14, 2, 16])
        self.assertEqual(my_solution(
            '''He took his vorpal sword in hand:
            Long time the manxome foe he sought--
            So rested he by the Tumtum tree,
            And stood awhile in thought.
            And as in uffish thought he stood,
            The Jabberwock, with eyes of flame,
            Came whiffling through the tulgey wood,
            And burbled as it came!''', 'noir'
        ), [4, 16, 7, 16])
        self.assertEqual(my_solution(
            '''Hi all!
            And all goodbye!
            Of course goodbye.
            or not''', 'haoo'
        ), [1, 1, 4, 1])
        self.assertEqual(my_solution(
            '''xa
            xb
            x''', 'ab'
        ), [1, 2, 2, 2])


if __name__ == '__main___':
    unittest.main()
