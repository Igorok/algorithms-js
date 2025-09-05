from typing import List
import json
from collections import deque, defaultdict
import math

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()

        def dfs(id, acc):
            if id == n:
                res.add(tuple(sorted(acc)))
                return

            acc.append(nums[id])
            dfs(id+1, acc)
            acc.pop()

            dfs(id+1, acc)

        dfs(0, [])

        return list(res)

'''

[[4,4],[4,4,1,4],[4,4,4,4],[4,1,4],[4,4,1],[4],[1,4],[4,4,4],[1],[4,4,4,1,4],[],[4,1],[4,4,4,1]]


[[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]

'''

def test ():
    params = [
        {
            'input': [4,4,4,1,4],
            'output': [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]],
        },
        {
            'input': [1,2,2],
            'output': [[],[1],[1,2],[1,2,2],[2],[2,2]],
        },
        {
            'input': [0],
            'output': [[],[0]],
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.subsetsWithDup(nums)
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
