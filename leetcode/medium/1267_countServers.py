from typing import List
from json import dumps
from collections import deque

class Solution:
    def countServers_0(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        visited = [[-1]*n for i in range(m)]
        rows = [-1]*m
        columns = [-1]*n

        def dfs (i, j):
            if visited[i][j] == 1 or grid[i][j] == 0:
                return 0

            visited[i][j] = 1
            localSum = 1

            for y in range(0, i):
                if grid[y][j] == 1:
                    if visited[y][j] == 1:
                        break
                    localSum += dfs(y, j)

            for y in range(i+1, m):
                if grid[y][j] == 1:
                    if visited[y][j] == 1:
                        break
                    localSum += dfs(y, j)

            columns[j] = 1

            for x in range(0, j):
                if grid[i][x] == 1:
                    if visited[i][x] == 1:
                        break
                    localSum += dfs(i, x)

            for x in range(j+1, n):
                if grid[i][x] == 1:
                    if visited[i][x] == 1:
                        break
                    localSum += dfs(i, x)

            return localSum

        for i in range(m):
            if rows[i] == 1:
                continue
            for j in range(n):
                if columns[j] == 1:
                    continue
                if grid[i][j] == 1:
                    if visited[i][j] == 1:
                        break
                    s = dfs(i, j)
                    s = s if s > 1 else 0
                    res += s
                    columns[j] = 1
                    rows[i] = 1
        return res


    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        rows = [0]*m
        columns = [0]*n

        for i in range(m):
            for j in range(n):
                rows[i] += grid[i][j]
                columns[j] += grid[i][j]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (rows[i] > 1 or columns[j] > 1):
                    res += 1

        return res



'''

[1,0,0,1,0],
[0,0,0,0,0],
[0,0,0,1,0]

1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0

[0,0,1,0,1],
[0,1,0,1,0],
[0,1,1,1,0],
[1,0,0,1,1],
[0,0,1,1,0]

0 1 2 3 4 2
2 0 0 1 0 1
2 0 1 0 1 0
3 0 1 1 1 0
3 1 0 0 1 1
2 0 0 1 1 0

[1,1,0,0],
[0,0,1,0],
[0,0,1,0],
[0,0,0,1]

0 1 1 2 1
2 1 1 0 0
1 0 0 1 0
1 0 0 1 0
1 0 0 0 0


'''

def test ():
    params = [
        {
            'input': [[1,0],[0,1]],
            'output': 0,
        },
        {
            'input': [[1,0],[1,1]],
            'output': 3,
        },
        {
            'input': [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]],
            'output': 4,
        },
        {
            'input': [
                [1,0,0,1,0],
                [0,0,0,0,0],
                [0,0,0,1,0]
            ],
            'output': 3,
        },
        {
            'input': [
                [0,0,1,0,1],
                [0,1,0,1,0],
                [0,1,1,1,0],
                [1,0,0,1,1],
                [0,0,1,1,0]
            ],
            'output': 12,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.countServers(param['input'])
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
