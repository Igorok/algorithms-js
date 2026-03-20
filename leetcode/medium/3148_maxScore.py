from typing import List
from json import dumps
from collections import deque
import heapq

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])

        res = float('-inf')
        memo = []
        for row in range(N):
            memo.append([])
            for col in range(M):
                memo[row].append(float('inf'))

                if row > 0:
                    memo[row][col] = min(memo[row][col], memo[row-1][col])
                if col > 0:
                    memo[row][col] = min(memo[row][col], memo[row][col-1])

                res = max(res, grid[row][col] - memo[row][col])
                memo[row][col]= min(memo[row][col], grid[row][col])


        return res


def test ():
    params = [
        {
            'input': [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]],
            'output': 9,
        },
        {
            'input': [[4,3,2],[3,2,1]],
            'output': -1,
        },
    ]
    solution = Solution()

    for param in params:
        grid = param['input']
        result = solution.maxScore(grid)

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            # 'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
