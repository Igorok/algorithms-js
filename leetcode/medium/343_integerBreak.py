import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq
import math

class Solution:
    def integerBreak(self, n: int) -> int:
        cache = {}

        def getMaxProduct(num):
            if num == 1:
                return 1

            if num in cache:
                return cache[num]

            res = float('-inf') if num == n else num

            for i in range(1, num):
                left = i
                right = num - i
                r1 = getMaxProduct(left)
                r2 = getMaxProduct(right)

                res = max(res, r1 * r2)

            cache[num] = res

            return res

        return getMaxProduct(n)

'''
10
3, 7



'''

def test ():
    params = [
        {
            'input': 2,
            'output': 1,
        },
        {
            'input': 3,
            'output': 2,
        },
        {
            'input': 10,
            'output': 36,
        },
        {
            'input': 57,
            'output': 1162261467,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.integerBreak(param['input'])
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
