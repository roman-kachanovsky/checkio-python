import unittest

from solutions.shelter.texas_referee import my_solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(my_solution('Kh,Qh,Ah,9s,2c,Th,Jh'), 'Ah,Kh,Qh,Jh,Th')  # Hight Straight Flush
        self.assertEqual(my_solution('Qd,Ad,9d,8d,Td,Jd,7d'), 'Qd,Jd,Td,9d,8d')  # Straight Flush
        self.assertEqual(my_solution('5c,7h,7d,9s,9c,8h,6d'), '9c,8h,7h,6d,5c')  # Straight
        self.assertEqual(my_solution('Ts,2h,2d,3s,Td,3c,Th'), 'Th,Td,Ts,3c,3s')  # Full House
        self.assertEqual(my_solution('Jh,Js,9h,Jd,Th,8h,Td'), 'Jh,Jd,Js,Th,Td')  # Full House vs Flush
        self.assertEqual(my_solution('Js,Td,8d,9s,7d,2d,4d'), 'Td,8d,7d,4d,2d')  # Flush
        self.assertEqual(my_solution('Ts,2h,Tc,3s,Td,3c,Th'), 'Th,Td,Tc,Ts,3c')  # Four of Kind
        self.assertEqual(my_solution('Ks,9h,Th,Jh,Kd,Kh,8s'), 'Kh,Kd,Ks,Jh,Th')  # Three of Kind
        self.assertEqual(my_solution('2c,3s,4s,5s,7s,2d,7h'), '7h,7s,5s,2d,2c')  # Two Pairs
        self.assertEqual(my_solution('2s,3s,4s,5s,2d,7h,8h'), '8h,7h,5s,2d,2s')  # One Pair
        self.assertEqual(my_solution('3h,4h,Th,6s,Ad,Jc,2h'), 'Ad,Jc,Th,6s,4h')  # High Cards


if __name__ == '__main___':
    unittest.main()
