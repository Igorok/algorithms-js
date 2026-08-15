import math
from collections import defaultdict, deque
from functools import cache
from json import dumps
from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        N = len(nums)

        prefSum = nums[0]
        isValid = True
        unique = set([nums[0]])

        for i in range(1, N):
            unique.add(nums[i])

            if isValid and nums[i - 1] + 1 == nums[i]:
                prefSum += nums[i]
            else:
                isValid = False

        res = prefSum
        while res in unique:
            res += 1

        return res


def test():
    params = [
        {
            "input": [1, 2, 3, 2, 5],
            "output": 6,
        },
        {
            "input": [3, 4, 5, 1, 12, 14, 13],
            "output": 15,
        },
        {
            "input": [1, 5, 4, 2],
            "output": 3,
        },
        {
            "input": [14, 9, 6, 9, 7, 9, 10, 4, 9, 9, 4, 4],
            "output": 15,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param["input"]
        result = solution.missingInteger(nums)
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
