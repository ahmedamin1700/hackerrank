"""
hackerrank python project 'The Minion Game'
link: https://www.hackerrank.com/challenges/the-minion-game/problem
"""

# VOWELS = "AEIOU"


# def results(d: dict):
#     total = 0
#
#     for value in d.values():
#         total += value
#     return total
#
#
# def minion_game(string):
#     result = {
#         "stuart": dict(),
#         "kevin": dict()
#     }
#     loops = 1
#
#     while loops <= len(string):
#         for i in range(len(string)):
#             if string[i] in VOWELS and (i + loops) <= len(string):
#                 word = string[i:i + loops]
#                 kevin = result["kevin"]
#                 if word in kevin.keys():
#                     kevin[word] += 1
#                 else:
#                     kevin[word] = 1
#
#             elif string[i] not in VOWELS and (i + loops) <= len(string):
#                 word = string[i:i + loops]
#                 stuart = result["stuart"]
#                 if word in stuart.keys():
#                     stuart[word] += 1
#                 else:
#                     stuart[word] = 1
#
#         loops += 1
#
#     stuart = results(result["stuart"])
#     kevin = results(result["kevin"])
#
#     if stuart > kevin:
#         print(f"Stuart {stuart}")
#     else:
#         print(f"Kevin {kevin}")

VOWELS = "AEIOU"


def minion_game(string):
    stuart_score = 0
    kevin_score = 0
    length = len(string)

    # Iterate over the string and calculate scores based on each character
    for i in range(length):
        if string[i] in VOWELS:
            # Kevin scores, all substrings starting with this vowel
            kevin_score += length - i
        else:
            # Stuart scores, all substrings starting with this consonant
            stuart_score += length - i

    # Determine the winner
    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
