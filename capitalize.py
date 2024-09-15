"""
hackerrank python project 'Capitalize'
link: https://www.hackerrank.com/challenges/capitalize/problem
"""


def solve(fullname: str):
    return " ".join([name.capitalize() for name in fullname.split(" ")])


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
