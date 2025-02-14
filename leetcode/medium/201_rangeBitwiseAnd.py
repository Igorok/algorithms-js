import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq
import math

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        l = bin(left)[2:]
        r = bin(right)[2:]
        n = min(len(l), len(r))
        res = ''
        for i in range(1, n+1):
            first = l[-i]
            second = r[-i]

            if first == '1' or second == '1':
                res = res + '1'
            else:
                res = res + '0'

        res = '0b'+res

        return int(res, 2)

'''

1 0 1
1 1 1

1 0 1
0 1 1
1 1 1

0 0 1 = 4


'''


def test ():
    params = [
        {
            'input': [5,7],
            'output': 4,
        },
        {
            'input': [0, 0],
            'output': 0,
        },
        {
            'input': [1, 2147483647],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        left, right = param['input']
        result = solution.rangeBitwiseAnd(left, right)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
