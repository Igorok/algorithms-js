from typing import List
import json
from collections import deque

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        offset = ((1, 0),(-1, 0),(0, 1),(0, -1))
        sizes = {}

        def isInvalidLoc(y, x):
            return y == -1 or x == -1 or y == n or x == n

        def getSizeOfMarkedIsland(y, x, label):
            if isInvalidLoc(y, x) or grid[y][x] != 1:
                return 0

            grid[y][x] = label
            res = 0
            for offY, offX in offset:
                i = y + offY
                j = x + offX
                res += getSizeOfMarkedIsland(i, j, label)

            return 1 + res

        def getMergedSize(y, x):
            visited = set()
            res = 0
            for offY, offX in offset:
                i = y + offY
                j = x + offX
                if isInvalidLoc(i, j) or grid[i][j] == 0 or grid[i][j] in visited:
                    continue
                visited.add(grid[i][j])
                res += sizes[grid[i][j]]

            return 0 if res == 0 else res + 1

        label = 2
        for i in range(n):
            for j in range(n):
                if isInvalidLoc(i, j) or grid[i][j] != 1:
                    continue
                else:
                    sizes[label] = getSizeOfMarkedIsland(i, j, label)
                    label += 1

        res = 0
        if sizes:
            res = max(sizes.values())

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    r = getMergedSize(i, j)
                    res = max(res, r)

        return res

'''
[1,0],
[0,1]


'''


def test ():
    params = [
        {
            'input': [[1,0],[0,1]],
            'output': 3,
        },
        {
            'input': [[1,1],[1,0]],
            'output': 4,
        },
        {
            'input': [[1,1],[1,1]],
            'output': 4,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.largestIsland(param['input'])
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
