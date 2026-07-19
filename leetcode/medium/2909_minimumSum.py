import json
import math
from collections import Counter, defaultdict, deque

# from functools import cache
from linecache import cache
from typing import List


class Solution_0:
    def minimumSum(self, nums: List[int]) -> int:
        N = len(nums)
        rightIds = [0] * N
        rightIds[N - 1] = N - 1

        for i in range(N - 2, -1, -1):
            id = rightIds[i + 1]
            if nums[i] < nums[id]:
                id = i
            rightIds[i] = id

        print("rightIds", rightIds)

        res = float("inf")
        leftId = 0
        for i in range(1, N - 1):
            rightId = rightIds[i + 1]

            if nums[leftId] < nums[i] and nums[i] > nums[rightId]:
                print(leftId, i, rightId)
                res = min(res, leftId + i + rightId)

            if nums[i] < nums[leftId]:
                leftId = i

        return -1 if res == float("inf") else res


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        N = len(nums)
        rightVals = [0] * N
        rightVals[N - 1] = nums[-1]

        for i in range(N - 2, -1, -1):
            rightVals[i] = min(rightVals[i + 1], nums[i])

        res = float("inf")
        left = nums[0]
        for i in range(1, N - 1):
            right = rightVals[i + 1]

            if left < nums[i] and nums[i] > right:
                res = min(res, left + nums[i] + right)

            if nums[i] < left:
                left = nums[i]

        return -1 if res == float("inf") else res


def test():
    params = [
        {"input": [8, 6, 1, 5, 3], "output": 9},
        {"input": [5, 4, 8, 7, 10, 2], "output": 13},
        {"input": [6, 5, 4, 3, 4, 5], "output": -1},
    ]
    solution = Solution()

    for param in params:
        nums = param["input"]
        result = solution.minimumSum(nums)
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
