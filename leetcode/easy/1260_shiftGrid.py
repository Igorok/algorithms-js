import heapq
import json
from collections import defaultdict, deque
from functools import lru_cache
from typing import List

"""
I think this is a crap issue. It is easy? I read it 3 times and i don't understand what does it mean. And should know the solution of this is flatten to 1 demension? It is clearly?
"""


class Solution_0:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        N = len(grid)
        M = len(grid[0])

        memo = [0] * (N * M)
        length = M * N
        moves = k % (N * M)

        if moves == 0:
            return grid

        # print("moves", moves)

        for row in range(N):
            for col in range(M):
                currId = (row * M) + col
                nextId = (currId + moves) % length

                # print("currId", currId, "moves", moves, (currId + moves) % moves)

                memo[nextId] = grid[row][col]

                # print(row, col, currId, nextId, grid[row][col], memo[nextId])

        # print("memo", memo)

        res = [[0] * M for i in range(N)]
        for row in range(N):
            for col in range(M):
                currId = (row * M) + col
                res[row][col] = memo[currId]

                # print(row, col, currId, memo[currId], res[row][col])

        return res


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        N = len(grid)
        M = len(grid[0])

        res = [[0] * M for i in range(N)]
        length = M * N
        moves = k % length

        if moves == 0:
            return grid

        for row in range(N):
            for col in range(M):
                currId = (row * M) + col
                nextId = (currId + moves) % length

                nextRow = nextId // M
                nextCol = nextId % M
                res[nextRow][nextCol] = grid[row][col]

        return res


def test():
    params = [
        {
            "input": [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1],
            "output": [[9, 1, 2], [3, 4, 5], [6, 7, 8]],
        },
        {
            "input": [
                [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]],
                4,
            ],
            "output": [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]],
        },
        {
            "input": [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9],
            "output": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        },
        {
            "input": [[[1], [2], [3], [4], [7], [6], [5]], 23],
            "output": [[6], [5], [1], [2], [3], [4], [7]],
        },
    ]
    solution = Solution()

    for param in params:
        grid, k = param["input"]
        result = solution.shiftGrid(grid, k)

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
