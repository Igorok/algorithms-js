from typing import List
import json
from collections import deque


class Solution_0:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        n1 = n+1
        grid = [[0]*n1 for i in range(n1)]

        def fill(r1, c1, r2, c2):
            for r in range(r1, r2+1):
                grid[r][c1] += 1
                grid[r][c2+1] -= 1

        for r1, c1, r2, c2 in queries:
            fill(r1, c1, r2, c2)

        res = [[0]*n for i in range(n)]
        for r in range(n):
            acc = 0
            for c in range(n):
                acc += grid[r][c]
                res[r][c] = acc

        return res



class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        n1 = n+1
        grid = [[0]*n1 for i in range(n1)]

        for r1, c1, r2, c2 in queries:
            grid[r1][c1] += 1
            grid[r1][c2+1] -= 1
            grid[r2+1][c1] -= 1
            grid[r2+1][c2+1] += 1

        res = [[0]*n for i in range(n)]
        for r in range(n):
            for c in range(n):
                top = 0 if r == 0 else res[r-1][c]
                left = 0 if c == 0 else res[r][c-1]
                diag = 0 if r == 0 or c == 0 else res[r-1][c-1]
                res[r][c] += grid[r][c] + top + left - diag

        return res

'''

500 * 10_000

3, [[1,1,2,2],[0,0,1,1]]],


 1  0 -1  0
 0  1  0 -1
-1  0  1  0
 0 -1  0  1

1 1 0
1 2 1
0 1 1








0 0 0
0 0 0
0 0 0


---

'''


def test ():
    params = [
        {
            'input': [3, [[1,1,2,2],[0,0,1,1]]],
            'output': [[1,1,0],[1,2,1],[0,1,1]],
        },
        {
            'input': [2, [[0,0,1,1]]],
            'output': [[1,1],[1,1]],
        },
    ]
    solution = Solution()

    for param in params:
        n, queries = param['input']
        result = solution.rangeAddQueries(n, queries)
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
