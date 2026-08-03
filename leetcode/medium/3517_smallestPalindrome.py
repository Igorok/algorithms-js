import heapq
import json
from collections import defaultdict, deque
from functools import cache
from typing import List


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        N = len(s)
        charsCnt = [0] * 26
        for char in s:
            id = ord(char) - ord("a")
            charsCnt[id] += 1

        res = [""] * N
        id = 0

        for i in range(26):
            char = chr(ord("a") + i)

            if (charsCnt[i] % 2) == 1:
                charsCnt[i] -= 1
                res[N // 2] = char

            while charsCnt[i] > 0:
                res[id] = char
                res[N - 1 - id] = char

                charsCnt[i] -= 2
                id += 1

        return "".join(res)


def test():
    params = [
        # {
        #     "input": "z",
        #     "output": "z",
        # },
        {
            "input": "babab",
            "output": "abbba",
        },
        {
            "input": "daccad",
            "output": "acddca",
        },
    ]
    solution = Solution()

    for param in params:
        s = param["input"]
        result = solution.smallestPalindrome(s)

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
