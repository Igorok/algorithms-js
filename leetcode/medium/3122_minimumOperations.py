from typing import List
import json
from collections import deque, defaultdict
import heapq
import math
from functools import cache

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])

        data = [[0] * 10 for i in range(width)]

        for row in range(height):
            for col in range(width):
                num = grid[row][col]
                data[col][num] += 1

        for id in range(width):
            arr = sorted(
                [(i, data[id][i]) for i in range(10)],
                key = lambda x: -x[1]
            )
            data[id] = arr

        @cache
        def dfs(id, prev):
            if id == width:
                return 0

            res = 0
            first = 0
            second = 1

            if data[id][first][0] == prev:
                first += 1
                second += 1

            if data[id][second][0] == prev:
                second += 1

            cnt = data[id][first][1]
            r1 = height - cnt
            r1 += dfs(id+1, data[id][first][0])

            cnt = data[id][second][1]
            r2 = height - cnt
            r2 += dfs(id+1, data[id][second][0])

            res = min(r1, r2)

            return res

        return dfs(0, -1)

'''
0 2 3 6
1 2 2 0
2 2 1 0
- 0 1 2 3 4 5

0 3 2 0
1 2 2 6
2 1 2 0
- 0 1 2 3 4 5

'''

def test ():
    params = [
        {
            'input': [[1,0,2],[1,0,2]],
            'output': 0,
        },
        {
            'input': [[1,1,1],[0,0,0]],
            'output': 3,
        },
        {
            'input': [[1],[2],[3]],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        grid = param['input']
        result = solution.minimumOperations(grid)
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
