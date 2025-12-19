from typing import List
import json
from collections import deque, defaultdict, Counter
import heapq
import math
from functools import cache
from functools import cmp_to_key


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        N = len(prices)
        left = 0
        res = 0

        for right in range(1, N):
            res += right - left
            if prices[right-1] - prices[right] != 1:
                left = right

        res += N - left

        return res

'''
[3,2,1,4]
3,2,1,4
1 2 3 1

'''


def test ():
    params = [
        {
            'input': [3,2,1,4],
            'output': 7,
        },
        {
            'input': [8,6,7,7],
            'output': 4,
        },
        {
            'input': [1],
            'output': 1,
        },
    ]
    solution = Solution()

    for param in params:
        prices = param['input']
        result = solution.getDescentPeriods(prices)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            # msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
