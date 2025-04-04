from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def maximumTripletValue_0(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    r = (nums[i] - nums[j]) * nums[k]
                    res = max(res, r)

        return res

    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        postfix = [0] * n
        postfix[n-1] = nums[-1]
        for i in range(n-2, -1, -1):
            postfix[i] = max(postfix[i+1], nums[i])

        prev = nums[0]
        for i in range(1, n-1):
            r = (prev - nums[i]) * postfix[i+1]
            res = max(res, r)
            prev = max(prev, nums[i])

        return res

'''
12,6,1,2,7
12  7  7  7  7
12 12 12 12 12


'''

def test ():
    params = [
        {
            'input': [1000000,1,1000000],
            'output': 999999000000,
        },
        {
            'input': [12,6,1,2,7],
            'output': 77,
        },
        {
            'input': [1,10,3,4,19],
            'output': 133,
        },
        {
            'input': [1,2,3],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.maximumTripletValue(param['input'])
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
