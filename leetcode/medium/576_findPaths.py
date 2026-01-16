import json
from collections import defaultdict, deque
from typing import List
# from functools import cache
import math

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 7 + 10**9
        memo = []

        for i in range(m):
            row = []
            for j in range(n):
                row.append([-1] * (maxMove + 1))
            memo.append(row)

        def dfs(row, col, steps):
            nonlocal n, m
            shifts = ((1,0),(-1,0),(0,1),(0,-1))

            if memo[row][col][steps] != -1:
                return memo[row][col][steps]

            if steps == 0:
                return 0

            res = 0
            for sR, sC in shifts:
                newR = row + sR
                newC = col + sC

                if newR < 0 or newR == m or newC < 0 or newC == n:
                    res += 1
                    continue

                res = (res + dfs(newR, newC, steps - 1)) % MOD

            memo[row][col][steps] = res % MOD

            return memo[row][col][steps]

        r = dfs(startRow, startColumn, maxMove)
        return r

def test():
    params = [
        {
            "input": [2, 2, 2, 0, 0],
            "output": 6,
        },
        {
            "input": [1, 3, 3, 0, 1],
            "output": 12,
        },
    ]
    solution = Solution()

    for param in params:
        m, n, maxMove, startRow, startColumn = param["input"]
        result = solution.findPaths(m, n, maxMove, startRow, startColumn)
        correct = json.dumps(result) == json.dumps(param["output"])

        msg = "SUCCESS" if correct else "ERROR"
        msg += "\n"
        if not correct:
            # msg += "input " + json.dumps(param["input"]) + "\n"
            msg += "output " + json.dumps(param["output"]) + "\n"
            msg += "result " + json.dumps(result) + "\n"

        print(msg)


if __name__ == "__main__":
    test()
