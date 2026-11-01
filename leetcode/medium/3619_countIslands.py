import json
from collections import defaultdict, deque
from functools import cache
from typing import List


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        N = len(grid)
        M = len(grid[0])

        shifts = ((1, 0), (-1, 0), (0, 1), (0, -1))
        visited = [[-1] * M for _ in range(N)]

        def dfs(row, col):

            val = grid[row][col] % k

            for sR, sC in shifts:
                newR = sR + row
                newC = sC + col
                if newR < 0 or newR >= N or newC < 0 or newC >= M:
                    continue
                if grid[newR][newC] == 0 or visited[newR][newC] != -1:
                    continue

                visited[newR][newC] = 1
                val = (val + dfs(newR, newC)) % k

            return val % k

        res = 0
        for row in range(N):
            for col in range(M):
                if grid[row][col] == 0 or visited[row][col] != -1:
                    continue
                visited[row][col] = 1
                v = dfs(row, col)
                if v == 0:
                    res += 1

        return res


"""

[
[0, 0, 0],
[0, 0, 1],
[11, 0, 6],
[0, 10, 2],
[0, 0, 0],
[8, 0, 0]
]



"""


def test():
    params = [
        {
            "input": [
                [
                    [0, 2, 1, 0, 0],
                    [0, 5, 0, 0, 5],
                    [0, 0, 1, 0, 0],
                    [0, 1, 4, 7, 0],
                    [0, 2, 0, 0, 8],
                ],
                5,
            ],
            "output": 2,
        },
        {
            "input": [[[3, 0, 3, 0], [0, 3, 0, 3], [3, 0, 3, 0]], 3],
            "output": 6,
        },
        {
            "input": [
                [[0, 0, 0], [0, 0, 1], [11, 0, 6], [0, 10, 2], [0, 0, 0], [8, 0, 0]],
                19,
            ],
            "output": 1,
        },
    ]
    solution = Solution()

    for param in params:
        grid, k = param["input"]
        result = solution.countIslands(grid, k)
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
