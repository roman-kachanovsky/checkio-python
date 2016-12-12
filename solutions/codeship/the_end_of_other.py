""" --- The End of Other --- Simple

For language training our Robots want to learn about suffixes.

In this task, you are given a set of words in lower case.
Check whether there is a pair of words, such that one word is
the end of another (a suffix of another).

For example: {"hi", "hello", "lo"} -- "lo" is the end of "hello",
so the result is True.

Input:              Words as a set of strings.
Output:             True or False, as a boolean.
How it is used:     Here you can learn about iterating through
                    set type and string data type functions.
Precondition:       2 <= len(words) < 30
                    all(re.match(r"\A[a-z]{1,99}\Z", w) for w in words)

"""


def my_solution(words_set):
    return any(a.endswith(b) for a in words_set for b in words_set if a != b)


def panaro32_solution(s):
    return any(map(lambda x: any(map(x.endswith, s - set([x]))), s))
