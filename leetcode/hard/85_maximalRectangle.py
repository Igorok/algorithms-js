from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        heights = [[0]*m for i in range(n)]

        def getMaxSquare(arr):
            nonlocal m

            row = arr.copy()
            res = row[0]

            for i in range(1, m):
                l = i-1
                while l > -1 and row[l] != 0 and row[i] < row[l]:
                    s = row[l] * (i-l)
                    res = max(res, s)
                    row[l] = row[i]
                    l -= 1

            for i in range(m):
                s = row[i] * (m-i)
                res = max(res, s)

            return res

        res = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    top = 0 if i == 0 or heights[i-1][j] == 0 else heights[i-1][j]
                    heights[i][j] = top + 1

                if j == (m-1):
                    r = getMaxSquare(heights[i])
                    res = max(res, r)

        return res

'''

["1","0","0","0","1"],
["1","1","0","1","1"],
["1","1","1","1","1"]

1 0 0 0 1
2 1 0 1 2
3 2 1 2 3


'''

def test ():
    params = [
        {
            'input': [["1","0","0","0","1"],["1","1","0","1","1"],["1","1","1","1","1"]],
            'output': 5,
        },
        {
            'input': [["1", '0']],
            'output': 1,
        },
        {
            'input': [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]],
            'output': 6,
        },
        {
            'input': [["0"]],
            'output': 0,
        },
        {
            'input': [["1"]],
            'output': 1,
        },

    ]
    solution = Solution()

    for param in params:
        result = solution.maximalRectangle(param['input'])
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
