from typing import List
from json import dumps
import heapq
from collections import deque

class Solution:
    def cherryPickup_0(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = 0
        found = False

        def isInvalidLoc(y, x):
            return y == -1 or x == -1 or y == n or x == n or grid[y][x] == -1

        def dfs(y1, x1, num1, y2, x2, num2, visited):
            nonlocal res, found

            if (y1, x1) in visited and (y2, x2) in visited:
                found = True
                return

            if not (y1, x1) in visited:
                num1 += grid[y1][x1]
                visited.add((y1, x1))
            if not (y2, x2) in visited:
                visited.add((y2, x2))
                num2 += grid[y2][x2]

            res = max(res, num1 + num2)

            if y1 == n-1 and x1 == n-1:
                if y2 == 0 and x2 == 0:
                    found = True
                return
            if y2 == 0 and x2 == 0:
                return

            if not isInvalidLoc(y1 + 1, x1) and not isInvalidLoc(y2 - 1, x2):
                dfs(y1 + 1, x1, num1, y2 - 1, x2, num2, visited.copy())

            if not isInvalidLoc(y1 + 1, x1) and not isInvalidLoc(y2, x2 - 1):
                dfs(y1 + 1, x1, num1, y2, x2 - 1, num2, visited.copy())

            if not isInvalidLoc(y1, x1 + 1) and not isInvalidLoc(y2 - 1, x2):
                dfs(y1, x1+1, num1, y2 - 1, x2, num2, visited.copy())

            if not isInvalidLoc(y1, x1 + 1) and not isInvalidLoc(y2, x2 - 1):
                dfs(y1, x1+1, num1, y2, x2 - 1, num2, visited.copy())

        dfs(0,0,0,n-1,n-1,0, set())

        return res if found else 0



    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        found = False
        offset = ((1, 0), (0, 1))
        memo = [[[[-1]*n for i in range(n)] for i1 in range(n)] for i2 in range(n)]


        def isInvalidLoc(y, x):
            return y == -1 or x == -1 or y == n or x == n or grid[y][x] == -1

        def dfs(y1, x1, y2, x2):
            nonlocal found, memo, offset, n

            if isInvalidLoc(y1, x1) or isInvalidLoc(y2, x2):
                return float('-inf')

            if memo[y1][x1][y2][x2] != -1:
                return memo[y1][x1][y2][x2]

            if y1 == n-1 and x1 == n-1 and y2 == n-1 and x2 == n-1:
                found = True
                memo[y1][x1][y2][x2] = grid[y1][x1]
                return memo[y1][x1][y2][x2]

            val = 0
            if (y1 == y2 and x1 == x2):
                val = grid[y1][x1]
            else:
                val = grid[y1][x1] + grid[y2][x2]

            r = float('-inf')
            for offY1, offX1 in offset:
                i1 = y1 + offY1
                j1 = x1 + offX1
                for offY2, offX2 in offset:
                    i2 = y2 + offY2
                    j2 = x2 + offX2
                    r = max(r, dfs(i1, j1, i2, j2))

            memo[y1][x1][y2][x2] = val + r

            return memo[y1][x1][y2][x2]

        res = dfs(0, 0, 0, 0)

        return res if found else 0

'''

[ x,-1, 1, 1, 1, 1, 1, 1,-1, 1],
[ x, x, 1, 1,-1,-1, 1, 1, 1, 1],
[-1, x, 1,-1, 1, 1, 1, 1, 1, 1],
[ 1, x,-1, 1,-1, 1, 1, 1, 1, 1],
[-1, x, x, x, x, 1, 1, 1, 1, 1],
[-1,-1, x, 1, x,-1, 1, 1,-1, 1],
[ 1, 1, x, x, x, x, 1,-1, 1, 1],
[ 1, 1, 1, 1,-1, x,-1,-1, 1, 1],
[ 1,-1, 1,-1,-1, x, x,-1, 1,-1],
[-1, 1,-1, 1,-1, x, x, x, x, x]


'''



def test ():
    params = [
        {
            'input': [[0,1,-1],[1,0,-1],[1,1,1]],
            'output': 5,
        },
        {
            'input': [[1,1,-1],[1,-1,1],[-1,1,1]],
            'output': 0,
        },
        {
            'input': [
                [1,1,1],
                [1,3,1],
                [2,1,1],
            ],
            'output': 11,
        },
        {
            'input': [
                [1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1],
            ],
            'output': 24,
        },
        {
            'input': [
                [1,-1,1,1,1,1,1,1,-1,1],
                [1,1,1,1,-1,-1,1,1,1,1],
                [-1,1,1,-1,1,1,1,1,1,1],
                [1,1,-1,1,-1,1,1,1,1,1],
                [-1,1,1,1,1,1,1,1,1,1],
                [-1,-1,1,1,1,-1,1,1,-1,1],
                [1,1,1,1,1,1,1,-1,1,1],
                [1,1,1,1,-1,1,-1,-1,1,1],
                [1,-1,1,-1,-1,1,1,-1,1,-1],
                [-1,1,-1,1,-1,1,1,1,1,1]
            ],
            'output': 23,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.cherryPickup(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
