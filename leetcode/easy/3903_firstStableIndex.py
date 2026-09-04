import json
from collections import deque
from functools import cache
from typing import List


class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        N = len(nums)
        minRight = [0] * N
        minRight[N - 1] = nums[N - 1]
        for i in range(N - 2, -1, -1):
            minRight[i] = min(minRight[i + 1], nums[i])

        maxLeft = nums[0]
        for i in range(N):
            maxLeft = max(maxLeft, nums[i])
            score = maxLeft - minRight[i]
            if score <= k:
                return i

        return -1


def test():
    params = [
        {
            "input": [[5, 0, 1, 4], 3],
            "output": 3,
        },
        {
            "input": [[3, 2, 1], 1],
            "output": -1,
        },
        {
            "input": [[0], 0],
            "output": 0,
        },
    ]
    solution = Solution()

    for param in params:
        nums, k = param["input"]
        result = solution.firstStableIndex(nums, k)
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
