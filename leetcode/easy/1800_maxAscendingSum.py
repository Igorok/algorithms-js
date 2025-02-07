from typing import List
import json
from collections import deque

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        s = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                s += nums[i]
            else:
                res = max(res, s)
                s = nums[i]
        res = max(res, s)

        return res


def test ():
    params = [
        {
            'input': [10,20,30,5,10,50],
            'output': 65,
        },
        {
            'input': [10,20,30,40,50],
            'output': 150,
        },
        {
            'input': [12,17,15,13,10,11,12],
            'output': 33,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.maxAscendingSum(param['input'])
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
