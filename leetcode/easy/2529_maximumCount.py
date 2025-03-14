from typing import List
import json
from collections import deque, defaultdict
import math

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        idNeg = -1
        idPos = -1

        for i in range(n):
            if nums[i] < 0:
                idNeg = i
            if nums[i] > 0 and idPos == -1:
                idPos = i
                break

        countNeg = 0 if idNeg == -1 else idNeg + 1
        countPos = 0 if idPos == -1 else n - idPos

        return max(countNeg, countPos)

def test ():
    params = [
        {
            'input': [-2,-1,-1,1,2,3],
            'output': 3,
        },
        {
            'input': [-3,-2,-1,0,0,1,2],
            'output': 3,
        },
        {
            'input': [5,20,66,1314],
            'output': 4,
        },
    ]
    solution = Solution()

    for param in params:
        s = param['input']
        result = solution.maximumCount(s)
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
