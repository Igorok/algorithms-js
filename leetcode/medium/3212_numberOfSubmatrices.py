from typing import List
from json import dumps
from collections import deque
import heapq


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        N = len(grid)
        M = len(grid[0])

        memo = []
        res = 0

        for row in range(N):
            memo.append([])
            for col in range(M):
                x = 1 if grid[row][col] == 'X' else 0
                y = 1 if grid[row][col] == 'Y' else 0

                memo[row].append([x,y])

                if row > 0:
                    memo[row][col][0] += memo[row-1][col][0]
                    memo[row][col][1] += memo[row-1][col][1]
                if col > 0:
                    memo[row][col][0] += memo[row][col-1][0]
                    memo[row][col][1] += memo[row][col-1][1]
                if row > 0 and col > 0:
                    memo[row][col][0] -= memo[row-1][col-1][0]
                    memo[row][col][1] -= memo[row-1][col-1][1]

                if memo[row][col][0] >= 1 and memo[row][col][0] == memo[row][col][1]:
                    res += 1

        memo = None

        return res


def test ():
    params = [
        {
            'input': [["X","Y","."],["Y",".","."]],
            'output': 3,
        },
        {
            'input': [["X","X"],["X","Y"]],
            'output': 0,
        },
        {
            'input': [[".","."],[".","."]],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        grid = param['input']
        result = solution.numberOfSubmatrices(grid)

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            # 'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
