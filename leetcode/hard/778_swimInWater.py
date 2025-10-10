from typing import List
from json import dumps
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        shifts = ((1, 0), (-1, 0), (0, 1), (0, -1))
        n = len(grid)
        visited = [[-1]*n for _ in range(n)]
        waterHeap = [(0,0,grid[0][0])]

        res = float('inf')

        while waterHeap:
            _row, _col, _time = heapq.heappop(waterHeap)
            if _row == n-1 and _col  == n-1:
                res = min(res, _time)
                continue

            for sR, sC in shifts:
                newR = _row + sR
                newC = _col + sC

                if newR < 0 or newR == n or newC < 0 or newC == n:
                    continue

                newT = max(_time, grid[newR][newC])

                if visited[newR][newC] != -1 and visited[newR][newC] <= newT:
                    continue

                visited[newR][newC] = newT
                heapq.heappush(waterHeap, (newR, newC, newT))

        return res

def test ():
    params = [
        {
            'input': [[0,2],[1,3]],
            'output': 3,
        },
        {
            'input': [
                [0,1,2,3,4],
                [24,23,22,21,5],
                [12,13,14,15,16],
                [11,17,18,19,20],
                [10,9,8,7,6]
            ],
            'output': 16,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.swimInWater(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
