from inspect import getgeneratorlocals
from typing import List
import json
from collections import deque, defaultdict
import heapq

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        leftSum = [0] * n
        rightSum = [0] * n

        rightSum[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            rightSum[i] = rightSum[i+1] + nums[i]

        res = 0
        leftSum[0] = nums[0]
        for i in range(0, n):
            left = 0 if i == 0 else leftSum[i-1]
            leftSum[i] = left + nums[i]
            if nums[i] == 0:
                diff = abs(leftSum[i] - rightSum[i])
                if diff == 0:
                    res += 2
                elif diff == 1:
                    res += 1

        return res

'''

16,13,10,0,0,0,10,6,7,8,7
39 38




'''

def test ():
    params = [
        {
            'input': [0],
            'output': 2,
        },
        {
            'input': [16,13,10,0,0,0,10,6,7,8,7],
            'output': 3,
        },
        {
            'input': [1,0,2,0,3],
            'output': 2,
        },
        {
            'input': [2,3,4,0,4,1,0],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.countValidSelections(nums)
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
