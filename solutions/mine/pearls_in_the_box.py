""" --- Pearls in the box --- Simple

To start the game, they put several black and white pearls in one
of the boxes. Each robots have Nth moves, then initial set are restored
for a next player. For each move, the robot take a pearl out of the box
and put one of the opposite color back. The winner is the one who pulls
the white pearl on the Nth step (or +1 point if they play many parties).

Our robots don't like indeterminacy and want to know the probability
of a white pearl on the Nth step. The probability is a value between 0
(0% chance or will not happen) and 1 (100% chance or will happen).
The result is a float from 0 to 1 with two digits precision (+-0.01).

You are given a start set of pearls as a string that contains "b" (black)
and "w" (white) and the number of the step (N). The order of the pearls
does not matter.

Input:              The start sequence of the pearls as a string and
                    the step number as an integer.
Output:             The probability for a white pearl as a float.
How it is used:     This task introduces you to the basics of probability
                    theory and statistics. Fun fact: regardless of the initial
                    state, as the number of steps increases, the probability
                    approaches 0.5!
Precondition:       0 < N <= 20
                    0 < |pearls| <= 20

"""


def my_solution(marbles, step):
    from fractions import Fraction as f

    sequences = [[{marbles: f(1, 1)}], ]

    for i in xrange(step):
        curr_step = []

        for seq in sequences[i]:
            k, v = seq.keys()[0], seq.values()[0]

            if 'w' in k:
                new_seq = k.replace('w', 'b', 1)
                curr_step.append({new_seq: f(k.count('w'), len(k)) * v})

            if 'b' in k and i < step - 1:  # Ignore black pearls in last iteration
                new_seq = k.replace('b', 'w', 1)
                curr_step.append({new_seq: f(k.count('b'), len(k)) * v})

        sequences.append(curr_step)

    return round(float(sum(s.values()[0] for s in sequences[-1])), 2)


# TODO: Investigate most clear solution here:
# https://py.checkio.org/mission/box-probability/publications/category/clear/
