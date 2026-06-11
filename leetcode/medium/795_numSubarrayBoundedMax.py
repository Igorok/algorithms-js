import heapq
import json
from collections import deque
from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        n = len(nums)
        start = 0
        active = 0
        res = 0

        for end in range(n):
            if nums[end] > right:
                start = end + 1
                active = 0
                continue

            if nums[end] <= right and nums[end] >= left:
                active = True

            if active:
                res += 1

        return res


"""

1 1 2 1 1 2 2 1 1

"""


def test():
    params = [
        {
            "input": [[2, 1, 4, 3], 2, 3],
            "output": 3,
        },
        {
            "input": [[2, 9, 2, 5, 6], 2, 8],
            "output": 7,
        },
    ]

    solution = Solution()

    for param in params:
        nums, left, right = param["input"]
        result = solution.numSubarrayBoundedMax(nums, left, right)
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
