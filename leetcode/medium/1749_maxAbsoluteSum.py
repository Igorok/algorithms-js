from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def maxAbsoluteSum_0(self, nums: List[int]) -> int:
        res = -1

        for i in range(len(nums)):
            s = nums[i]
            res = max(res, abs(s))
            for j in range(i+1, len(nums)):
                s += nums[j]
                res = max(res, abs(s))

        return res

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        res = -1
        maxVal = minVal = 0

        for num in nums:
            maxVal = max(maxVal + num, num)
            minVal = min(minVal + num, num)
            res = max(res, abs(minVal), maxVal)

        return res


def test ():
    params = [
        {
            'input': [1,-3,2,3,-4],
            'output': 5,
        },
        {
            'input': [2,-5,1,-4,3,-2],
            'output': 8,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.maxAbsoluteSum(param['input'])
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
