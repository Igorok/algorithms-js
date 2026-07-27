import heapq
import json
from collections import defaultdict, deque
from functools import lru_cache
from typing import List


class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        N = len(nums)
        toRight = [float("inf")] * N
        toRight[0] = 0
        toRight[1] = 1
        toLeft = [float("inf")] * N
        toLeft[N - 1] = 0
        toLeft[N - 2] = 1

        for i in range(1, N - 1):
            left = nums[i - 1]
            right = nums[i + 1]

            leftDiff = nums[i] - left
            rightDiff = right - nums[i]
            if leftDiff > rightDiff:
                toRight[i + 1] = toRight[i] + 1
            else:
                toRight[i + 1] = toRight[i] + rightDiff

        for i in range(N - 2, 0, -1):
            left = nums[i - 1]
            right = nums[i + 1]

            leftDiff = nums[i] - left
            rightDiff = right - nums[i]
            if rightDiff >= leftDiff:
                toLeft[i - 1] = toLeft[i] + 1
            else:
                toLeft[i - 1] = toLeft[i] + leftDiff

        print(
            "toRight",
            toRight,
        )
        print(
            "toLeft",
            toLeft,
        )

        M = len(queries)
        res = [0] * M
        for i in range(M):
            s, e = queries[i]
            if s == e:
                continue
            if s < e:
                res[i] = min(nums[e] - nums[s], toRight[e] - toRight[s])
            else:
                res[i] = min(nums[s] - nums[e], toLeft[e] - toLeft[s])

        return res


def test():
    params = [
        # {
        #     "input": [[-5, -2, 3], [[0, 2], [2, 0], [1, 2]]],
        #     "output": [6, 2, 5],
        # },
        # {
        #     "input": [[0, 2, 3, 9], [[3, 0], [1, 2], [2, 0]]],
        #     "output": [4, 1, 3],
        # },
        # {
        #     "input": [[1, 2, 3, 10, 11, 12], [[0, 5]]],
        #     "output": [11],
        # },
        # {
        #     "input": [[1, 2, 5, 10, 11, 12], [[0, 5]]],
        #     "output": [11],
        # },
        {
            "input": [
                [-25, 6, 12, 18, 33],
                [[2, 1], [3, 4]],
            ],
            "output": [1, 15],
        },
    ]
    solution = Solution()

    for param in params:
        nums, queries = param["input"]
        result = solution.minCost(nums, queries)
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
