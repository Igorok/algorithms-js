from typing import List
import json
from collections import deque, defaultdict
from functools import cache


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)

        @cache
        def rec(step, start, end):
            if step >= N:
                return [0, 0]

            r1 = rec(step+1, start+1, end)
            r1 = (r1[1] + piles[start], r1[0])

            r2 = rec(step+1, start, end-1)
            r2 = (r2[1] + piles[end], r2[0])

            if r1[1] <= r2[1]:
                return r1
            else:
                return r2

        r = rec(0, 0, N - 1)

        return r[0] > r[1]


def test ():
    params = [
        {
            'input': [5,3,4,5],
            'output': True,
        },
        {
            'input': [3,7,2,3],
            'output': True,
        },
    ]
    solution = Solution()

    for param in params:
        piles = param['input']
        result = solution.stoneGame(piles)
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
