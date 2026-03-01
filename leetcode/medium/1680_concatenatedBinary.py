from typing import List
import json
from collections import deque, defaultdict
import heapq
import bisect


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 7 + 10**9
        acc = 0

        for i in range(1, n+1):
            v1 = bin(acc)[2:]
            v2 = bin(i)[2:]
            v = int(v1+v2, 2)
            v = v % MOD
            acc = v

        return acc




def test ():
    params = [
        {
            'input': 1,
            'output': 1,
        },
        {
            'input': 3,
            'output': 27,
        },
        {
            'input': 12,
            'output': 505379714,
        },
        {
            'input': 100000,
            'output': 757631812,
        },
    ]
    solution = Solution()

    for param in params:
        n = param['input']
        result = solution.concatenatedBinary(n)
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
