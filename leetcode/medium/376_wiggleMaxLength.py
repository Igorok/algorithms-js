import heapq
import json
from collections import defaultdict, deque
from functools import cache
from typing import List

"""
376. Wiggle Subsequence

"""


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = len(nums)

        @cache
        def rec(prev, sign, curr):
            nonlocal N, nums

            if curr == N:
                return 0

            if prev == -1:
                r1 = 1 + rec(curr, 1, curr + 1)
                r2 = 1 + rec(curr, 0, curr + 1)
                r3 = rec(prev, sign, curr + 1)

                return max(r1, r2, r3)

            r1 = rec(prev, sign, curr + 1)
            r2 = 0
            _sign = 1 if nums[curr] > nums[prev] else 0
            if nums[curr] != nums[prev] and _sign != sign:
                r2 = 1 + rec(curr, _sign, curr + 1)

            return max(r1, r2)

        return rec(-1, 0, 0)


def test():
    params = [
        {
            "input": [1, 7, 4, 9, 2, 5],
            "output": 6,
        },
        {
            "input": [1, 17, 5, 10, 13, 15, 10, 5, 16, 8],
            "output": 7,
        },
        {
            "input": [1, 2, 3, 4, 5, 6, 7, 8, 9],
            "output": 2,
        },
        {
            "input": [0, 0],
            "output": 1,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param["input"]
        result = solution.wiggleMaxLength(nums)

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
