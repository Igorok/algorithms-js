import json
from collections import defaultdict, deque
from functools import cache
from typing import List


class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        prev = [set() for i in range(M)]

        for row in range(N):
            curr = [set() for i in range(M)]

            for col in range(M):
                if row == 0 and col == 0:
                    curr[0].add(grid[row][col])
                    continue

                if row > 0:
                    for num in prev[col]:
                        curr[col].add(num ^ grid[row][col])
                if col > 0:
                    for num in curr[col - 1]:
                        curr[col].add(num ^ grid[row][col])

            prev = curr

        return min(prev[-1])


def test():
    params = [
        {
            "input": [[1, 2], [3, 4]],
            "output": 6,
        },
        {
            "input": [[6, 7], [5, 8]],
            "output": 9,
        },
        {
            "input": [[2, 7, 5]],
            "output": 0,
        },
    ]
    solution = Solution()

    for param in params:
        grid = param["input"]
        result = solution.minCost(grid)
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
