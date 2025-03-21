from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        aTotal = 0
        for i in range(n):
            if s[i] == 'a':
                aTotal += 1

        aCount = 0
        bCount = 0
        res = float('inf')

        for i in range(n):
            if s[i] == 'a':
                aCount += 1
            if s[i] == 'b':
                bCount += 1

            ac = aTotal - aCount
            r = bCount + ac
            if aCount == 0:
                r = min(r, aTotal)

            res = min(res, r)


        return res

'''

a a b a b b a b
1 2 2 3 3 3 4 4
0 0 1 1 2 3 3 4

'''


def test ():
    params = [
        {
            'input': 'aababbab',
            'output': 2,
        },
        {
            'input': 'bbaaaaabb',
            'output': 2,
        },
        {
            'input': 'bbbbaa',
            'output': 2,
        },
        {
            'input': 'bbbbaaaaa',
            'output': 4,
        },
        {
            'input': 'abbbbaa',
            'output': 2,
        },
        {
            'input': 'ababababaaaaa',
            'output': 4,
        },
    ]
    solution = Solution()

    for param in params:
        s = param['input']
        result = solution.minimumDeletions(s)
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
