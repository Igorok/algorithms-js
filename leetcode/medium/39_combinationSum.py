from typing import List
import json
from collections import deque

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        nums = sorted(candidates)

        def rec(id, arr, s):
            nonlocal res, nums

            if s == target:
                res.append(arr.copy())
                return

            if s > target:
                return

            if id == len(nums):
                return

            s += nums[id]
            arr.append(nums[id])
            rec(id, arr, s)
            s -= nums[id]
            arr.pop()

            id += 1
            rec(id, arr, s)


        rec(0, [], 0)

        return res


def test ():
    params = [
        {
            'input': [[2,3,6,7], 7],
            'output': [[2,2,3],[7]],
        },
        {
            'input': [[2,3,5], 8],
            'output': [[2,2,2,2],[2,3,3],[3,5]],
        },
    ]
    solution = Solution()

    for param in params:
        candidates, target = param['input']
        result = solution.combinationSum(candidates, target)
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
