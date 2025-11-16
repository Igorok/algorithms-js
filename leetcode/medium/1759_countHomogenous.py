from typing import List
import json
from collections import deque, defaultdict
import math

class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 7 + 10**9
        N = len(s)

        res = 0
        left = 0

        for right in range(N):
            if s[right] == s[left]:
                res = (res + right - left + 1) % MOD
            else:
                left = right
                res = (res + 1) % MOD

        return res

def test ():
    params = [
        {
            'input': 'abbcccaa',
            'output': 13,
        },
        {
            'input': 'xy',
            'output': 2,
        },
        {
            'input': 'zzzzz',
            'output': 15,
        },
    ]
    solution = Solution()

    for param in params:
        s = param['input']
        result = solution.countHomogenous(s)
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
