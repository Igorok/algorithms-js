import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq
import math

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        n = len(board)
        m = len(board[0])

        shifts = ((-1, -1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
        def getCount(row, col):
            count = 0
            for sR, sC in shifts:
                newR = row + sR
                newC = col + sC
                if newR < 0 or newR == n or newC < 0 or newC == m:
                    continue
                if board[newR][newC] == 'M':
                    count += 1
            return count

        def updateBoard(row, col):
            for sR, sC in shifts:
                newR = row + sR
                newC = col + sC
                if newR < 0 or newR == n or newC < 0 or newC == m:
                    continue
                if board[newR][newC] != 'E':
                    continue

                count = getCount(newR, newC)
                if count != 0:
                    board[newR][newC] = str(count)
                    continue

                board[newR][newC] = 'B'
                updateBoard(newR, newC)

        row, col = click
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board

        count = getCount(row, col)
        if count != 0:
            board[row][col] = str(count)
            return board

        board[row][col] = 'B'
        updateBoard(row, col)


        return board


def test ():
    params = [
        {
            'input': [
                [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]],
                [3,0]
            ],
            'output': [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]],
        },
        {
            'input': [
                [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]],
                [1,2]
            ],
            'output': [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]],
        },
    ]
    solution = Solution()

    for param in params:
        board, click = param['input']
        result = solution.updateBoard(board, click)
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
