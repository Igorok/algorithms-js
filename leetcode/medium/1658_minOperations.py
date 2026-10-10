import json
from collections import deque
from functools import cache
from typing import List


class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        N = len(nums)
        total = sum(nums)
        if total < x:
            return -1
        if total == x:
            return N

        length = -1

        left = 0
        acc = 0

        for right in range(N):
            acc += nums[right]

            while left < right and total - acc < x:
                acc -= nums[left]
                left += 1

            if total - acc == x:
                length = max(length, right - left + 1)

        return -1 if length == -1 else N - length


"""
4
100, 100, 1, 1, 1, 1

"""


def test():
    params = [
        {
            "input": [[1, 1, 4, 2, 3], 5],
            "output": 2,
        },
        {
            "input": [[5, 6, 7, 8, 9], 4],
            "output": -1,
        },
        {
            "input": [[3, 2, 20, 1, 1, 3], 10],
            "output": 5,
        },
        {
            "input": [[1, 1], 3],
            "output": -1,
        },
    ]
    solution = Solution()

    for param in params:
        nums, x = param["input"]
        result = solution.minOperations(nums, x)
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
