from typing import List
import json
from collections import deque

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[-1]*m for i in range(n)]

        def dfs(y, x):
            offset = ((1, 0), (-1, 0), (0, 1), (0, -1))

            visited[y][x] = 1
            val = grid[y][x]

            for moveY, moveX in offset:
                i = moveY + y
                j = moveX + x

                if i < 0 or j < 0 or i == n or j == m or visited[i][j] == 1 or grid[i][j] == 0:
                    continue

                val += dfs(i, j)

            return val

        res = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0 and visited[i][j] == -1:
                    res = max(res, dfs(i, j))

        return res


def test ():
    params = [
        {
            'input': [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]],
            'output': 7,
        },
        {
            'input': [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]],
            'output': 1,
        },
        {
            'input': [[0,0]],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.findMaxFish(param['input'])
        print(
            'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR',
            '\n input', param['input'],
            '\n output', param['output'],
            '\n result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
