from typing import List
import json
from collections import deque

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        shifts = (1,0,-1)
        memo = [[[-1]*m for i in range(m)] for i1 in range(n)]
        res = 0

        def isInvalidLoc(y, x1, x2):
            return y == n or y == -1 or x1 == m or x1 == -1 or x2 == m or x2 == -1

        def dfs(y, x1, x2):
            nonlocal memo, res

            if isInvalidLoc(y, x1, x2):
                return float('-inf')

            if memo[y][x1][x2] != -1:
                return memo[y][x1][x2]

            val = grid[y][x1] + grid[y][x2] if x1 != x2 else grid[y][x1]

            if y == n - 1:
                return val

            r = float('-inf')
            y1 = y + 1
            for shift in shifts:
                newX1 = x1 + shift
                for shift1 in shifts:
                    newX2 = x2 + shift1
                    r = max(r, dfs(y1, newX1, newX2))

            memo[y][x1][x2] = val + r

            return memo[y][x1][x2]

        return dfs(0, 0, m-1)

def test ():
    params = [
        {
            'input': [[3,1,1],[2,5,1],[1,5,5],[2,1,1]],
            'output': 24,
        },
        {
            'input': [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]],
            'output': 28,
        },
        {
            'input': [[8,8,10,9,1,7],[8,8,1,8,4,7],[8,6,10,3,7,7],[3,0,9,3,2,7],[6,8,9,4,2,5],[1,1,5,8,8,1],[5,6,5,2,9,9],[4,4,6,2,5,4],[4,4,5,3,1,6],[9,2,2,1,9,3]],
            'output': 146,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.cherryPickup(param['input'])
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
