from typing import List
import json
from collections import deque

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        def isInvalid(i, increase):
            if increase:
                return nums[i-1] >= nums[i]
            return nums[i-1] <= nums[i]

        def getLength(increase):
            r = 1
            left = 0
            for right in range(1, n):
                if isInvalid(right, increase):
                    r = max(r, right - left) # right - 1 + 1
                    left = right
                if right == n-1:
                    r = max(r, n - left)
                    left = right
            return r

        return max(getLength(True), getLength(False))


def test ():
    params = [
        {
            'input': [1,4,3,3,2],
            'output': 2,
        },
        {
            'input': [3,3,3,3],
            'output': 1,
        },
        {
            'input': [3,2,1],
            'output': 3,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.longestMonotonicSubarray(param['input'])
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
