import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq
import math

class Solution:
    def myPow(self, x: float, n: int) -> float:
        pows = {}
        pows[1] = x
        def rec(n: int):
            if n == 0:
                return 1

            if n in pows:
                return pows[n]

            h1 = h2 = n // 2
            if (n % 2) == 1:
                h2 += 1

            pows[n] = rec(h1) * rec(h2)

            return pows[n]

        if n > 0:
            return rec(n)
        else:
            return 1 / rec(-n)

def test ():
    params = [
        {
            'input': [2.00000, 10],
            'output': 1024,
        },
        {
            'input': [2.10000, 3],
            'output': 9.26100,
        },
        {
            'input': [2.00000, -2],
            'output': 0.25000,
        },
        {
            'input': [0.00001, 2147483647],
            'output': 0.25000,
        },
    ]
    solution = Solution()

    for param in params:
        x, n = param['input']
        result = solution.myPow(x, n)
        correct = result == param['output']

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
