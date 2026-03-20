from typing import List
from json import dumps
from collections import deque
import heapq

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        N = len(grid)
        M = len(grid[0])
        memo = [[0]*M for i in range(N)]
        res = 0

        for row in range(N):
            for col in range(M):
                top = 0 if row == 0 else memo[row-1][col]
                left = 0 if col == 0 else memo[row][col-1]
                diag = 0 if row == 0 or col == 0 else memo[row-1][col-1]

                memo[row][col] = grid[row][col] + top + left - diag
                if memo[row][col] <= k:
                    res += 1
                else:
                    break

        return res


def test ():
    params = [
        {
            'input': [[[7,6,3],[6,6,1]], 18],
            'output': 4,
        },
        {
            'input': [[[7,2,9],[1,5,0],[2,6,6]], 20],
            'output': 6,
        },
    ]
    solution = Solution()

    for param in params:
        grid, k = param['input']
        result = solution.countSubmatrices(grid, k)

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            # 'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
