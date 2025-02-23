import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq
import math

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        memo = [[0] * m for i in range(n)]
        res = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '0':
                    continue

                top = 0
                if i > 0 and matrix[i-1][j] == '1':
                    top = memo[i-1][j]
                left = 0
                if j > 0 and matrix[i][j-1] == '1':
                    left = memo[i][j-1]

                if i > 0 and j > 0 and matrix[i-1][j-1] == '1':
                    memo[i][j] = min(top + 1, left + 1, memo[i-1][j-1] + 1)
                else:
                    memo[i][j] = 1

                res = max(res, memo[i][j])



        return res**2

'''
["1","0","1","0","0"],
["1","0","1","1","1"],
["1","1","1","1","1"],
["1","0","0","1","0"]


1 1 0 1 1
1 1 1 0 1
1 1 1 0 1
1 1 1 0 1

1 1 0 0 1
1 1 1 0 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1


["1","0","1","0","0","1","1","1","0"],
["1","1","1","0","0","0","0","0","1"],
["0","0","1","1","0","0","0","1","1"],
["0","1","1","0","0","1","0","0","1"],
["1","1","0","1","1","0","0","1","0"],
["0","1","1","1","1","1","1","0","1"],
["1","0","1","1","1","0","0","1","0"],
["1","1","1","0","1","0","0","0","1"],
["0","1","1","1","1","0","0","1","0"],
["1","0","0","1","1","1","0","0","0"]]



'''

def test ():
    params = [
        {
            'input': [["1","0","1","0","0","1","1","1","0"],["1","1","1","0","0","0","0","0","1"],["0","0","1","1","0","0","0","1","1"],["0","1","1","0","0","1","0","0","1"],["1","1","0","1","1","0","0","1","0"],["0","1","1","1","1","1","1","0","1"],["1","0","1","1","1","0","0","1","0"],["1","1","1","0","1","0","0","0","1"],["0","1","1","1","1","0","0","1","0"],["1","0","0","1","1","1","0","0","0"]],
            'output': 4,
        },
        {
            'input': [["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]],
            'output': 4,
        },
        {
            'input': [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]],
            'output': 4,
        },
        {
            'input': [["0","1"],["1","0"]],
            'output': 1,
        },
        {
            'input': [["0"]],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.maximalSquare(param['input'])
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
