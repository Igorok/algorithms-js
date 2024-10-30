from collections import deque
from typing import List
from json import dumps

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        steps = [
            (-1, 1),
            (0, 1),
            (1, 1)
        ]

        track = [[0]*len(grid[0]) for _ in range(len(grid))]

        res = 0
        def movement(i, j, s):
            for y, x in steps:
                nonlocal res

                res = max(res, s)
                newI = i + y
                newJ = j + x
                if newI < 0 or newJ < 0 or newI == len(grid) or newJ == len(grid[0]) or grid[newI][newJ] <= grid[i][j] or track[newI][newJ] >= s + 1:
                    continue
                track[newI][newJ] = s + 1
                movement(newI, newJ, s + 1)

        for i in range(len(grid)):
            movement(i, 0, 0)

        return res

def test ():
    params = [
        {
            'input': [
                [2,4,3,5],
                [5,4,9,3],
                [3,4,2,11],
                [10,9,13,15]
            ],
            'output': 3,
        },
        {
            'input': [
                [3,2,4],
                [2,1,9],
                [1,1,7]
            ],
            'output': 0,
        },
        {
            'input': [
                [1,1,1,1,1,1],
                [2,2,2,2,2,2],
                [3,3,3,3,3,3],
                [4,4,4,4,4,4],
                [5,5,5,5,5,5],
                [6,6,6,6,6,6],
            ],
            'output': 5,
        },
        {
            'input': [
                [1,1,1,1,9,10],
                [1,1,1,1,9,1],
                [2,2,2,8,2,2],
                [3,3,7,3,3,3],
                [4,6,4,4,4,4],
                [5,5,5,5,5,5],
                [6,6,6,6,6,6],
            ],
            'output': 5,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.maxMoves(param['input'])

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
