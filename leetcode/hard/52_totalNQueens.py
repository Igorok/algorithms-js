from typing import List
from json import dumps
import heapq
from collections import deque


class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        board = [[0]*n for i in range(n)]
        colls = [0]*n

        def isInvalidLoc(y, x):
            return y == -1 or x == -1 or y == n or x == n

        def checDiagonal(y, x):
            def checkBottomLeft(y, x):
                if isInvalidLoc(y, x):
                    return True
                if board[y][x] == 1:
                    return False
                return checkBottomLeft(y-1, x-1)
            def checkBottomRight(y, x):
                if isInvalidLoc(y, x):
                    return True
                if board[y][x] == 1:
                    return False
                return checkBottomRight(y-1, x+1)

            return checkBottomLeft(y, x) and checkBottomRight(y, x)



        def dfs(row):
            nonlocal res, n, board, colls, checDiagonal

            if row == n:
                res += 1
                return

            for i in range(n):
                if colls[i] == 0 and checDiagonal(row, i):
                    colls[i] = 1
                    board[row][i] = 1

                    dfs(row + 1)

                    colls[i] = 0
                    board[row][i] = 0

        dfs(0)

        return res

def test ():
    params = [
        {
            'input': 4,
            'output': 2,
        },
        {
            'input': 1,
            'output': 1,
        },
        {
            'input': 9,
            'output': 352,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.totalNQueens(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
