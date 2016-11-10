""" --- Brackets --- Elementary

You are given an expression with numbers, brackets and operators.
For this task only the brackets matter. Brackets come in three flavors:
"{}" "()" or "[]". Brackets are used to determine scope or to restrict
some expression. If a bracket is open, then it must be closed with
a closing bracket of the same type. The scope of a bracket must
not intersected by another bracket. In this task you should make
a decision, whether to correct an expression or not based
on the brackets. Do not worry about operators and operands.

Input:              An expression with different of types brackets
                    as a string (unicode).
Output:             A verdict on the correctness of the expression
                    in boolean (True or False).
How it is used:     When you write code or complex expressions in
                    a mathematical package, you can get a huge headache
                    when it comes to excess or missing brackets.
                    This concept can be useful for your own IDE.
Precondition:       There are only brackets ("{}" "()" or "[]"),
                    digits or operators ("+" "-" "*" "/").
                    0 < len(expression) < 103

"""


BRACKETS = ('{', '(', '[', ']', ')', '}')


def my_solution(expression):
    def _reverse_bracket(br):
        return ')' if br == '(' else ']' if br == '[' else '}'

    brackets = [ch for ch in expression if ch in BRACKETS]
    stack = []

    for bracket in brackets:
        # Open bracket
        if bracket in BRACKETS[:3]:
            stack.append(bracket)

        # Close bracket
        if bracket in BRACKETS[3:]:
            if not stack:
                return False

            if bracket == _reverse_bracket(stack[-1]):
                stack = stack[:-1]
            else:
                return False
    return not stack


# TODO: Investigate most clear solution here:
# https://py.checkio.org/mission/brackets/publications/review/clear/
