from typing import List
import json
from collections import deque


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        acc = 1
        res = 0

        for right in range(n):
            if acc * nums[right] < k:
                acc *= nums[right]
                continue

            while acc * nums[right] >= k and left < right:
                length = right - left
                res += length
                acc = acc // nums[left]
                left += 1

            if nums[right] >= k:
                left = right + 1
            else:
                acc *= nums[right]

        while left < n:
            res += n - left
            left += 1


        return res



def test ():
    params = [
        {
            'input': [[2], 3],
            'output': 1,
        },
        {
            'input': [[10,5,2,6], 100],
            'output': 8,
        },
        {
            'input': [[1,2,3], 0],
            'output': 0,
        },
        {
            'input': [[10,9,10,4,3,8,3,3,6,2,10,10,9,3], 19],
            'output': 18,
        },
    ]
    solution = Solution()

    for param in params:
        nums, k = param['input']
        result = solution.numSubarrayProductLessThanK(nums, k)
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
