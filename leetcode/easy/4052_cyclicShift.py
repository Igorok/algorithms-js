import json
from collections import deque
from functools import cache
from typing import List


class Solution:
    def cyclicShift(
        self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]
    ) -> list[list[int]]:
        N = len(grid)
        M = len(grid[0])

        for row in range(len(grid)):
            if row >= len(rowShift):
                break

            shift = rowShift[row] % M

            data = [0] * M
            for col in range(M):
                data[(col - shift + M) % M] = grid[row][col]
            grid[row] = data

        for col in range(len(grid[0])):
            if col >= len(colShift):
                break
            shift = colShift[col] % N
            memo = [0] * N
            for row in range(N):
                memo[row] = grid[row][col]

            for row in range(N):
                grid[(row - shift + N) % N][col] = memo[row]

        return grid


def test():
    params = [
        {
            "input": [2, [[1, 2], [3, 4]], [1, 0], [0, 1]],
            "output": [[2, 4], [3, 1]],
        },
        {
            "input": [3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 0], [2, 2, 1]],
            "output": [[7, 8, 5], [2, 3, 9], [6, 4, 1]],
        },
    ]
    solution = Solution()

    for param in params:
        n, grid, rowShift, colShift = param["input"]
        result = solution.cyclicShift(n, grid, rowShift, colShift)
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
