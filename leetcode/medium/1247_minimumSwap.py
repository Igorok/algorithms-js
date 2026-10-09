import json
from collections import defaultdict, deque
from functools import cache
from typing import List


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x_y = 0
        y_x = 0

        N = len(s1)
        for i in range(N):
            if s1[i] == s2[i]:
                continue
            if s1[i] == "x":
                x_y += 1
            else:
                y_x += 1

        if ((x_y + y_x) % 2) != 0:
            return -1

        res = 0
        res += x_y // 2
        res += y_x // 2

        x_y = x_y % 2
        res += x_y * 2

        return res


def test():
    params = [
        {
            "input": ["xx", "yy"],
            "output": 1,
        },
        {
            "input": ["xy", "yx"],
            "output": 2,
        },
        {
            "input": ["xx", "xy"],
            "output": -1,
        },
    ]
    solution = Solution()

    for param in params:
        s1, s2 = param["input"]
        result = solution.minimumSwap(s1, s2)
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
