import heapq
import math
from collections import Counter, defaultdict
from functools import cache
from json import dumps
from typing import List

"""
leetcode "1840. Maximum Building Height"

[5, [[2, 1], [4, 1]]]
Okay I can take 0 height and 1 and build 1 height.
I have restrictions
0 1 2 3 4 5 6
0 5 5 5 5 5 1
I build a heights
0 1 2 3 4 5 1
I can not build a height 5, I should walk back like in monotonic stack and fix restrictions
0 1 2 3 3 2 1
Now I can walk through restrictions an calculate a piramid

(1,0),(2,5); steps = 2-1=1; diff=5-0=5; available=0+steps=1;




"""


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # I have restrictions
        # 0 1 2 3 4 5 6
        # 0 5 5 5 5 5 1
        # left border
        restrictions.append([1, 0])

        restrictions = sorted(restrictions)

        # right border
        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])

        M = len(restrictions)

        # print(1, restrictions)

        # I build a heights
        # 0 1 2 3 4 5 1
        # build from left to right
        for i in range(1, M):
            idPrev, heightPrev = restrictions[i - 1]
            id, height = restrictions[i]
            diff = id - idPrev
            h = min(height, heightPrev + diff)
            restrictions[i][1] = h

        # print(2, restrictions)

        # I can not build a height 5, I should walk back and fix restrictions
        # 0 1 2 3 3 2 1
        for i in range(M - 2, -1, -1):
            id, height = restrictions[i]
            idNext, heightNext = restrictions[i + 1]
            diff = idNext - id
            h = min(height, heightNext + diff)
            restrictions[i][1] = h

        # print(3, restrictions)

        """
        i build a piramid
        0 1 2 3 4 5 6
        1 2 3 4 5 4 3
        steps = 6 - 0
        before building a piramid I should have an equal height
        diff = 3 - 1 = 2
        remaining = 6 - 2 = 4
        top of piramid = 4 // 2 = 2
        max height = 3 + 2 = 5
        peak = max(h1, h2) + (steps - diff) // 2
        h1 = min
        h2 = max
        peak = h2 + (steps - (h2 - h1)) // 2 = (2*h2 + steps - h2 + h1) // 2
        = (h2 + steps + h1) // 2
        """

        res = 0
        for i in range(1, M):
            id, height = restrictions[i]
            idPrev, heightPrev = restrictions[i - 1]

            peak = (height + heightPrev + id - idPrev) // 2
            res = max(res, peak)

        return res


def test():
    params = [
        # {
        #     "input": [5, [[2, 1], [4, 1]]],
        #     "output": 2,
        # },
        # {
        #     "input": [6, []],
        #     "output": 5,
        # },
        # {
        #     "input": [10, [[5, 3], [2, 5], [7, 4], [10, 3]]],
        #     "output": 5,
        # },
        {
            "input": [
                10,
                [
                    [8, 5],
                    [9, 0],
                    [6, 2],
                    [4, 0],
                    [3, 2],
                    [10, 0],
                    [5, 3],
                    [7, 3],
                    [2, 4],
                ],
            ],
            "output": 2,
        },
    ]
    solution = Solution()

    for param in params:
        n, restrictions = param["input"]
        result = solution.maxBuilding(n, restrictions)
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
