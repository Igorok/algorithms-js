from typing import List
from json import dumps
import heapq
from collections import deque


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        visited = [[0] * m for i in range(n)]
        shifts = ((1, 0), (-1, 0), (0, 1), (0,-1))

        def isInvalidLoc(y, x):
            return y == -1 or x == -1 or y == n or x == m or visited[y][x] != 0

        def dfs(y, x, id):
            if board[y][x] != word[id]:
                return False

            if id == len(word) - 1:
                return True

            for shiftY, shiftX in shifts:
                i = y + shiftY
                j = x + shiftX
                if isInvalidLoc(i, j):
                    continue

                visited[i][j] = 1
                r = dfs(i, j, id + 1)
                if r:
                    return True
                visited[i][j] = 0

            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited[i][j] = 1
                    if dfs(i, j, 0):
                        return True
                    visited[i][j] = 0
        return False

def test ():
    params = [
        {
            'input': [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"],
            'output': True,
        },
        {
            'input': [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"],
            'output': True,
        },
        {
            'input': [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"],
            'output': False,
        },
    ]
    solution = Solution()

    for param in params:
        board, word = param['input']
        result = solution.exist(board, word)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
