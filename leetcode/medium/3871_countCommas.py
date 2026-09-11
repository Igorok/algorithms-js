import json
from collections import deque
from functools import cache
from typing import List


class Solution:
    def countCommas(self, n: int) -> int:
        step = 1000
        res = 0

        while n >= step:
            res += n - step + 1
            step *= 1000

        return res


"""
1_200_200
"""


def test():
    params = [
        {
            "input": 1002,
            "output": 3,
        },
        {
            "input": 998,
            "output": 0,
        },
        {
            "input": 2_002,
            "output": 1003,
        },
        {
            "input": 2_000_002,
            "output": 2999006,
        },
        {
            "input": 9_999,
            "output": 9000,
        },
        {
            "input": 10_000_000,
            "output": 18999002,
        },
    ]
    solution = Solution()

    for param in params:
        n = param["input"]
        result = solution.countCommas(n)
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
