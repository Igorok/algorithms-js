import heapq
import json
from collections import defaultdict, deque
from functools import lru_cache
from typing import List


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:

        data = []
        N = len(s)

        data.append([s[0], 1])
        totalOne = 0 if s[0] == "0" else 1

        for i in range(1, N):
            if s[i] == "1":
                totalOne += 1

            if s[i] == s[i - 1]:
                data[-1][1] += 1
            else:
                data.append([s[i], 1])

        res = totalOne

        for i in range(len(data)):
            if data[i][0] == "0":
                continue

            if i - 1 == -1 or i + 1 == len(data):
                continue

            left = data[i - 1][1]
            right = data[i + 1][1]

            res = max(res, totalOne + left + right)

        return res


def test():
    params = [
        {
            "input": "01",
            "output": 1,
        },
        {
            "input": "0100",
            "output": 4,
        },
        {
            "input": "1000100",
            "output": 7,
        },
        {
            "input": "01010",
            "output": 4,
        },
    ]
    solution = Solution()

    for param in params:
        s = param["input"]
        result = solution.maxActiveSectionsAfterTrade(s)

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
