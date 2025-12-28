from typing import List
import json
import heapq
from collections import defaultdict

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        top = 0
        bottom = N-1
        negativeRow = N

        while bottom <= top:
            middle = (top + bottom) // 2
            if grid[middle][0] < 0:
                negativeRow = middle
                top = middle - 1
            else:
                bottom = middle + 1

        res = (N - negativeRow) * M

        for row in range(negativeRow):
            left = 0
            right = M-1
            negativeCol = M
            while left <= right:
                middle = (left + right) // 2
                if grid[row][middle] < 0:
                    negativeCol = middle
                    right = middle - 1
                else:
                    left = middle + 1
            res += (M - negativeCol)

        return res



def test ():
    params = [
        {
            'input': [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]],
            'output': 8,
        },
        {
            'input': [[3,2],[1,0]],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        grid = param['input']
        result = solution.countNegatives(grid)
        print(
            'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
