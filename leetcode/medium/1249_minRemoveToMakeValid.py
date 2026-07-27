import heapq
import json
from collections import defaultdict, deque
from functools import lru_cache
from typing import List


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        N = len(s)
        stack = []
        available = [0] * N

        for i in range(N):
            if s[i] == "(":
                stack.append(i)
            if s[i] == ")":
                if len(stack):
                    available[i] = 1
                    prev = stack.pop()
                    available[prev] = 1

        res = []
        for i in range(N):
            if s[i] == "(" or s[i] == ")":
                if available[i] == 1:
                    res.append(s[i])
                continue

            res.append(s[i])

        return "".join(res)


def test():
    params = [
        {
            "input": "lee(t(c)o)de)",
            "output": "lee(t(c)o)de",
        },
        {
            "input": "a)b(c)d",
            "output": "ab(c)d",
        },
        {
            "input": "))((",
            "output": "",
        },
        {
            "input": "(l(e(e(t(c)o)de)",
            "output": "le(e(t(c)o)de)",
        },
        {
            "input": "())()(((",
            "output": "()()",
        },
    ]
    solution = Solution()

    for param in params:
        s = param["input"]
        result = solution.minRemoveToMakeValid(s)

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
