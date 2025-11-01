from inspect import getgeneratorlocals
from typing import List
import json
from collections import deque, defaultdict
import heapq

class Solution_0:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        shifts = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def isValidCell(row, col):
            return row > -1 and row < n and col > -1 and col < n

        def getDist(row1, col1, row2, col2):
            return abs(row1 - row2) + abs(col1 - col2)

        def getClosest(row, col):
            gridQueue = deque()
            gridQueue.append((row, col))
            visited = set((row, col))

            while gridQueue:
                r, c = gridQueue.popleft()
                if grid[r][c] == 1:
                    return getDist(row, col, r, c)

                for sR, sC in shifts:
                    nR = r + sR
                    nC = c + sC
                    if isValidCell(nR, nC) and not (nR, nC) in visited:
                        visited.add((nR, nC))
                        gridQueue.append((nR, nC))

            return float('-inf')


        res = float('-inf')
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    d = getClosest(row, col)
                    res = max(res, d)


        return -1 if res == float('-inf') else res



class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        shifts = ((-1, 0), (1, 0), (0, -1), (0, 1))

        memo = [[float('inf')] * n for i in range(n)]

        def isValidCell(row, col):
            return row > -1 and row < n and col > -1 and col < n and grid[row][col] == 0

        def getDist(row1, col1, row2, col2):
            return abs(row1 - row2) + abs(col1 - col2)

        def getClosest(row, col):
            def dfs(r, c):
                for sR, sC in shifts:
                    nR = r + sR
                    nC = c + sC
                    if isValidCell(nR, nC):
                        dist = getDist(row, col, nR, nC)
                        if dist < memo[nR][nC]:
                            memo[nR][nC] = dist
                            dfs(nR, nC)
            dfs(row, col)

        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    getClosest(row, col)

        res = float('-inf')
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0 and memo[row][col] != float('inf'):
                    res = max(res, memo[row][col])


        return -1 if res == float('-inf') else res

'''

1, 0, 0, 0, 1
1, 0, 0, 0, 1
1, 0, 1, 0, 1
1, 0, 0, 0, 1
1, 0, 0, 0, 1

'''

def test ():
    params = [
        {
            'input': [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
            'output': -1,
        },
        {
            'input': [[1,0,1],[0,0,0],[1,0,1]],
            'output': 2,
        },
        {
            'input': [[1,0,0],[0,0,0],[0,0,0]],
            'output': 4,
        },
    ]
    solution = Solution()

    for param in params:
        grid = param['input']
        result = solution.maxDistance(grid)
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
