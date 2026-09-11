import json
from collections import deque
from functools import cache
from typing import List


class Solution_0:
    def minCost(
        self,
        startPos: List[int],
        homePos: List[int],
        rowCosts: List[int],
        colCosts: List[int],
    ) -> int:
        shifts = ((1, 0), (-1, 0), (0, 1), (0, -1))
        N = len(rowCosts)
        M = len(colCosts)
        memo = [[-1] * M for _ in range(N)]

        def rec(row, col):
            if row == homePos[0] and col == homePos[1]:
                return 0

            if memo[row][col] != -1:
                return memo[row][col]

            memo[row][col] = float("inf")

            for sR, sC in shifts:
                nR = row + sR
                nC = col + sC

                if nR == N or nR == -1 or nC == M or nC == -1:
                    continue

                cost = rowCosts[nR] if sC == 0 else colCosts[nC]
                cellCost = rec(nR, nC)

                memo[row][col] = min(memo[row][col], cost + cellCost)

            return memo[row][col]

        return rec(startPos[0], startPos[1])


class Solution:
    def minCost(
        self,
        startPos: List[int],
        homePos: List[int],
        rowCosts: List[int],
        colCosts: List[int],
    ) -> int:
        res = 0
        if startPos[0] < homePos[0]:
            for r in range(startPos[0] + 1, homePos[0] + 1):
                res += rowCosts[r]
        else:
            for r in range(startPos[0] - 1, homePos[0] - 1, -1):
                res += rowCosts[r]

        if startPos[1] < homePos[1]:
            for r in range(startPos[1] + 1, homePos[1] + 1):
                res += colCosts[r]
        else:
            for r in range(startPos[1] - 1, homePos[1] - 1, -1):
                res += colCosts[r]

        return res


def test():
    params = [
        {
            "input": [[1, 0], [2, 3], [5, 4, 3], [8, 2, 6, 7]],
            "output": 18,
        },
        {
            "input": [[0, 0], [0, 0], [5], [26]],
            "output": 0,
        },
    ]
    solution = Solution()

    for param in params:
        startPos, homePos, rowCosts, colCosts = param["input"]
        result = solution.minCost(startPos, homePos, rowCosts, colCosts)
        correct = json.dumps(result) == json.dumps(param["output"])

        msg = "SUCCESS" if correct else "ERROR"
        msg += "\n"
        if not correct:
            msg += "input " + json.dumps(param["input"]) + "\n"
            msg += "output " + json.dumps(param["output"]) + "\n"
            msg += "result " + json.dumps(result) + "\n"

        print(msg)


if __name__ == "__main__":
    test()
