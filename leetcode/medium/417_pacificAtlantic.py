from typing import List
import json
from collections import deque, defaultdict


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        shifts = ((-1, 0), (1, 0), (0, -1), (0, 1))
        n = len(heights)
        m = len(heights[0])

        memo = [[None] * m for _ in range(n)]

        def dfs(row, col, pRow, pCol):
            if memo[row][col] != None:
                return memo[row][col]

            memo[row][col] = [0, 0]
            if pRow != -1 and heights[pRow][pCol] == heights[row][col]:
                memo[row][col] = memo[pRow][pCol]

            if row - 1 < 0 or col - 1 < 0:
                memo[row][col][0] = 1
            if row + 1 == n or col + 1 == m:
                memo[row][col][1] = 1

            for sR, sC in shifts:
                newR = row + sR
                newC = col + sC

                if (
                    newR < 0
                    or newR == n
                    or newC < 0
                    or newC == m
                    or heights[newR][newC] > heights[row][col]
                ):
                    continue

                r = dfs(newR, newC, row, col)
                if r[0] == 1:
                    memo[row][col][0] = 1
                if r[1] == 1:
                    memo[row][col][1] = 1

            return memo[row][col]

        res = []

        for row in range(n):
            for col in range(m):
                r = dfs(row, col, -1, -1)
                if r[0] == 1 and r[1] == 1:
                    res.append([row, col])

        return res


def test():
    params = [
        {
            "input": [
                [3, 3, 3, 3, 3, 3],
                [3, 0, 3, 3, 0, 3],
                [3, 3, 3, 3, 3, 3]
            ],
            "output": [
                [0, 0],
                [0, 1],
                [0, 2],
                [0, 3],
                [0, 4],
                [0, 5],
                [1, 0],
                [1, 2],
                [1, 3],
                [1, 5],
                [2, 0],
                [2, 1],
                [2, 2],
                [2, 3],
                [2, 4],
                [2, 5],
            ],
        },
        {
            "input": [
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4],
            ],
            "output": [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
        },
        {
            "input": [[1]],
            "output": [[0, 0]],
        },
    ]
    solution = Solution()

    for param in params:
        nums = param["input"]
        result = solution.pacificAtlantic(nums)
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
