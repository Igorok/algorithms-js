from typing import List
import json
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        shifts = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
        n = len(grid)
        memo = [[float('inf')]*n for i in range(n)]
        memo[0][0] = 1

        cellQueue = deque()
        cellQueue.append((0, 0, 1))

        while cellQueue:
            r, c, length = cellQueue.popleft()
            newL = length + 1

            if r == n-1 and c == n-1:
                return length

            for sR, sC in shifts:
                newR = r + sR
                newC = c + sC
                if newR == -1 or newR == n or newC == -1 or newC == n:
                    continue
                if grid[newR][newC] == 1 or memo[newR][newC] <= newL:
                    continue

                memo[newR][newC] = newL
                cellQueue.append((newR, newC, length + 1))

        return -1


def test ():
    params = [
        {
            'input': [[0,1],[1,0]],
            'output': 2,
        },
        {
            'input': [[0,1],[1,0]],
            'output': 2,
        },
        {
            'input': [[0,0,0],[1,1,0],[1,1,0]],
            'output': 4,
        },
        {
            'input': [[1,0,0],[1,1,0],[1,1,0]],
            'output': -1,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.shortestPathBinaryMatrix(param['input'])
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
