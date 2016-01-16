''' 04. --- Monkey Typing --- Elementary

You are given some text potentially including sensible words. 
You should count how many words are included in the given text. 
A word should be whole and may be a part of other word. 
Text letter case does not matter. Words are given in lowercase 
and don't repeat. If a word appears several times in the text, 
it should be counted only once.

For example, 
    text "How aresjfhdskfhskd you?", 
        words - ("how", "are", "you", "hello"). The result will be 3.

Input:              Two arguments. A text as a string (unicode for py2) 
                    and words as a set of strings (unicode for py2).
Output:             The number of words in the text as an integer.
How it is used:     Python is a useful and powerful language 
                    for text processing. 
                    This mission is only a simple example of the kind 
                    of text searching tools you could build.
Precondition:       0 < len(text) <= 256
                    all(3 <= len(w) and w.islower() and w.isalpha 
                        for w in words)

'''

# My solution:
def count_words(text, words):
    count = 0
    for w in words:
        if w in text.lower():
            count += 1
    return count

# Sim0000's solution:
def count_words(text, words):
    return sum(w in text.lower() for w in words)

''' To remember:

Notation of generators: x for x in x_list [if x ..], [] - means optional

>> a = [x for x in range(10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>> a = [x for x in range(10) if x % 2]
[1, 3, 5, 7, 9]
>> b = 3 in [x for x in range(10)] # Check if 3 is in generated list
True
>> b = [x in a for x in range(10)] # Check if each item of generated list
                                   # is in 'a' list [1, 3, 5, 7, 9]
[False, True, False, True, False, True, False, True, False, True]

>> sum([False, True, True])
2

'''