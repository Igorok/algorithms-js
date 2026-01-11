from typing import List
import heapq
import math
from collections import defaultdict, deque

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        M = len(nums2)

        notEmpty = float('-inf')
        memo = [[None]*M for i in range(N)]

        def dfs(id1, id2):
            nonlocal notEmpty
            if id1 == N or id2 == M:
                return 0

            if memo[id1][id2] is not None:
                return memo[id1][id2]

            product = nums1[id1] * nums2[id2]

            notEmpty = max(notEmpty, product)

            r1 = product + dfs(id1+1, id2+1)
            r2 = dfs(id1+1, id2)
            r3 = dfs(id1, id2+1)

            memo[id1][id2] = max(r1, r2, r3)
            return max(r1, r2, r3)

        res = dfs(0, 0)
        if res == 0:
            res = notEmpty

        return res


def test ():
    params = [
        {
            'input': [[2,1,-2,5], [3,0,-6]],
            'output': 18,
        },
        {
            'input': [[3,-2], [2,-6,7]],
            'output': 21,
        },
        {
            'input': [[-1,-1], [1,1]],
            'output': -1,
        },
        {
            'input': [[-5,-1,-2], [3,3,5,5]],
            'output': -3,
        },
    ]
    solution = Solution()

    for param in params:
        nums1, nums2 = param['input']
        result = solution.maxDotProduct(nums1, nums2)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
