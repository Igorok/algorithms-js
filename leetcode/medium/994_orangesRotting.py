from collections import deque
from typing import List
from json import dumps

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        steps = (
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        )

        visited = set()
        fresh = set()
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh.add((i,j))
                elif grid[i][j] == 2:
                    q.appendleft((i, j, 0))

        res = 0
        while q:
            i, j, s = q.pop()
            res = max(res, s)
            for y, x in steps:
                newI = i + y
                newJ = j + x
                if newI < 0 or newJ < 0 or newI == len(grid) or newJ == len(grid[0]) or grid[newI][newJ] == 0 or (newI, newJ) in visited:
                    continue
                visited.add((newI, newJ))
                if grid[newI][newJ] == 1:
                    grid[newI][newJ] = 2
                    q.appendleft((newI, newJ, s + 1))
                    if (newI, newJ) in fresh:
                        fresh.remove((newI, newJ))
                if grid[newI][newJ] == 2:
                    q.appendleft((newI, newJ, s))

        return -1 if len(fresh) != 0 else res

def test ():
    params = [
        {
            'input': [
                [2,1,1],
                [1,1,0],
                [0,1,1]
            ],
            'output': 4,
        },
        {
            'input': [
                [2,1,1],
                [0,1,1],
                [1,0,1]
            ],
            'output': -1,
        },
        {
            'input': [
                [0,2]
            ],
            'output': 0,
        },
        {
            'input': [
                [2,1,1],
                [1,1,1],
                [0,1,2]
            ],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.orangesRotting(param['input'])

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
