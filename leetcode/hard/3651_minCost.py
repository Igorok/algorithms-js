import json
from collections import defaultdict, deque
from typing import List
# from functools import cache
import math


class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        M = len(grid)
        N = len(grid[0])

        dp = [[float('inf')] * N for i in range(M)]
        dp[0][0] = 0

        coordForValues = defaultdict(list)
        minPriceForValues = {}

        for r in range(M):
            for c in range(N):
                top = float('inf') if r == 0 else dp[r-1][c]
                left = float('inf') if c == 0 else dp[r][c-1]
                dp[r][c] = min(dp[r][c], top + grid[r][c], left+grid[r][c])

                coordForValues[grid[r][c]].append((r, c))
                minPriceForValues[grid[r][c]] = float('inf')

        res = dp[-1][-1]

        minPriceForValues = dict(sorted(minPriceForValues.items(), reverse = True))


        for t in range(k+1):
            minPrice = float('inf')
            newDp = [[float('inf')] * N for i in range(M)]

            for val in minPriceForValues:
                for r, c in coordForValues[val]:
                    minPrice = min(dp[r][c], minPrice)

                minPriceForValues[val] = minPrice

            for r in range(M):
                for c in range(N):
                    mp = minPriceForValues[grid[r][c]]
                    newDp[r][c] = mp

                    top = float('inf') if r == 0 else newDp[r-1][c]
                    left = float('inf') if c == 0 else newDp[r][c-1]
                    newDp[r][c] = min(newDp[r][c], top + grid[r][c], left+grid[r][c])

            dp = newDp
            res = dp[-1][-1]


        return res


'''
[[[1,3,3],[2,5,4],[4,3,5]], 2]

[
[1,3,3],
[2,5,4],
[4,3,5]
]

[[1,2],[2,3],[3,4]]
[
[1,2],
[2,3],
[3,4]
]


[
[1,2,3,4],
[3,2,3,4],
[1,3,2,4],
]

[[1,2,3,4],[3,2,3,4],[1,3,2,4]]

'''



def test():
    params = [
        {
            "input": [[[1,3,3],[2,5,4],[4,3,5]], 2],
            "output": 7,
        },
        {
            "input": [[[1,2],[2,3],[3,4]], 1],
            "output": 9,
        },
        {
            "input": [
                [
                [1,2,3,4],
                [3,2,3,4],
                [1,3,2,4],
                ],
                2
            ],
            "output": 6,
        },
    ]
    solution = Solution()

    for param in params:
        grid, k = param["input"]
        result = solution.minCost(grid, k)
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
