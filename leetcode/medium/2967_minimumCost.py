import heapq
import json
from collections import defaultdict, deque
from functools import cache
from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)

        res = 0

        return res


def test():
    params = [
        {
            "input": [1, 2, 3, 4, 5],
            "output": 6,
        },
        {
            "input": [10, 12, 13, 14, 15],
            "output": 11,
        },
        {
            "input": [22, 33, 22, 33, 22],
            "output": 22,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param["input"]
        result = solution.minimumCost(nums)
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
