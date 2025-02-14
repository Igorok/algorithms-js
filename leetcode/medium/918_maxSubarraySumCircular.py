import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq

class Solution:
    def maxSubarraySumCircular_0(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        total = nums[0]
        localMax = nums[0]
        globalMax = nums[0]

        localMin = nums[0]
        globalMin = nums[0]

        startMax = nums[0]
        endMax = float('-inf')
        start = 0

        for i in range(1, n):
            total += nums[i]
            localMin = min(localMin + nums[i], nums[i])
            globalMin = min(localMin, globalMin)

            if nums[i] >= localMax + nums[i]:
                localMax = nums[i]
                if start == 0:
                    startMax = max(startMax, startMax + nums[i])
                start = i
            else:
                localMax = localMax + nums[i]
                if start == 0:
                    startMax = max(startMax, localMax)

            if i == n-1 and start != 0:
                endMax = localMax

            globalMax = max(globalMax, localMax)

        sideMax = total - globalMin if start == 0 and globalMin < 0 else startMax + endMax

        return max(globalMax, sideMax)



    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        total = nums[0]
        localMax = nums[0]
        globalMax = nums[0]

        localMin = nums[0]
        globalMin = nums[0]


        for i in range(1, n):
            total += nums[i]
            localMin = min(localMin + nums[i], nums[i])
            globalMin = min(localMin, globalMin)

            localMax = max(localMax + nums[i], nums[i])
            globalMax = max(globalMax, localMax)

        if globalMax < 0:
            return globalMax

        return max(globalMax, total - globalMin)

'''

1,2,3,-1,-1,3,3,3,-1,-1,1,2,3
4+4+9=17

2,2,2,-5,-5,5,5,-5,-5,2,2,2
6,10,6 = 22
6 -10 10 -10 6 = 4

2,2,2,-10,10,-10,10,-10,10,-10,2,2,2

5,5,-10,-10,-10

'''


def test ():
    params = [
        {
            'input': [3,-1,2,-1],
            'output': 4,
        },
        {
            'input': [1,-2,3,-2],
            'output': 3,
        },
        {
            'input': [5,-3,5],
            'output': 10,
        },
        {
            'input': [-3,-2,-3],
            'output': -2,
        },
        {
            'input': [1,2,3,-1,-1,3,3,3,-1,-1,1,2,3],
            'output': 19,
        },
        {
            'input': [2,2,2,-5,-5,5,5,-5,-5,2,2,2],
            'output': 12,
        },
        {
            'input': [2,2,2,-10,10,-10,10,-10,10,-10,2,2,2],
            'output': 12,
        },
        {
            'input': [5,5,-10,-10,-10],
            'output': 10,
        },
        {
            'input': [-2],
            'output': -2,
        },
        {
            'input': [-2,4,-5,4,-5,9,4],
            'output': 15,
        },
        {
            'input': [1,-6,-7,4],
            'output': 5,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.maxSubarraySumCircular(param['input'])
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
