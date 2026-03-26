from typing import List
from json import dumps
from collections import deque
import heapq

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        N = len(grid)
        M = len(grid[0])

        suffix = [0]*N*M

        for row in range(N-1, -1, -1):
            for col in range(M-1, -1, -1):
                prev = 1 if row == N-1 and col == M-1 else suffix[row*M + col + 1]
                curr = (grid[row][col] * prev) % MOD
                suffix[row*M + col] = curr

        res = []
        prev = 1
        for row in range(N):
            res.append([])
            for col in range(M):
                nextVal = 1 if row == N-1 and col == M-1 else suffix[row*M + col + 1]
                res[row].append((prev * nextVal) % MOD)
                prev = (prev * grid[row][col]) % MOD

        return res



def test ():
    params = [
        {
            'input': [[1,2],[3,4]],
            'output': [[24,12],[8,6]],
        },
        {
            'input': [[12345],[2],[1]],
            'output': [[2],[0],[0]],
        },
    ]
    solution = Solution()

    for param in params:
        grid = param['input']
        result = solution.constructProductMatrix(grid)

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            # 'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
