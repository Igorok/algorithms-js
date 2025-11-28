from typing import List
import json
from collections import deque
import heapq

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        sumOfNums = [0] * N
        sumOfNums[0] = nums[0]
        for i in range(1, N):
            sumOfNums[i] = sumOfNums[i-1] + nums[i]

        remainders = [float('-inf')] * k
        res = float('-inf')

        for i in range(k-1, N):
            r = i % k
            prevVal = 0 if i - k < 0 else sumOfNums[i-k]
            s = sumOfNums[i] - prevVal
            remainders[r] = s if s >= remainders[r] + s else remainders[r] + s

            res = max(res, remainders[r])

        return res

def test ():
    params = [
        {
            'input': [[1,2], 1],
            'output': 3,
        },
        {
            'input': [[-1,-2,-3,-4,-5], 4],
            'output': -10,
        },
        {
            'input': [[-5,1,2,-3,4], 2],
            'output': 4,
        },
    ]
    solution = Solution()

    for param in params:
        nums, k = param['input']
        result = solution.maxSubarraySum(nums, k)
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
