from typing import List
from json import dumps
from collections import deque
import heapq

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        MOD = 10**9 + 7

        memo = []

        def fillValues(val, arr, negative, positive):
            if val > 0:
                if arr[0] != None:
                    negative.append(arr[0] * val)
                    negative.append(arr[1] * val)
                if arr[2] != None:
                    positive.append(arr[2] * val)
                    positive.append(arr[3] * val)
            else:
                if arr[0] != None:
                    positive.append(arr[0] * val)
                    positive.append(arr[1] * val)
                if arr[2] != None:
                    negative.append(arr[2] * val)
                    negative.append(arr[3] * val)


        for row in range(N):
            memo.append([])
            for col in range(M):
                val = grid[row][col]

                if val == 0:
                    memo[row].append([0, 0, 0, 0])
                    continue

                if row == 0 and col == 0:
                    nMin = None if val > 0 else val
                    nMax = None if val > 0 else val
                    pMin = None if val < 0 else val
                    pMax = None if val < 0 else val
                    memo[row].append([nMin, nMax, pMin, pMax])
                    continue

                memo[row].append([None, None, None, None])
                negative = []
                positive = []
                if row > 0:
                    fillValues(grid[row][col], memo[row-1][col], negative, positive)
                if col > 0:
                    fillValues(grid[row][col], memo[row][col-1], negative, positive)

                if negative:
                    memo[row][col][0] = min(negative)
                    memo[row][col][1] = max(negative)
                if positive:
                    memo[row][col][2] = min(positive)
                    memo[row][col][3] = max(positive)


        arr = filter(lambda x: x != None, memo[-1][-1])
        res = max(arr)

        if res == 0:
             return res
        if res < 0:
             return -1

        return res % MOD



def test ():
    params = [
        {
            'input': [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]],
            'output': -1,
        },
        {
            'input': [[1,-2,1],[1,-2,1],[3,-4,1]],
            'output': 8,
        },
        {
            'input': [[1,3],[0,-4]],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        grid = param['input']
        result = solution.maxProductPath(grid)

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            # 'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
