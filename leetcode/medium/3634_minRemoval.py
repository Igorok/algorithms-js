from typing import List
from collections import deque
from functools import cache
import re

class Solution_0:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)

        def isOk(size):
            nonlocal k, nums

            for i in range(N-size+1):
                v1 = nums[i]
                v2 = nums[i+size-1]

                if v1*k >= v2:
                    return True

            return False

        start = 0
        end = N
        size = 0

        while start <= end:
            middle = (start + end) // 2
            if isOk(middle):
                size = middle
                start = middle + 1
            else:
                end = middle -1



        return N - size



class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)

        size = 0
        left = 0

        for right in range(N):
            while nums[left]*k < nums[right]:
                left += 1
            size = max(size, right-left + 1)

        return N - size

'''

1, 2, 3, 4, 5, 5, 7, 7, 7, 20, ,40, 41, 42, 45, 46


1 2 5
'''


def test ():
    params = [
        {
            'input': [[2,1,5], 2],
            'output': 1,
        },
        {
            'input': [[1,6,2,9], 3],
            'output': 2,
        },
        {
            'input': [[4,6], 2],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        nums, k = param['input']
        result = solution.minRemoval(nums, k)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            # 'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
