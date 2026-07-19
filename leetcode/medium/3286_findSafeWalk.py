import heapq
import json
import math
from collections import defaultdict, deque
from typing import List


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        N = len(grid)
        M = len(grid[0])
        memo = [[0] * M for i in range(N)]

        shifts = ((1, 0), (-1, 0), (0, 1), (0, -1))

        memo[0][0] = health - grid[0][0]
        if memo[0][0] <= 0:
            return False

        gridQueue = [(memo[0][0], 0, 0)]

        while gridQueue:
            h, r, c = heapq.heappop(gridQueue)

            if r == N - 1 and c == M - 1:
                return True

            for sR, sC in shifts:
                newR = r + sR
                newC = c + sC

                if newR < 0 or newR == N or newC < 0 or newC == M:
                    continue

                newH = h - grid[newR][newC]
                if newH <= 0 or memo[newR][newC] >= newH:
                    continue

                memo[newR][newC] = newH
                heapq.heappush(gridQueue, (newH, newR, newC))

        return False


def test():
    params = [
        {
            "input": [[[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]], 1],
            "output": True,
        },
        {
            "input": [
                [
                    [0, 1, 1, 0, 0, 0],
                    [1, 0, 1, 0, 0, 0],
                    [0, 1, 1, 1, 0, 1],
                    [0, 0, 1, 0, 1, 0],
                ],
                3,
            ],
            "output": False,
        },
        {
            "input": [[[1, 1, 1], [1, 0, 1], [1, 1, 1]], 5],
            "output": True,
        },
    ]
    solution = Solution()

    for param in params:
        grid, health = param["input"]
        result = solution.findSafeWalk(grid, health)
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
