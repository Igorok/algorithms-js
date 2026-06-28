import heapq
import math
from collections import Counter, defaultdict
from functools import cache
from json import dumps
from operator import countOf
from typing import List

"""
I do not understand - "688. Knight Probability in Chessboard"
It is look like absolutly trash. Positive final if knight never leave a board? But knight can leave a board and come back, but it is negative?

"""


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        shifts = (
            (-2, -1),
            (-2, 1),
            (2, -1),
            (2, 1),
            (1, -2),
            (1, 2),
            (-1, -2),
            (-1, 2),
        )

        @cache
        def dfs(row, col, steps):
            nonlocal n, shifts

            if steps == 0:
                return 1

            prob = 0

            for sRow, sCol in shifts:
                newRow = sRow + row
                newCol = sCol + col

                if newRow >= n or newRow < 0 or newCol >= n or newCol < 0:
                    continue

                p = dfs(newRow, newCol, steps - 1)

                prob += (1 / 8) * p

            return prob

        prob = dfs(row, column, k)

        return prob


"""
 [3, 2, 0, 0]


k - -
- - -
- - -


"""


def test():
    params = [
        {
            "input": [3, 2, 0, 0],
            "output": 0.06250,
        },
        {
            "input": [1, 0, 0, 0],
            "output": 1.00000,
        },
    ]
    solution = Solution()

    for param in params:
        n, k, row, column = param["input"]
        result = solution.knightProbability(n, k, row, column)
        print(
            "SUCCESS" if result == param["output"] else "ERROR",
            "input",
            param["input"],
            "output",
            param["output"],
            "result",
            result,
            "\n",
        )


if __name__ == "__main__":
    test()
