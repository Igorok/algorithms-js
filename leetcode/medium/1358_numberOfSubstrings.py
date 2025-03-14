from typing import List
import json
from collections import deque, defaultdict
import math

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        abc = 'abc'
        abcDict = {}
        res = 0
        start = 0

        for end in range(n):
            char = s[end]
            if char in abc:
                abcDict[char] = abcDict.get(char, 0) + 1

            while len(abcDict) == 3:
                res += n - end

                prev = s[start]
                abcDict[prev] -= 1
                if abcDict[prev] == 0:
                    abcDict.pop(prev)

                start += 1

        return res

'''

abcabcaaa
9-2=7
9-3=6
9-4=5
9-5=4
9-6=3

'''

def test ():
    params = [
        {
            'input': 'abcabc',
            'output': 10,
        },
        {
            'input': 'aaacb',
            'output': 3,
        },
        {
            'input': 'abc',
            'output': 1,
        },
        {
            'input': 'abcabcaaa',
            'output': 25,
        },
    ]
    solution = Solution()

    for param in params:
        s = param['input']
        result = solution.numberOfSubstrings(s)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
