from typing import List
from json import dumps
import heapq
from collections import deque
import math


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        res = 0

        while start < end:
            area = min(height[start], height[end]) * (end - start)
            res = max(res, area)
            if height[end] < height[start]:
                end -= 1
            else:
                start += 1

        return res


"""

0 1 2 3  4  5 6  7  8 9 10 11 12 13 14 15 16
1 1 1 10 10 3 4  5  1 1 1  1  1  1  1  1  1
0 1 2 3  10 6 16 20 5 6 7  8  9  10 11 12 13

0 1 2 3  4 5 6 7 8 9 10 11 12 13 14 15 16
1 1 1 10 1 1 1 1 1 1 1  1  1  1  1  1  1


0 1 2 3 4 5 6 7
1 2 3 1 2 3 2 1

0  1  2  3  4  5  6  7  8
1, 8, 6, 2, 5, 4, 8, 3, 7

"""


def test():
    params = [
        {
            "input": [1, 8, 6, 2, 5, 4, 8, 3, 7],
            "output": 49,
        },
    ]
    solution = Solution()

    for param in params:
        height = param["input"]
        result = solution.maxArea(height)
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
