import json
from collections import defaultdict, deque
from functools import cache
from typing import List


class Solution_0:
    def subArrayRanges(self, nums: list[int]) -> int:
        N = len(nums)
        res = 0

        for i in range(N):
            minV = nums[i]
            maxV = nums[i]

            for j in range(i + 1, N):
                minV = min(minV, nums[j])
                maxV = max(maxV, nums[j])
                res += maxV - minV

        return res


"""
1 2 3 4 5



"""


class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        N = len(nums)
        res = 0

        for i in range(N):
            minV = nums[i]
            maxV = nums[i]

            for j in range(i + 1, N):
                minV = min(minV, nums[j])
                maxV = max(maxV, nums[j])
                res += maxV - minV

        return res


def test():
    params = [
        {
            "input": [1, 2, 3],
            "output": 4,
        },
        {
            "input": [1, 3, 3],
            "output": 4,
        },
        {
            "input": [4, -2, -3, 4, 1],
            "output": 59,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param["input"]
        result = solution.subArrayRanges(nums)
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
