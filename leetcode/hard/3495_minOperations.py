from typing import List
from json import dumps
import heapq
from collections import deque
import math


class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def getOperations(num):
            sumOfOp = 0
            start = 1
            shift = 0

            while start <= num:
                shift += 1
                prev = start
                start = start << 2
                curr = min(start - 1, num)
                count = curr - prev + 1

                sumOfOp += count * shift

            return sumOfOp

        res = 0

        for [s, e] in queries:
            opS = getOperations(s-1)
            opE = getOperations(e)

            res += math.ceil((opE - opS) / 2)

        return res



'''

000001
000100

[[14,18]]
13
12 = 3*1 + 10*2 = 23; 23 / 2 = 12
18
18 = 3*1 + 12*2 + 3*3 = 36; 36 / 2 = 18;



'''


def test ():
    params = [
        {
            'input': [[14,18]],
            'output': 7,
        },
        {
            'input': [[1,8]],
            'output': 7,
        },
        {
            'input': [[1,2],[2,4]],
            'output': 3,
        },
        {
            'input': [[2,6]],
            'output': 4,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.minOperations(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
