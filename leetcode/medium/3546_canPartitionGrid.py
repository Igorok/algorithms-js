from typing import List
from json import dumps
from collections import deque
import heapq


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        N = len(grid)
        M = len(grid[0])

        memo = []
        for row in range(N):
            memo.append([])

            for col in range(M):
                memo[row].append(grid[row][col])
                if row > 0:
                    memo[row][col] += memo[row-1][col]
                if col > 0:
                    memo[row][col] += memo[row][col-1]
                if row > 0 and col > 0:
                    memo[row][col] -= memo[row-1][col-1]

        if memo[-1][-1] % 2 == 1:
            return False

        if N > 1:
            for row in range(N-1):
                val = memo[row][-1]
                if val*2 == memo[-1][-1]:
                    return True
                if val * 2 > memo[-1][-1]:
                    break
        if M > 1:
            for col in range(M-1):
                val = memo[-1][col]
                if val*2 == memo[-1][-1]:
                    return True
                if val*2 > memo[-1][-1]:
                    break

        memo = None
        return False



def test ():
    params = [
        {
            'input': [[1,4],[2,3]],
            'output': True,
        },
        {
            'input': [[1,3],[2,4]],
            'output': False,
        },
    ]
    solution = Solution()

    for param in params:
        grid = param['input']
        result = solution.canPartitionGrid(grid)

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            # 'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
