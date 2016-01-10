''' 12. --- The end of other --- Simple

In this task, you are given a set of words in lower case. 
Check whether there is a pair of words, such that one word is the end of another (a suffix of another). 
For example: 
    {"hi", "hello", "lo"} -- "lo" is the end of "hello", so the result is True.

Input:              Words as a set of strings.
Output:             True or False, as a boolean.
How it is used:     Here you can learn about iterating through set type and string data type functions.
Precondition:       2 ≤ len(words) < 30
                    all(re.match(r"\A[a-z]{1,99}\Z", w) for w in words)
'''

# My solution:
def checkio(words_set):
    for w1 in words_set:
        for w2 in words_set:
            if (w1 == w2[len(w2)-len(w1):]) and (w1 != w2):
                return True
    return False

# bryukh's solution:
def checkio(words):
    for w1 in words:
        for w2 in words:
            if w1 != w2 and (w1.endswith(w2) or w2.endswith(w1)):
                return True
    return False

# panaro32's solution:
def checkio(s):
    return any(map(lambda x: any(map(x.endswith,s-set([x]))),s))
