from collections import deque
from functools import cache
from json import dumps
from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        N = len(stoneValue)

        @cache
        def rec(start):
            if start >= N:
                return 0

            diff1 = float("-inf")
            diff2 = float("-inf")
            diff3 = float("-inf")

            diff1 = stoneValue[start] - rec(start + 1)

            if start + 1 < N:
                diff2 = stoneValue[start] + stoneValue[start + 1] - rec(start + 2)

            if start + 2 < N:
                diff3 = (
                    stoneValue[start]
                    + stoneValue[start + 1]
                    + stoneValue[start + 2]
                    - rec(start + 3)
                )

            return max(diff1, diff2, diff3)

        r = rec(0)

        if r > 0:
            return "Alice"
        elif r == 0:
            return "Tie"
        else:
            return "Bob"


def test():
    params = [
        {
            "input": [1, 2, 3, 7],
            "output": "Bob",
        },
        {
            "input": [1, 2, 3, -9],
            "output": "Alice",
        },
        {
            "input": [1, 2, 3, 6],
            "output": "Tie",
        },
    ]
    solution = Solution()

    for param in params:
        stoneValue = param["input"]
        result = solution.stoneGameIII(stoneValue)
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
