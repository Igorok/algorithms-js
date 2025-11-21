from typing import List
import json
from collections import deque
import heapq

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        unique = set()
        acc = [0]*26
        aOrd = ord('a')

        for char in s:
            code = ord(char) - aOrd
            acc[code] += 1

        leftAcc = [0]*26
        for char in s:
            curr = ord(char) - aOrd
            leftAcc[curr] += 1

            for i in range(26):
                l = leftAcc[i]
                r = acc[i] - leftAcc[i]
                if i == curr and l > 1 and r > 0:
                    unique.add((i, i, i))
                elif i != curr and l > 0 and r > 0:
                    unique.add((i, curr, i))


        return len(unique)


def test ():
    params = [
        {
            'input': 'aabca',
            'output': 3,
        },
        {
            'input': 'adc',
            'output': 0,
        },
        {
            'input': 'bbcbaba',
            'output': 4,
        },
    ]
    solution = Solution()

    for param in params:
        s = param['input']
        result = solution.countPalindromicSubsequence(s)
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
