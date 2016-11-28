""" --- House Password --- Elementary

The password will be considered strong enough if its length
is greater than or equal to 10 symbols, it has at least one digit,
as well as containing one uppercase letter and one lowercase letter
in it. The password contains only ASCII latin letters or digits.

Input:              A password as a string (Unicode for python 2.7).
Output:             Is the password safe or not as a boolean or
                    any data type that can be converted and processed
                    as a boolean.
                    In the results you will see the converted results.
How it is used:     If you are worried about the security of your app
                    or service, you can check your users' passwords for
                    complexity. You can use these skills to require
                    that your users passwords
                    meet more conditions (punctuations or unicode).
Precondition:       re.match("[a-zA-Z0-9]+", password)

"""


def my_solution(data):
    import string

    return (
        data and len(data) >= 10 and
        set(string.ascii_lowercase) & set(data) and
        set(string.ascii_uppercase) & set(data) and
        set(string.digits) & set(data)
    )


renelvon_solution = lambda s: not (
    len(s) < 10
    or s.isdigit()
    or s.isalpha()
    or s.islower()
    or s.isupper()
)


def riddick_solution(data):
    import re
    return True if re.search("^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$",
                             data) and len(data) >= 10 else False


def noname_solution(data):
    import re
    if len(data) < 10: return False
    if not re.search('[a-z]', data): return False
    if not re.search('[A-Z]', data): return False
    if not re.search('[0-9]', data): return False
    return True
