from typing import List
from json import dumps
from collections import deque, defaultdict


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        prevLeft = -1
        prevRight = -1
        left = 0
        for right in range(1, n):
            if nums[right-1] < nums[right]:
                length = right - left + 1
                prevLength = 0 if (prevRight == -1 or left - prevRight != 1) else prevRight - prevLeft + 1
                res = max(res, length // 2, min(length, prevLength))
            else:
                prevLeft = left
                prevRight = right - 1
                left = right

        length = n - left
        prevLength = 0 if (prevRight == -1 or left - prevRight != 1) else prevRight - prevLeft + 1
        res = max(res, length // 2, min(length, prevLength))

        return res


def test ():
    params = [
        {
            'input': [19,5],
            'output': 1,
        },
        {
            'input': [2,5,7,8,9,2,3,4,3,1],
            'output': 3,
        },
        {
            'input': [1,2,3,4,4,4,4,5,6,7],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.maxIncreasingSubarrays(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
