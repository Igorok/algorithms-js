from collections import deque
from typing import List
from json import dumps

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque()
        visited = set()

        cases = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]

        start = (entrance[0], entrance[1], 0)
        visited.add((entrance[0], entrance[1]))
        q.append(start)
        while q:
            i, j, steps = q.pop()
            if (i == 0 or j == 0 or i == len(maze) - 1 or j == len(maze[0]) - 1) and not (entrance[0] == i and entrance[1] == j):
                return steps

            for y, x in cases:
                newI = i + y
                newJ = j + x
                if newI < 0 or newJ < 0 or newI == len(maze) or newJ == len(maze[0]) or maze[newI][newJ] == '+' or (newI, newJ) in visited:
                    continue
                q.appendleft((newI, newJ, steps + 1))
                visited.add((newI, newJ))
        return -1

def test ():
    params = [
        {
            'input': [
                [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]],
                [1,2]
            ],
            'output': 1,
        },
        {
            'input': [
                [["+","+","+"],[".",".","."],["+","+","+"]],
                [1,0]
            ],
            'output': 2,
        },
        {
            'input': [
                [[".","+"]], [0,0],
            ],
            'output': -1,
        },
    ]
    solution = Solution()

    for param in params:
        maze, entrance = param['input']
        result = solution.nearestExit(maze, entrance)

        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
