from typing import List
import json
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        shifts = ((1, 0),(-1, 0),(0, 1),(0, -1))
        visited = [[-1]*m for i in range(n)]

        def isInvalidLoc(y, x):
            return y == -1 or x == -1 or y == n or x == m

        def markBorderArea(y, x):
            visited[y][x] = 1
            for shiftY, shiftX in shifts:
                i = y + shiftY
                j = x + shiftX
                if not isInvalidLoc(i, j) and board[i][j] == 'O' and visited[i][j] == -1:
                    markBorderArea(i, j)

        for i in range(n):
            if board[i][0] == 'O' and visited[i][0] == -1:
                markBorderArea(i, 0)
            if board[i][n-1] == 'O' and visited[i][n-1] == -1:
                markBorderArea(i, n-1)

        for i in range(m):
            if board[0][i] == 'O' and visited[0][i] == -1:
                markBorderArea(0, i)
            if board[n-1][i] == 'O' and visited[n-1][i] == -1:
                markBorderArea(n-1, i)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and visited[i][j] == -1:
                    board[i][j] = 'X'





def test ():
    params = [
        {
            'input': [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]],
            'output': [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]],
        },
        {
            'input': [["X"]],
            'output': [["X"]],
        },
        {
            'input': [["O","O","O"],["O","O","O"],["O","O","O"]],
            'output': [["O","O","O"],["O","O","O"],["O","O","O"]],
        },
    ]
    solution = Solution()

    for param in params:
        inputList = [arr.copy() for arr in param['input']]
        solution.solve(inputList)
        correct = json.dumps(inputList) == json.dumps(param['output'])

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(inputList) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
