from typing import List
import json
from collections import deque, defaultdict
import math

class Solution:
    def numSub(self, s: str) -> int:
        MOD = 7 + 10**9
        N = len(s)
        res = 0
        left = -1

        for right in range(N):
            if s[right] == '0':
                left = -1
                continue

            if left == -1:
                left = right
                res = (res + 1) % MOD
            else:
                l = right - left + 1
                res = (res + l) % MOD

        return res


'''
0110111
11
12
-1
--
3

111
123
-12
--1
---
6



'''

def test ():
    params = [
        {
            'input': '0110111',
            'output': 9,
        },
        {
            'input': '101',
            'output': 2,
        },
        {
            'input': '111111',
            'output': 21,
        },
    ]
    solution = Solution()

    for param in params:
        s = param['input']
        result = solution.numSub(s)
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
