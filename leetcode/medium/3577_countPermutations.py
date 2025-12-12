from typing import List
import json
from collections import deque, defaultdict, Counter
import heapq
import math
from functools import cache


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        N = len(complexity)
        MOD = 7 + 10**9
        res = 1

        for i in range(1, N):
            if complexity[i] <= complexity[0]:
                return 0

            res = (res * i) % MOD

        return res

'''

1 2 3

x 2
x x 3

---

2,68,61

1 1 1

---

1 3 3 3 2 3
5*4*3*2*1

'''


def test ():
    params = [
        {
            'input': [1,2,3],
            'output': 2,
        },
        {
            'input': [3,3,3,4,4,4],
            'output': 0,
        },
        {
            'input': [2,68,61],
            'output': 2,
        },
        {
            'input': [1, 3, 3, 3, 2, 3],
            'output': 120,
        },
    ]
    solution = Solution()

    for param in params:
        complexity = param['input']
        result = solution.countPermutations(complexity)
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
