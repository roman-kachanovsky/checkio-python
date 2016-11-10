import unittest

from solutions.oreilly.friends import MyFriends


class TestSolution(unittest.TestCase):

    def test_solution(self):
        letter_friends = MyFriends(({'a', 'b'}, {'b', 'c'},
                                    {'c', 'a'}, {'a', 'c'}))
        digit_friends = MyFriends(({'1', '2'}, {'3', '1'}))

        self.assertTrue(letter_friends.add({'c', 'd'}))
        self.assertFalse(letter_friends.add({'c', 'd'}))
        self.assertTrue(letter_friends.remove({'c', 'd'}))
        self.assertFalse(digit_friends.remove({'c', 'd'}))
        self.assertEqual(letter_friends.names(), {'a', 'b', 'c'})
        self.assertEqual(letter_friends.connected('d'), set())
        self.assertEqual(letter_friends.connected('a'), {'b', 'c'})


if __name__ == '__main___':
    unittest.main()
