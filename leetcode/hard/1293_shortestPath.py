import heapq
import json
import math
from collections import defaultdict, deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        shifts = ((1, 0), (-1, 0), (0, 1), (0, -1))
        N = len(grid)
        M = len(grid[0])

        memo = []
        for r in range(N):
            memo.append([None] * M)
            for c in range(M):
                memo[r][c] = [0] * (k + 2)

        obst = k if grid[0][0] == 0 else k - 1
        if obst == -1:
            return -1

        cellQueue = deque()
        cellQueue.append((0, 0, 0, obst, 0, 0))
        memo[0][0][obst] = 1

        while cellQueue:
            row, col, steps, obst, prevR, prevC = cellQueue.popleft()
            if row == N - 1 and col == M - 1:
                return steps

            for sR, sC in shifts:
                newR = sR + row
                newC = sC + col

                if newR == -1 or newR == N or newC == -1 or newC == M:
                    continue

                if newR == prevR and newC == prevC:
                    continue

                newObs = obst - 1 if grid[newR][newC] == 1 else obst
                if newObs == -1:
                    continue
                if memo[newR][newC][newObs] == 1:
                    continue

                memo[newR][newC][newObs] = 1
                cellQueue.append((newR, newC, steps + 1, newObs, row, col))

        return -1


def test():
    params = [
        {
            "input": [[[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1],
            "output": 6,
        },
        {
            "input": [[[0, 1, 1], [1, 1, 1], [1, 0, 0]], 1],
            "output": -1,
        },
    ]
    solution = Solution()

    for param in params:
        grid, k = param["input"]
        result = solution.shortestPath(grid, k)
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
