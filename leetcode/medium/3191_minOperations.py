from typing import List
import json
from collections import deque, defaultdict


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        for i in range(N):
            if nums[i] == 0:
                if i + 3 > N:
                    return -1
                res += 1
                for j in range(i, i+3):
                    nums[j] = 1 if nums[j] == 0 else 0

        return res if nums[-1] == 1 else -1



def test ():
    params = [
        {
            'input': [1,0,0,1,1,0,1,1,1],
            'output': -1,
        },
        {
            'input': [0,1,1,1,0,0],
            'output': 3,
        },
        {
            'input': [0,1,1,1],
            'output': -1,
        },
        {
            'input': [0,1,1,0,1,0,0],
            'output': -1,
        },
        {
            'input': [0,0,1,0,0],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.minOperations(nums)
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
