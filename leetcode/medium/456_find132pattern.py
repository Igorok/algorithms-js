import json
from collections import Counter
from functools import cache
from typing import List


class Solution_0:
    def find132pattern(self, nums: List[int]) -> bool:
        N = len(nums)

        minRight = [float("inf")] * N
        minRight[N - 1] = nums[N - 1]
        for i in range(N - 2, -1, -1):
            minRight[i] = min(nums[i], minRight[i + 1])

        prev = nums[0]
        for i in range(1, N - 1):
            if nums[i] > prev and nums[i] > minRight[i]:
                return True
            prev = min(prev, nums[i])

        return False


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        N = len(nums)

        s2 = float("-inf")
        stack = []

        for i in range(N - 1, -1, -1):
            if nums[i] < s2:
                return True

            while stack and stack[-1] < nums[i]:
                s2 = stack.pop()

            stack.append(nums[i])

        return False


def test():
    params = [
        {
            "input": [1, 2, 3, 4],
            "output": False,
        },
        {
            "input": [3, 1, 4, 2],
            "output": True,
        },
        {
            "input": [-1, 3, 2, 0],
            "output": True,
        },
        {
            "input": [1, 0, 1, -4, -3],
            "output": False,
        },
        {
            "input": [3, 4, 5, 5, 1, 2, 3, 4],
            "output": True,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param["input"]
        result = solution.find132pattern(nums)
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
