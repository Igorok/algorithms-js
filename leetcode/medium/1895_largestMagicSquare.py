from typing import List
import heapq
import math
from collections import defaultdict, deque


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])

        res = 1
        columns = [[0]*M for i in range(N)]
        rows = [[0]*M for i in range(N)]
        diagonalLeft = [[0]*M for i in range(N)]
        diagonalRight = [[0]*M for i in range(N)]

        for r in range(N):
            for c in range(M):
                columns[r][c] = rows[r][c] = diagonalLeft[r][c] = diagonalRight[r][c] = grid[r][c]
                if r > 0:
                    columns[r][c] += columns[r-1][c]
                if c > 0:
                    rows[r][c] += rows[r][c-1]
                if r > 0 and c > 0:
                    diagonalLeft[r][c] += diagonalLeft[r-1][c-1]
                if r > 0 and c < M-1:
                    diagonalRight[r][c] += diagonalRight[r-1][c+1]


                for shift in range(2, min(r, c)+2):
                    prevDLeft = diagonalLeft[r-shift][c-shift] if r-shift >= 0 and c-shift >= 0 else 0
                    dLeft = diagonalLeft[r][c] - prevDLeft

                    prevDRight = diagonalRight[r-shift][c+1] if r-shift >= 0 and c+1 < M else 0
                    dRight = diagonalRight[r][c-shift+1] - prevDRight

                    # print(r,c, dLeft, dRight, shift)

                    if dLeft != dRight:
                        continue

                    isOk = True
                    for s in range(shift):
                        col = c-s
                        row = r-s

                        prev = 0 if c - shift < 0 else rows[row][c-shift]
                        l2 = rows[row][c] - prev

                        prev = 0 if r - shift < 0 else columns[r-shift][col]
                        l1 = columns[r][col] - prev


                        if l1 != dLeft or l2 != dLeft:
                            isOk = False
                            break

                    if isOk:
                        res = max(res, shift)








        return res

'''
[
[8,1,6],
[3,5,7],
[4,9,2],
[7,10,9]
]

'''


def test ():
    params = [
        {
            'input': [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]],
            'output': 3,
        },
        {
            'input': [[5,1,3,1],[9,3,3,1],[1,3,3,8]],
            'output': 2,
        },
        {
            'input': [[8,1,6],[3,5,7],[4,9,2],[7,10,9]],
            'output': 3,
        },
    ]
    solution = Solution()

    for param in params:
        grid = param['input']
        result = solution.largestMagicSquare(grid)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
