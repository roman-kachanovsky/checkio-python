''' 01. --- Fizz Buzz --- Elementary

You should write a function that will receive a positive integer and return:
    "Fizz Buzz" if the number is divisible by 3 and by 5;
    "Fizz" if the number is divisible by 3;
    "Buzz" if the number is divisible by 5; 
    The number as a string for other cases.

Input:              A number as an integer.
Output:             The answer as a string.
How it is used:     Here you can learn how to write the simplest function and work with if-else statements.
Precondition:       0 < number ≤ 1000
'''

# My solution:
def checkio(number):
    if (number % 3 == 0) and (number % 5 == 0):
        return "Fizz Buzz"
    elif (number % 3 == 0):
        return "Fizz"
    elif (number % 5 == 0):
        return "Buzz"
    else:
        return str(number)

# panaro32's solution:
def checkio(n):
    return 'Fizz' * (not n%3) + ' ' * (not n%15) + 'Buzz' * (not n%5) or str(n)

''' 02. --- Index Power --- Elementary

You are given an array with positive numbers and a number N. 
You should find the N-th power of the element in the array with the index N. 
If N is outside of the array, then return -1. 
Don't forget that the first element has the index 0.

Let's look at a few examples:
    array = [1, 2, 3, 4] and N = 2, then the result is 32 == 9;
    array = [1, 2, 3] and N = 3, but N is outside of the array, so the result is -1.

Input:              Two arguments. An array as a list of integers and a number as a integer.
Output:             The result as an integer.
How it is used:     This mission teaches you how to use basic arrays and indexes when combined with simple mathematics.
Precondition:       0 < len(array) ≤ 10
                    0 ≤ N
                    all(0 ≤ x ≤ 100 for x in array)
'''

# My solution:
def index_power(array, n):
    if n > len(array)-1:
        return -1
    else:
        return array[n] ** n

# veky's solution:
def index_power(array, n):
    try: return array[n] ** n
    except IndexError: return -1

# gyahun_dash's solution:
def index_power(array, n):
    return array[n] ** n if n < len(array) else -1


''' 03. --- Even the last --- Elementary

You are given an array of integers. You should find the sum of the elements with even indexes (0th, 2nd, 4th...) 
then multiply this summed number and the final element of the array together. 
Don't forget that the first element has an index of 0.
For an empty array, the result will always be 0 (zero).

Input:              A list of integers.
Output:             The number as an integer.
How it is used:     Indexes and slices are important elements of coding in python and other languages. This will come in handy down the road!
Precondition:       0 ≤ len(array) ≤ 20
                    all(isinstance(x, int) for x in array)
                    all(-100 < x < 100 for x in array)
'''

# My solution:
def checkio(array):
    if len(array) == 0:
        return 0
    return sum(array[::2]) * array[len(array)-1]

# monkshorin's solution:
def checkio(array):
    if len(array) == 0: return 0
    return sum(array[0::2]) * array[-1]

# aggelgian's solution:
checkio=lambda x: sum(x[::2])*x[-1] if x else 0

''' 04. --- Monkey Typing --- Elementary
You are given some text potentially including sensible words. You should count how many words 
are included in the given text. A word should be whole and may be a part of other word. 
Text letter case does not matter. Words are given in lowercase and don't repeat. 
If a word appears several times in the text, it should be counted only once.

For example, 
    text "How aresjfhdskfhskd you?", words - ("how", "are", "you", "hello"). The result will be 3.

Input:              Two arguments. A text as a string (unicode for py2) and words as a set of strings (unicode for py2).
Output:             The number of words in the text as an integer.
How it is used:     Python is a useful and powerful language for text processing. 
                    This mission is only a simple example of the kind of text searching tools you could build.
Precondition:       0 < len(text) ≤ 256
                    all(3 ≤ len(w) and w.islower() and w.isalpha for w in words)
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

''' 05. --- Secret Message --- Elementary

You are given a chunk of text. Gather all capital letters in one word in the order that they appear in the text.
For example: 
    text = "How are you? Eh, ok. Low or Lower? Ohhh.", if we collect all of the capital letters, 
    we get the message "HELLO".

Input:              A text as a string (unicode).
Output:             The secret message as a string or an empty string.
How it is used:     This is a simple exercise in working with strings: iterate, recognize and concatenate.
Precondition:       0 < len(text) ≤ 1000
                    all(ch in string.printable for ch in text)
'''

# My solution:
def find_message(text):
    s = ''
    for c in text:
        if (c == c.upper()) and c.isalpha():
            s += c
    return s

# veky's solution:
find_message = lambda text: ''.join(filter(str.isupper, text))

# gyahun_dash's solution:
def find_message(text):
    return ''.join(c for c in text if c.isupper())

''' 06. --- Three words --- Elementary

You are given a string with words and numbers separated by whitespaces (one space). 
The words contains only letters. You should check if the string contains three words in succession. 
For example, the string "start 5 one two three 7 end" contains three words in succession.

Input:              A string with words.
Output:             The answer as a boolean.
How it is used:     This teaches you how to work with strings and introduces some useful functions.
Precondition:       The input contains words and/or numbers. There are no mixed words (letters and digits combined).
                    0 < len(words) < 100
'''

# My solution:
def checkio(words):
    lst = words.split(' ')
    counter = 0
    for l in lst:
        if l.isalpha():
            counter += 1
            if counter == 3:
                break
        else:
            counter = 0
    return (counter == 3)

# veky's solution:
def checkio(words):
    succ = 0
    for word in words.split():
        succ = (succ + 1) * word.isalpha()
        if succ == 3: return True
    else: return False

''' 07. --- The Most Numbers --- Elementary

You are given an array of numbers (floats). You should find the difference between the maximum and minimum element. 
Your function should be able to handle an undefined amount of arguments. 
For an empty argument list, the function should return 0.

Floating-point numbers are represented in computer hardware as base 2 (binary) fractions (read about this here). 
So we should check the result with ±0.001 precision.
Think about how to work with an arbitrary number of arguments.

Input:              An arbitrary number of arguments as numbers (int, float).
Output:             The difference between maximum and minimum as a number (int, float).
How it is used:     Here you will learn about passing an undefined amount of arguments to functions.
Precondition:       0 ≤ len(args) ≤ 20
                    all(-100 < x < 100 for x in args)
                    all(isinstance(x, (int, float)) for x in args)
'''

# My solution:
def checkio(*args):
    if len(args) == 0:
        return 0
    else:
        return max(args) - min(args)

# madmanbob's solution:
def checkio(*args):
    return max(args) - min(args) if args else 0

''' 08. --- Boolean Algebra --- Elementary

In this mission you should implement some boolean operations:
    "conjunction" denoted x ∧ y, satisfies x ∧ y = 1 if x = y = 1 and x ∧ y = 0 otherwise.
    "disjunction" denoted x ∨ y, satisfies x ∨ y = 0 if x = y = 0 and x ∨ y = 1 otherwise.
    "implication" (material implication) denoted x→y and can be described as ¬ x ∨ y. If x is true then the value of x → y is taken to be that of y. But if x is false then the value of y can be ignored; however the operation must return some truth value and there are only two choices, so the return value is the one that entails less, namely true.
    "exclusive" (exclusive or) denoted x ⊕ y and can be described as (x ∨ y)∧ ¬ (x ∧ y). It excludes the possibility of both x and y. Defined in terms of arithmetic it is addition mod 2 where 1 + 1 = 0.
    "equivalence" denoted x ≡ y and can be described as ¬ (x ⊕ y). It's true just when x and y have the same value.

You are given two boolean values x and y as 1 or 0 and you are given an operation name as described earlier. 
You should calculate the value and return it as 1 or 0.

Input:              Three arguments. X and Y as 0 or 1. An operation name as a string.
Output:             The result as 1 or 0.
How it is used:     Here you will learn how to work with boolean values and operators. 
                    You even get to think about numbers as booleans.
Precondition:       x in (0, 1)
                    y in (0, 1)
                    operation in ("conjunction", "disjunction", "implication", "exclusive", "equivalence")
'''

# My solution:
OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")
def boolean(x, y, operation):
    if (x in (0, 1)) and (y in (0, 1)):
        if operation in OPERATION_NAMES:
            if operation == 'conjunction':
                return x and y
            elif operation == 'disjunction':
                return x or y
            elif operation == 'implication':
                if x:
                    return y
                else:
                    return 1
            elif operation == 'exclusive':
                if x == y:
                    return 0
                else:
                    return 1
            elif operation == 'equivalence':
                if x != y:
                    return 0
                else:
                    return 1

# Sim0000's solution:
def boolean(x, y, operation):
    if operation == "conjunction": return x & y
    if operation == "disjunction": return x | y
    if operation == "implication": return (1 ^ x) | y
    if operation == "exclusive":   return x ^ y
    if operation == "equivalence": return x ^ y ^ 1
    return 0

# penguinand's solution:
def boolean(x, y, operation):
    results = {"conjunction" : x and y,
               "disjunction" : x or y,
               "implication" : y or not x,
               "exclusive"   : x ^ y,
               "equivalence" : x == y
    }
    return results[operation]

# Cjkjvfnby's solution:
from operator import and_, or_, xor, eq

def implication(x, y):
    return not x or y
​
OPERATIONS = {"conjunction": and_,
              "disjunction": or_,
              "implication": implication,
              "exclusive": xor,
              "equivalence": eq}
​
def boolean(x, y, operation):
    return OPERATIONS[operation](x, y)

''' 09. --- Right to Left --- Elementary

You are given a sequence of strings. You should join these strings into chunk of text where the initial 
strings are separated by commas. As a joke on the right handed robots, 
you should replace all cases of the words "right" with the word "left", 
even if it's a part of another word. All strings are given in lowercase.

Input:              A sequence of strings as a tuple of strings (unicode).
Output:             The text as a string.
How it is used:     This is a simple example of operations using strings and sequences.
Precondition:       0 < len(phrases) < 42
'''

# My solution:
def left_join(phrases):
    output_s = ",".join(phrases)
    return output_s.replace("right", "left")

# mr.floppy's solution:
def left_join(phrases):
    return (",".join(phrases)).replace("right","left")

''' 10. --- Digits Multiplication --- Elementary

You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.

For example: 
    The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).

Input:              A positive integer.
Output:             The product of the digits as an integer.
How it is used:     This task can teach you how to solve a problem with simple data type conversion.
Precondition:       0 < number < 106
'''

# My solution:
def checkio(number):
    s = str(number)
    result = 1
    for c in s:
        if c != '0':
            result = result * int(c)
    return result

# Cjkjvfnby's solution:
from functools import reduce
from operator import mul
​
def checkio(number):
    return reduce(mul, (int(x) for x in str(number) if x != '0'))

# bryukh's solution:
def checkio(number):
    res = 1
    for d in str(number):
        res *= int(d) if int(d) else 1
    return res

''' 11. --- Count Inversions --- Simple
You are given a sequence of unique numbers and you should count the number of inversions in this sequence.

Input:              A sequence as a tuple of integers.
Output:             The inversion number as an integer.
How it is used:     In this mission you will get to experience the wonder of nested loops, that is of course, 
                    if you don't use advanced algorithms.
Precondition:       2 < len(sequence) < 200
                    len(sequence) == len(set(sequence))
                    all(-100 < x < 100 for x in sequence)
'''

# My solution:
def count_inversion(sequence):
    count = 0
    for x in sequence:
        for y in sequence[sequence.index(x):]:
            if x > y:
                count += 1
    return count

# gyahun_dash's solution:
import itertools as it
​
def count_inversion(sequence):
    return sum(x > y for x, y in it.combinations(sequence, 2))

# bukebuer's solution:
def count_inversion(sequence):
    return sum(sum(m<n for m in sequence[i+1:]) for i,n in enumerate(sequence))

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

''' 13. --- Days Between --- Simple

You are given two dates as tuples with three numbers - year, month and day. 
For example: 
    19 April 1982 will be (1982, 4, 19). 

You should find the difference in days between the given dates. 
For example between today and tomorrow = 1 day. 
The difference will always be either a positive number or zero, so don't forget about absolute value.

Input:              Two dates as tuples of integers.
Output:             The difference between the dates in days as an integer.
How it is used:     Python has batteries included, so in this mission you will need to learn 
                    how to use completed modules so that you don't have to invent the bicycle all over again.
Precondition:       Dates between 1 january 1 and 31 december 9999. Dates are correct.
'''

# My solution:
from datetime import date

def days_diff(date1, date2):
    year, month, day = date1
    d1 = date(year=year, month=month, day=day)
    year, month, day = date2
    d2 = date(year=year, month=month, day=day)
    return abs((d2 - d1).days)

# mr.floppy's solution:
def days_diff(date1, date2):
    from datetime import date
    return abs(date(*date1) - date(*date2)).days

''' 14. --- Pangram --- Simple

For this mission, we will use the latin alphabet (A-Z). 
You are given a text with latin letters and punctuation symbols. 
You need to check if the sentence is a pangram or not. Case does not matter.

Input:              A text as a string.
Output:             Whether the sentence is a pangram or not as a boolean.
How it is used:     Pangrams have been used to display typefaces, test equipment, and develop skills in handwriting, 
                    calligraphy, and keyboarding for ages.
Precondition:       all(ch in (string.punctuation + string.ascii_letters + " ") for ch in text)
                    0 < len(text)
'''

# My solution:
import string

def check_pangram(text):
    return set(string.ascii_lowercase) == set(''.join(filter(str.isalpha, text.lower())))

# dagger126's solution:
from string import ascii_lowercase
​
def check_pangram(text):
    return set(ascii_lowercase).issubset(set(text.lower()))

# saklar13's solution:
check_pangram = lambda text: len({x for x in text.lower() if x.isalpha()}) == 26

# asa19's solution:
def check_pangram(text):
    return not set('abcdefghijklmnopqrstuvwxyz') - set(text.lower())




