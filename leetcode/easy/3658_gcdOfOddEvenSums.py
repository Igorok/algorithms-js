import heapq
import json
from collections import defaultdict, deque
from functools import lru_cache
from typing import List


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def getSum(a1, step):
            an = a1 + step * (n - 1)
            return (an + a1) * n // 2

        # print("odd", getSum(1, 2))
        # print("even", getSum(2, 2))

        def getGcd(a, b):
            a, b = [a, b] if a >= b else [b, a]

            if a % b == 0:
                return b

            a = a % b
            return getGcd(b, a)

        return getGcd(getSum(1, 2), getSum(2, 2))


def test():
    params = [
        {
            "input": 4,
            "output": 4,
        },
        {
            "input": 5,
            "output": 5,
        },
    ]
    solution = Solution()

    for param in params:
        n = param["input"]
        result = solution.gcdOfOddEvenSums(n)

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
