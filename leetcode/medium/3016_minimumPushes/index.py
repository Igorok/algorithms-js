import math
from collections import defaultdict
from typing import List

'''
aabbccddeeffgghhiiiiii

letAndOrder
{
    'a': 1, 'b': 2, 'c': 3, 'd': 1, 'e': 2, 'f': 3, 'g': 1,
    'h': 2, 'i': 3, 'j': 1, 'k': 2, 'l': 3, 'm': 1, 'n': 2,
    'o': 3, 'p': 1, 'q': 2, 'r': 3, 's': 4, 't': 1, 'u': 2,
    'v': 3, 'w': 1, 'x': 2, 'y': 3, 'z': 4
}

letByOrder
[
    [],
    ['a', 'd', 'g', 'j', 'm', 'p', 't', 'w'],
    ['b', 'e', 'h', 'k', 'n', 'q', 'u', 'x'],
    ['c', 'f', 'i', 'l', 'o', 'r', 'v', 'y'],
    ['s', 'z']
]



'''


class Solution:
    buttons = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i'],
        ['j', 'k', 'l'],
        ['m', 'n', 'o'],
        ['p', 'q', 'r', 's'],
        ['t', 'u', 'v'],
        ['w', 'x', 'y', 'z'],
    ]
    letAndOrder = {
        'a': 1, 'b': 2, 'c': 3, 'd': 1, 'e': 2, 'f': 3, 'g': 1,
        'h': 2, 'i': 3, 'j': 1, 'k': 2, 'l': 3, 'm': 1, 'n': 2,
        'o': 3, 'p': 1, 'q': 2, 'r': 3, 's': 4, 't': 1, 'u': 2,
        'v': 3, 'w': 1, 'x': 2, 'y': 3, 'z': 4
    }
    letByOrder = [
        [],
        ['a', 'd', 'g', 'j', 'm', 'p', 't', 'w'],
        ['b', 'e', 'h', 'k', 'n', 'q', 'u', 'x'],
        ['c', 'f', 'i', 'l', 'o', 'r', 'v', 'y'],
        ['s', 'z']
    ]

    def minimumPushes_(self, word: str) -> int:
        letAndOrder = {
            'a': 1, 'b': 2, 'c': 3, 'd': 1, 'e': 2, 'f': 3, 'g': 1,
            'h': 2, 'i': 3, 'j': 1, 'k': 2, 'l': 3, 'm': 1, 'n': 2,
            'o': 3, 'p': 1, 'q': 2, 'r': 3, 's': 4, 't': 1, 'u': 2,
            'v': 3, 'w': 1, 'x': 2, 'y': 3, 'z': 4
        }
        letByOrder = [
            [],
            ['a', 'd', 'g', 'j', 'm', 'p', 't', 'w'],
            ['b', 'e', 'h', 'k', 'n', 'q', 'u', 'x'],
            ['c', 'f', 'i', 'l', 'o', 'r', 'v', 'y'],
            ['s', 'z']
        ]

        letCount = {}
        for letter in word:
            c = 0 if letter not in letCount else letCount[letter]
            letCount[letter] = c + 1

        letCount = dict(sorted(letCount.items(), key=lambda item: -item[1]))

        changed = {}
        order = 1
        result = 0

        def getOrder(letter, order):
            if letAndOrder[letter] == order:
                changed[letter] = 1
                return order

            replace = None
            while len(letByOrder[order]) and not replace:
                val = letByOrder[order].pop()
                if val in changed:
                    continue
                replace = val
                changed[letter] = 1
                letByOrder[letAndOrder[letter]].append(replace)
                letAndOrder[replace], letAndOrder[letter] = letAndOrder[letter], letAndOrder[replace]

            if replace:
                return order

            return getOrder(letter, order + 1)

        for letter, count in letCount.items():
            order = getOrder(letter, order)
            result += count * order

        return result


    def minimumPushes(self, word: str) -> int:
        btnCount = 8
        letCount = {}
        for letter in word:
            c = 0 if letter not in letCount else letCount[letter]
            letCount[letter] = c + 1

        letCount = dict(sorted(letCount.items(), key=lambda item: -item[1]))

        result = 0
        i = 0
        for letter, count in letCount.items():
            order = math.floor(i / btnCount) + 1
            result += count * order
            i += 1

        return result



def test ():
    params = [
        {
            'input': 'abcde',
            'output': 5,
        },
        {
            'input': 'xyzxyzxyzxyz',
            'output': 12,
        },
        {
            'input': 'aabbccddeeffgghhiiiiii',
            'output': 24,
        },
        {
            'input': 'hueodnbjfczmivpxl',
            'output': 27,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.minimumPushes(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
