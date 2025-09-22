from typing import List
import json
from collections import deque, defaultdict


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rowSky = [-1]*n
        colSky = [-1]*n

        for row in range(n):
            for col in range(n):
                rowSky[row] = max(grid[row][col], rowSky[row])
                colSky[col] = max(grid[row][col], colSky[col])

        res = 0

        for row in range(n):
            for col in range(n):
                maxHeight = min(rowSky[row], colSky[col])
                res += maxHeight - grid[row][col]

        return res

'''
[
    [3,0,8,4],
    [2,4,5,7],
    [9,2,6,3],
    [0,3,1,0]
]

'''



def test ():
    params = [
        {
            'input': [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]],
            'output': 35,
        },
        {
            'input': [[0,0,0],[0,0,0],[0,0,0]],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.maxIncreaseKeepingSkyline(param['input'])
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
