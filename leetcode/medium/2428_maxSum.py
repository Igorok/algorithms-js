from typing import List
import json
from collections import deque, defaultdict
import heapq
import math


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        prefix = [[0]*m for i in range(n)]

        for row in range(n):
            for col in range(m):
                top = 0 if row == 0 else prefix[row-1][col]
                left = 0 if col == 0 else prefix[row][col-1]
                diag = 0 if row == 0 or col == 0 else prefix[row-1][col-1]

                prefix[row][col] = top + left - diag + grid[row][col]

        res = 0

        for row in range(2, n):
            for col in range(2, m):
                top = 0 if row - 3 < 0 else prefix[row-3][col]
                left = 0 if col - 3 < 0 else prefix[row][col-3]
                diag = 0 if row - 3 < 0 or col - 3 < 0 else prefix[row-3][col-3]

                square = prefix[row][col] - top - left + diag
                square -= grid[row-1][col] + grid[row-1][col-2]

                res = max(res, square)

        return res

'''

1 1 1 1
1 2 2 2
1 2 2 2
1 2 2 2

1 2 3 4
2 5 8 11


11-5-4+2=4

'''



def test ():
    params = [
        {
            'input': [
                [520626,685427,788912,800638,717251,683428],
                [23602,608915,697585,957500,154778,209236],
                [287585,588801,818234,73530,939116,252369]
            ],
            'output': 5095181,
        },
        {
            'input': [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]],
            'output': 30,
        },
        {
            'input': [[1,2,3],[4,5,6],[7,8,9]],
            'output': 35,
        },
    ]
    solution = Solution()

    for param in params:
        s = param['input']
        result = solution.maxSum(s)
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
