''' 09. --- Right to Left --- Elementary

You are given a sequence of strings. You should join these strings 
into chunk of text where the initial 
strings are separated by commas. As a joke on the right handed robots, 
you should replace all cases of the words "right" with the word "left", 
even if it's a part of another word. All strings are given in lowercase.

Input:              A sequence of strings as a tuple 
                    of strings (unicode).
Output:             The text as a string.
How it is used:     This is a simple example of operations 
                    using strings and sequences.
Precondition:       0 < len(phrases) < 42

'''

# My solution:
def left_join(phrases):
    output_s = ",".join(phrases)
    return output_s.replace("right", "left")

# mr.floppy's solution:
def left_join(phrases):
    return (",".join(phrases)).replace("right","left")

''' To remember:

.join() return 'str' object and I can call its built-in methods at once.

>> ''.join(['a', 'b', 'c']).replace('b', 'e').title()
Aec

'''
