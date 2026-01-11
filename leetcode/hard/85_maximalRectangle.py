from typing import List
import json
from collections import deque, defaultdict

class Solution_0:
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



class Solution_1:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        N = len(matrix)
        M = len(matrix[0])
        heights = [[0]*M for i in range(N)]

        res = 0
        for row in range(N):
            for col in range(M):
                prev = 0 if row == 0 else heights[row-1][col]
                heights[row][col] = 0 if matrix[row][col] == '0' else prev + 1


        for row in range(N):
            for col in range(M):
                if heights[row][col] == 0:
                    continue

                stack = []
                for col1 in range(col, M):
                    if heights[row][col1] == 0:
                        prev = 0 if not stack else stack[-1]
                        local = (col1 - col) * prev
                        res = max(res, local)
                        break
                    else:
                        if not stack or heights[row][col1] < stack[-1]:
                            stack.append(heights[row][col1])
                        local = (col1 + 1 - col) * stack[-1]
                        res = max(res, local)


        return res


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        N = len(matrix)
        M = len(matrix[0])
        heights = [[0]*M for i in range(N)]

        res = 0
        for row in range(N):
            stack = []

            for col in range(M):
                prevH = 0 if row == 0 else heights[row-1][col]
                heights[row][col] = 0 if matrix[row][col] == '0' else prevH + 1

                while stack and stack[-1][1] > heights[row][col]:
                    loc, height = stack.pop()
                    area = (col-loc) * height
                    res = max(res, area)
                    if (heights[row][col] != 0 and not stack) or (stack and stack[-1][1] < heights[row][col]):
                        stack.append((loc, heights[row][col]))
                        break

                if (not stack and heights[row][col] != 0) or (stack and stack[-1][1] < heights[row][col]):
                    stack.append((col, heights[row][col]))

            while stack:
                loc, height = stack.pop()
                area = (M-loc) * height
                res = max(res, area)



        return res


'''

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0


1 2 3 4 5 4 3
(1,0),(2,1),(3,2),(4,3)(5,4),(4,5)
(1,0),(2,1),(3,2),(4,3), res = 5* 5-4
(1,0),(2,1),(3,2),(4,3)(3,6)
(1,0),(2,1),(3,2), res = 4* 6-3
...


3 2 1 1 2 3

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
