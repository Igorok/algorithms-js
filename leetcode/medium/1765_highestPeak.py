from typing import List
from json import dumps
from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        cellQueue = deque([])
        offset = ((1,0),(-1,0),(0,1),(0,-1))
        res = [[-1]*n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    res[i][j] = 0
                    cellQueue.append((i, j, 0))

        while cellQueue:
            i, j, v = cellQueue.popleft()
            for offY, offX in offset:
                y = offY + i
                x = offX + j
                if y < 0 or x < 0 or y == m or x == n or res[y][x] != -1:
                    continue
                res[y][x] = v + 1
                cellQueue.append((y, x, v + 1))

        return res

def test ():
    params = [
        {
            'input': [[0,1],[0,0]],
            'output': [[1,0],[2,1]],
        },
        {
            'input': [[0,0,1],[1,0,0],[0,0,0]],
            'output': [[1,1,0],[0,1,1],[1,2,2]],
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.highestPeak(param['input'])
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
