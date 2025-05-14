from typing import List
import json
from collections import deque, defaultdict
import heapq
import math


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:

        return 0


def test ():
    params = [
        {
            'input': ["abcyy", 2, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]],
            'output': 7,
        },
        {
            'input': ["azbk", 1, [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]],
            'output': 8,
        },
    ]
    solution = Solution()

    for param in params:
        s, t, nums = param['input']
        result = solution.lengthAfterTransformations(s, t, nums)
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
