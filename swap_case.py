"""
hackerrank python project 'Swap Case'
link: https://www.hackerrank.com/challenges/swap-case/problem
"""


def swap_case(s):
    result = ""
    for char in s:
        if char.isalpha() and char.isupper():
            result += char.lower()
        elif char.isalpha() and char.islower():
            result += char.upper()
        else:
            result += char
    return result


if __name__ == '__main__':
    st = input()
    print(swap_case(st))
