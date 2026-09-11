import json
from collections import deque
from functools import cache
from typing import List


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        N = len(s)
        res = 0
        left = 0
        cnt = 0
        for right in range(N):
            if s[right] != t[right]:
                cnt += abs(ord(s[right]) - ord(t[right]))

            while cnt > maxCost:
                if s[left] != t[left]:
                    cnt -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            res = max(res, right - left + 1)

        return res


def test():
    params = [
        {
            "input": ["abcd", "bcdf", 3],
            "output": 3,
        },
        {
            "input": ["abcd", "cdef", 3],
            "output": 1,
        },
        {
            "input": ["abcd", "acde", 0],
            "output": 1,
        },
    ]
    solution = Solution()

    for param in params:
        s, t, maxCost = param["input"]
        result = solution.equalSubstring(s, t, maxCost)
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
