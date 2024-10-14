from typing import List
import json

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if s == '':
            return t

        count = {}
        for char in s:
            c = count.get(char, 0)
            count[char] = c + 1

        res = ''
        for char in t:
            c = count.get(char, 0)
            if c != 0:
                count[char] = c - 1
            else:
                res += char

        return res



def test ():
    params = [
        {
            'input': ["abcd", "abcde"],
            'output': 'e',
        },
        {
            'input': ["", "y"],
            'output': "y",
        },
        {
            'input': ["a", "aa"],
            'output': "a",
        },
    ]
    solution = Solution()

    for param in params:
        s, t = param['input']
        result = solution.findTheDifference(s, t)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
