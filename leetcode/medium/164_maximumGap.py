from typing import List
import json
from collections import deque, defaultdict
import heapq
from functools import lru_cache


class Solution:
    def maximumGap(self, nums: List[int]) -> int:

        return 0



def test ():
    params = [
        {
            'input': [3,6,9,1],
            'output': 3,
        },
        {
            'input': [10],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.maximumGap(nums)
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
