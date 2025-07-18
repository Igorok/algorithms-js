from typing import List
from json import dumps
import heapq
from collections import deque

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        required = sorted([(nums[i], i) for i in range(n)])[n-k:]
        required.sort(key=lambda x: x[1])

        return [r[0] for r in required]


def test ():
    params = [
        {
            'input': [[2,1,3,3], 2],
            'output': [3,3],
        },
        {
            'input': [[-1,-2,3,4], 3],
            'output': [-1,3,4],
        },
        {
            'input': [[3,4,3,3], 2],
            'output': [3,4],
        },
    ]
    solution = Solution()

    for param in params:
        nums, k = param['input']

        result = solution.maxSubsequence(nums, k)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
