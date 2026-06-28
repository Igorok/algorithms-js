import json
import math
from collections import Counter, defaultdict, deque

# from functools import cache
from linecache import cache
from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()

        arr[0] = 1
        for i in range(1, len(arr)):
            arr[i] = min(arr[i], arr[i - 1] + 1)

        return arr[-1]


def test():
    params = [
        {
            "input": [2, 2, 1, 2, 1],
            "output": 2,
        },
        {
            "input": [100, 1, 1000],
            "output": 3,
        },
        {
            "input": [1, 2, 3, 4, 5],
            "output": 5,
        },
        {
            "input": [1, 2, 3, 4, 4, 8],
            "output": 5,
        },
    ]
    solution = Solution()

    for param in params:
        arr = param["input"]
        result = solution.maximumElementAfterDecrementingAndRearranging(arr)
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
