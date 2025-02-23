from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        min_v = max_v = 1

        for num in nums:
            if num == 0:
                min_v = max_v = 1
                res = max(res, 0)
            else:
                tmp = max_v * num
                max_v = max(tmp, min_v * num, num)
                min_v = min(tmp, min_v * num, num)
                res = max(res, max_v)

        return res

'''
-2 2 2 -2
-2,-2
-4, 2
-8, 4
-2, 16


'''


def test ():
    params = [
        {
            'input': [2,3,-2,4],
            'output': 6,
        },
        {
            'input': [-2,0,-1],
            'output': 0,
        },
        {
            'input': [-2, 2, 2, -2],
            'output': 16,
        },
        {
            'input': [2,2,-1,2,2],
            'output': 4,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.maxProduct(param['input'])
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
