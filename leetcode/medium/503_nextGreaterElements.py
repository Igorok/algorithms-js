from typing import List
import json
from collections import deque, defaultdict
import math

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(n):
            while stack and stack[-1][0] < nums[i]:
                val, id = stack.pop()
                res[id] = nums[i]

            stack.append((nums[i], i))

        if stack:
            for i in range(n):
                while stack and stack[-1][0] < nums[i]:
                    val, id = stack.pop()
                    res[id] = nums[i]

                if not stack:
                    break

        return res

def test ():
    params = [
        {
            'input': [1,2,1],
            'output': [2,-1,2],
        },
        {
            'input': [1,2,3,4,3],
            'output': [2,3,4,-1,4],
        },
    ]
    solution = Solution()

    for param in params:
        s = param['input']
        result = solution.nextGreaterElements(s)
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
