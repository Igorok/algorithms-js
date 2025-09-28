from typing import List
from json import dumps
import math
import heapq


class Solution_0:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n: int = len(nums)

        def getPerimeter(a: int, b: int) -> int:
            start: int = b + 1
            end: int = n - 1
            limit: int = nums[a] + nums[b]
            res: int = -1

            while start <= end:
                middle: int = (start + end) // 2
                if nums[middle] < limit:
                    res = middle
                    start = middle + 1
                else:
                    end = middle - 1

            if res == -1:
                return 0

            return nums[a] + nums[b] + nums[res]

        res = -1
        for a in range(n - 2):
            for b in range(a + 1, n - 1):
                perimeter = getPerimeter(a, b)
                res = max(res, perimeter)

        return res


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n: int = len(nums)

        for i in range(n - 3, -1, -1):
            if nums[i] + nums[i + 1] > nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]

        return 0


"""
1 7 8 9


"""


def test():
    params = [
        {
            "input": [2, 1, 2],
            "output": 5,
        },
        {
            "input": [1, 2, 1, 10],
            "output": 0,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.largestPerimeter(param["input"])
        print(
            "SUCCESS" if dumps(result) == dumps(param["output"]) else "ERROR",
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
