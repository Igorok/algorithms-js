from typing import List
import json
from collections import deque, defaultdict
import heapq
import math
from functools import cache


class Solution_0:
    def isValid(self, row, col):
        return row > -1 and row < self.n and col > -1 and col < self.m

    def dfs(self, row, col, dir, turn):
        if ((row, col, dir, turn) in self.memo):
            return self.memo[(row, col, dir, turn)]

        val = self.grid[row][col]
        res = 0

        dirs = [dir] if turn == 1 else [dir, self.availableDir[dir]]

        for d in dirs:
            newRow = row + self.directions[d][0]
            newCol = col + self.directions[d][1]

            if not self.isValid(newRow, newCol) or self.grid[newRow][newCol] != self.availableVal[val]:
                continue

            t = turn + 1 if dir != d else turn
            r = self.dfs(newRow, newCol, d, t)
            res = max(res, r)

        self.memo[(row, col, dir, turn)] = res + 1

        return res + 1

    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.n = len(grid)
        self.m = len(grid[0])
        self.directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))
        self.availableDir = (1, 3, 0, 2)
        self.availableVal = { 2: 0, 0: 2 }
        self.memo = {}

        res = 0
        for row in range(self.n):
            for col in range(self.m):
                if self.grid[row][col] != 1:
                    continue

                res = max(res, 1)

                for d in range(4):
                    newRow = row + self.directions[d][0]
                    newCol = col + self.directions[d][1]

                    if not self.isValid(newRow, newCol) or grid[newRow][newCol] != 2:
                        continue

                    r = self.dfs(newRow, newCol, d, 0) + 1
                    res = max(res, r)

        return res


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        grid = grid
        n = len(grid)
        m = len(grid[0])
        directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))
        availableDir = (1, 3, 0, 2)
        availableVal = { 2: 0, 0: 2 }
        # memo = {}
        memo = [-1]*n*m*8

        def isValid(row, col):
            return row > -1 and row < n and col > -1 and col < m

        def dfs(row, col, dir, turn):
            # if ((row, col, dir, turn) in memo):
            #     return memo[(row, col, dir, turn)]

            key = row * m * 8 + col * 8 + dir*2 + turn
            if memo[key] != -1:
                return memo[key]

            val = grid[row][col]
            res = 0

            dirs = [dir] if turn == 1 else [dir, availableDir[dir]]

            for d in dirs:
                newRow = row + directions[d][0]
                newCol = col + directions[d][1]

                if not isValid(newRow, newCol) or grid[newRow][newCol] != availableVal[val]:
                    continue

                t = turn + 1 if dir != d else turn
                r = dfs(newRow, newCol, d, t)
                res = max(res, r)

            # memo[(row, col, dir, turn)] = res + 1
            memo[key] = res + 1

            return res + 1

        res = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] != 1:
                    continue

                res = max(res, 1)

                for d in range(4):
                    newRow = row + directions[d][0]
                    newCol = col + directions[d][1]

                    if not isValid(newRow, newCol) or grid[newRow][newCol] != 2:
                        continue

                    r = dfs(newRow, newCol, d, 0) + 1
                    res = max(res, r)

        return res

def test ():
    params = [
        {
            'input': [[1,0,1,0,0,0,1,2,2,1,1,1,0,2,2],[0,1,2,1,2,2,0,2,1,1,1,0,0,1,2],[1,2,1,1,2,2,0,1,1,1,1,2,0,1,0],[2,0,0,1,0,1,2,2,2,2,2,2,1,0,2],[0,2,0,0,0,0,0,1,1,0,1,0,1,2,1]],
            'output': 5,
        },
        {
            'input': [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]],
            'output': 5,
        },
        {
            'input': [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]],
            'output': 4,
        },
        {
            'input': [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]],
            'output': 5,
        },
        {
            'input': [[1]],
            'output': 1,
        },
    ]
    solution = Solution()

    for param in params:
        grid = param['input']
        result = solution.lenOfVDiagonal(grid)
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
