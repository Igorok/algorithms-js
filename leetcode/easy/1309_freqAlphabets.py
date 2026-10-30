import json
from collections import defaultdict, deque
from functools import cache
from typing import List


class Solution:
    def freqAlphabets(self, s: str) -> str:
        memo = {}
        for i in range(26):
            char = chr(ord("a") + i)
            key = i + 1
            if key > 9:
                key = str(key) + "#"
            else:
                key = str(key)

            memo[key] = char

        # print("memo", memo)

        res = []
        i = len(s) - 1
        while i > -1:
            if s[i] == "#":
                char = s[i - 2 : i + 1]
                res.append(memo[char])
                i -= 3
            else:
                char = s[i : i + 1]
                res.append(memo[char])
                i -= 1

        res.reverse()
        return "".join(res)


def test():
    params = [
        {
            "input": "10#11#12",
            "output": "jkab",
        },
        {
            "input": "1326#",
            "output": "acz",
        },
    ]
    solution = Solution()

    for param in params:
        s = param["input"]
        result = solution.freqAlphabets(s)
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
