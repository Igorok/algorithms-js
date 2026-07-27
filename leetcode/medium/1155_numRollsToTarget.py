import heapq
import json
from collections import defaultdict, deque
from functools import lru_cache
from typing import List


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7

        prev = [0] * (target + 1)
        for i in range(min(k + 1, target + 1)):
            prev[i] = 1

        for step in range(1, n):
            curr = [0] * (target + 1)

            for num in range(1, k + 1):
                for val in range(step, target + 1):
                    if val + num > target:
                        break
                    if prev[val] == 0:
                        continue

                    curr[val + num] = (curr[val + num] + prev[val]) % MOD

            prev = curr

        return prev[target]


def test():
    params = [
        {
            "input": [1, 6, 3],
            "output": 1,
        },
        {
            "input": [2, 6, 7],
            "output": 6,
        },
        {
            "input": [30, 30, 500],
            "output": 222616187,
        },
        {
            "input": [10, 6, 50],
            "output": 85228,
        },
    ]
    solution = Solution()

    for param in params:
        n, k, target = param["input"]
        result = solution.numRollsToTarget(n, k, target)

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
