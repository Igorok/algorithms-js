import heapq
import json
from collections import defaultdict, deque
from functools import lru_cache
from typing import List


class Solution:
    def sumAndMultiply(self, n: int) -> int:
        num = 0
        sumOfDigits = 0

        i = 1
        while n > 0:
            r = n % 10
            n = n // 10
            if r == 0:
                continue

            sumOfDigits += r

            r = r * i
            num = num + r
            i *= 10

        return num * sumOfDigits


def test():
    params = [
        {
            "input": 10203004,
            "output": 12340,
        },
        {
            "input": 1000,
            "output": 1,
        },
    ]
    solution = Solution()

    for param in params:
        n = param["input"]
        result = solution.sumAndMultiply(n)
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
