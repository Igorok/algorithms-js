from typing import List
from json import dumps
from collections import deque

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = [[10e4]*n for i in range(m)]
        memo[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i - 1 > -1:
                    memo[i][j] = min(memo[i][j], grid[i][j] + memo[i-1][j])
                if j - 1 > -1:
                    memo[i][j] = min(memo[i][j], grid[i][j] + memo[i][j-1])

        return memo[-1][-1]

def test ():
    params = [
        {
            'input': [[1,3,1],[1,5,1],[4,2,1]],
            'output': 7,
        },
        {
            'input': [[1,2,3],[4,5,6]],
            'output': 12,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.minPathSum(param['input'])
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
