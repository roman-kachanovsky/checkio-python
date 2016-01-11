''' 21. --- I love Python! --- Elementary

Let's write an essay in python code which will explain why you love python 
(if you don't love it, when we will make an additional mission special for the haters). 
Publishing the default solution will only earn you 0 points as the goal 
is to earn points through votes for your code essay.

Input:              Nothing.
Output:             The string "I love Python!".
How it is used:     This mission revolves around code literacy.
'''

# My solution:
import string
from itertools import product
​
def is_correct_phrase(s):
    return True if s == 'I love Python!' else False
​
def bruteforce(count_of_symbols):
    '''
        54^14 = 1.792720718×10^24 combinations
        Over 2 million years to iterate all of them
    '''
    # We use all latin letters plus ' ' and '!' symbols: 
    # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !'
    # and got our list of combinations. 
    # Each of them have length = 14 like the 'I love Python!' string.
    list_of_combinations = product(string.ascii_letters+' '+'!', 
        repeat=count_of_symbols)
    
    # aaaaaaaaaaaaaa
    # aaaaaaaaaaaaab
    # aaaaaaaaaaaaac
    # ...
​
    # Now try to find our phrase here!
    for c in [list('I love Python!'),]:         # Comment this line!
    # for c in list_of_combinations:            # Uncomment this line!
        if is_correct_phrase(''.join(c)):
            return ''.join(c)
    return None
​
def i_love_python():
    return bruteforce(14)
​
if __name__ == '__main__':
    assert i_love_python() == 'I love Python!'
