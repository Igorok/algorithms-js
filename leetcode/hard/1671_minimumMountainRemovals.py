from collections import deque
from typing import List
from json import dumps

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        incr = [1]*len(nums)
        decr = [1]*len(nums)

        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    incr[i] = max(incr[i], incr[j] + 1)

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    decr[i] = max(decr[i], decr[j] + 1)


        n = len(nums)
        res = n
        for i in range(len(nums)):
            if incr[i] == 1 or decr[i] == 1:
                continue
            res = min(res, n - (incr[i] + decr[i] - 1))

        print(
            'incr', incr,
            'decr', decr,
        )


        return res

def test ():
    params = [
        {
            'input': [1,3,1],
            'output': 0,
        },
        {
            'input': [2,1,1,5,6,2,3,1],
            'output': 3,
        },
        {
            'input': [9,8,1,7,6,5,4,3,2,1],
            'output': 2,
        },
        {
            'input': [100,92,89,77,74,66,64,66,64],
            'output': 6,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.minimumMountainRemovals(param['input'])

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
