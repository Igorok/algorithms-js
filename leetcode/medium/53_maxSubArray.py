import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        localSum = nums[0]
        globalSum = nums[0]

        for i in range(1, len(nums)):
            localSum = max(localSum + nums[i], nums[i])
            globalSum = max(globalSum, localSum)

        return globalSum

'''

-2,1,-3,4,-1,2,1,-5,4

'''

def test ():
    params = [
        {
            'input': [-2,1,-3,4,-1,2,1,-5,4],
            'output': 6,
        },
        {
            'input': [1],
            'output': 1,
        },
        {
            'input': [5,4,-1,7,8],
            'output': 23,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.maxSubArray(param['input'])
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
