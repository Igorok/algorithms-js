
from typing import List
import json
from collections import Counter
from functools import cache

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)

        if k == len(nums):
            return max(nums)

        if k == 1:
            r = -1
            for v, c in cnt.items():
                if c == 1:
                    r = max(r, v)
            return r

        res = []
        if cnt[nums[0]] == 1:
            res.append(nums[0])
        if cnt[nums[-1]] == 1:
            res.append(nums[-1])

        if len(res) == 0:
            return -1

        return max(res)

def test ():
    params = [
        {
            'input': [[3,9,2,1,7], 3],
            'output': 7,
        },
        {
            'input': [[3,9,7,2,1,7], 4],
            'output': 3,
        },
        {
            'input': [[0,0], 1],
            'output': -1,
        },
        {
            'input': [[0,0], 2],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        nums, k = param['input']
        result = solution.largestInteger(nums, k)
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
