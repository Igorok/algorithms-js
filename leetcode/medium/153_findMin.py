from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        if nums[0] < nums[-1]:
            return nums[0]

        start = 0
        end = n - 1

        while start <= end:
            m = (start + end) // 2

            if m-1 != -1 and nums[m] < nums[m-1]:
                return nums[m]
            if m+1 != n and nums[m+1] < nums[m]:
                return nums[m+1]

            if nums[m] > nums[0]:
                start += 1
            else:
                end -= 1

        return 0

def test ():
    params = [
        {
            'input': [3,4,5,1,2],
            'output': 1,
        },
        {
            'input': [4,5,6,7,0,1,2],
            'output': 0,
        },
        {
            'input': [11,13,15,17],
            'output': 11,
        },
        {
            'input': [3,1,2],
            'output': 1,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.findMin(param['input'])
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
