from typing import List
import json
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        shifts = ((-1, 0), (1, 0), (0, -1), (0, 1))
        n = len(mat)
        m = len(mat[0])

        res = [[0]*m for i in range(n)]

        cellQueue = deque()

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    cellQueue.append((i,j,0))
                else:
                    res[i][j] = float('inf')


        while cellQueue:
            r, c, length = cellQueue.popleft()
            newL = length + 1

            for sR, sC in shifts:
                newR = r + sR
                newC = c + sC
                if newR == -1 or newR == n or newC == -1 or newC == m:
                    continue
                if res[newR][newC] <= newL:
                    continue
                res[newR][newC] = newL
                cellQueue.append((newR, newC, newL))


        return res

'''

[ [0, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 0, 0] ]


'''


def test ():
    params = [
        {
            'input': [[0,0,0],[0,1,0],[0,0,0]],
            'output': [[0,0,0],[0,1,0],[0,0,0]],
        },
        {
            'input': [[0,0,0],[0,1,0],[1,1,1]],
            'output': [[0,0,0],[0,1,0],[1,2,1]],
        },
        {
            'input': [
                [0, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 0, 0],
            ],
            'output': [
                [0,1,2,2,1,0],
                [1,2,3,2,1,0],
                [2,3,3,2,1,0],
                [3,3,2,1,0,0]
            ],
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.updateMatrix(param['input'])
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
