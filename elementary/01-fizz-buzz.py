""" 01. --- Fizz Buzz --- Elementary

You should write a function that will receive a positive integer 
and return:
    "Fizz Buzz" if the number is divisible by 3 and by 5;
    "Fizz" if the number is divisible by 3;
    "Buzz" if the number is divisible by 5; 
    The number as a string for other cases.

Input:              A number as an integer.
Output:             The answer as a string.
How it is used:     Here you can learn how to write the simplest 
                    function and work with if-else statements.
Precondition:       0 < number <= 1000

"""


def my_solution(number):
    if (not number % 3) and (not number % 5):
        return "Fizz Buzz"
    elif not number % 3:
        return "Fizz"
    elif not number % 5:
        return "Buzz"
    else:
        return str(number)


def panaro32_solution(n):
    return 'Fizz' * (not n % 3) + ' ' * (not n % 15) + 'Buzz' * (not n % 5) or str(n)

