from typing import List
import json
from collections import deque, defaultdict
import heapq

class Solution:
    def numSteps(self, s: str) -> int:
        N = len(s)

        rem = 0
        res = 0
        for i in range(N-1, -1, -1):
            val = int(s[i]) + rem
            rem = 0

            if val == 1 and i == 0:
                break

            if val == 0:
                res += 1
            elif val == 1:
                rem = 1
                res += 2
            elif val == 2:
                rem = 1
                res += 1

        return res

'''
1101

001101
001110
00111
01000
0100
010
01


'''

def test ():
    params = [
        {
            'input': '1101',
            'output': 6,
        },
        {
            'input': '10',
            'output': 1,
        },
        {
            'input': '1',
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        s = param['input']
        result = solution.numSteps(s)
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
