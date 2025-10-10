from typing import List
from json import dumps
from collections import defaultdict, deque
import heapq

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        cache = {}

        def rec(start):
            if start in cache:
                return cache[start]

            if start == n:
                return 0

            end = min(start + k, n)
            res = 0
            val = -1

            for i in range(start, end):
                val = max(val, arr[i])
                r = (i - start + 1) * val
                r += rec(i + 1)

                res = max(res, r)

            cache[start] = res

            return res

        return rec(0)


def test ():
    params = [
        {
            'input': [[1,15,7,9,2,5,10], 3],
            'output': 84,
        },
        {
            'input': [[1,4,1,5,7,3,6,1,9,9,3], 4],
            'output': 83,
        },
        {
            'input': [[1], 1],
            'output': 1,
        },
    ]
    solution = Solution()

    for param in params:
        arr, k = param['input']
        result = solution.maxSumAfterPartitioning(arr, k)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
