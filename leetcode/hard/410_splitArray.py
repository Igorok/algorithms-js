import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq
import math

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        prefixSum = [0]*N
        prefixSum[0] = nums[0]
        maxVal = nums[0]
        for i in range(1, N):
            prefixSum[i] = prefixSum[i-1] + nums[i]
            maxVal = max(maxVal, nums[i])

        minSum = maxVal
        maxSum = prefixSum[-1]
        res = prefixSum[-1]

        def isOk(value):
            nonlocal N, nums, k
            cnt = 1
            local = nums[0]
            for i in range(1, N):
                if local + nums[i] > value:
                    cnt += 1
                    local = nums[i]
                else:
                    local += nums[i]
            if local > value:
                cnt += 1
            return cnt <= k



        while minSum <= maxSum:
            middle = (minSum + maxSum) // 2

            if isOk(middle):
                res = middle
                maxSum = middle - 1
            else:
                minSum = middle + 1

        return res

def test ():
    params = [
        # {
        #     'input': [[7,2,5,10,8], 2],
        #     'output': 18,
        # },
        # {
        #     'input': [[1,2,3,4,5], 2],
        #     'output': 9,
        # },
        {
            'input': [[10,2,3], 2],
            'output': 10,
        },
    ]
    solution = Solution()

    for param in params:
        nums, k = param['input']
        result = solution.splitArray(nums, k)
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
