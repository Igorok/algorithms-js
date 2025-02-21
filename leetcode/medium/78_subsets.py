from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def rec(arr, id):
            nonlocal res, nums

            if id == len(nums):
                res.append(arr.copy())
                return

            b = arr.copy()
            b.append(nums[id])
            rec(b, id + 1)

            a = arr.copy()
            rec(a, id + 1)

        rec([], 0)

        return res


def test ():
    params = [
        {
            'input': [1,2,3],
            'output': [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]],
        },
        {
            'input': [0],
            'output': [[],[0]],
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.subsets(nums)
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
