from typing import List
import json
from collections import deque, defaultdict
from functools import lru_cache


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:

        def dfs(height, width):
            if height == n or width == m:
                return float('inf')

            res = float('inf')



            return res


        return dfs(1, 1)

'''
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
- - - - - - - - - - -
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0


'''


def test ():
    params = [
        {
            'input': [2, 3],
            'output': 3,
        },
        {
            'input': [5, 8],
            'output': 5,
        },
        {
            'input': [11, 13],
            'output': 6,
        },
    ]
    solution = Solution()

    for param in params:
        n, m = param['input']
        result = solution.tilingRectangle(n, m)
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
