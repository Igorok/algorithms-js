from typing import List
import json
from collections import deque, defaultdict
from functools import cache

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        N = len(nums)

        res = 0
        memo = defaultdict(int)
        left = 0

        for right in range(N):
            memo[nums[right]] += 1

            while memo[nums[right]] > k:
                memo[nums[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res

def test ():
    params = [
        {
            'input': [[1,2,3,1,2,3,1,2], 2],
            'output': 6,
        },
        {
            'input': [[1,2,1,2,1,2,1,2], 1],
            'output': 2,
        },
        {
            'input': [[5,5,5,5,5,5,5], 4],
            'output': 4,
        },
    ]
    solution = Solution()

    for param in params:
        nums, k = param['input']
        result = solution.maxSubarrayLength(nums, k)
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
