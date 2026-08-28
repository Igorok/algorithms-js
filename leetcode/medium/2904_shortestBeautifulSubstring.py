import json
from collections import Counter
from functools import cache
from typing import List

"""

{
    "input": ["1100100101011001001", 7],
    "output": "1100100101011",
},
100101011001001
"""


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        N = len(s)
        left = 0
        right = 0
        res = ""
        acc = 0

        for right in range(N):
            if s[right] == "1":
                acc += 1

            while acc == k:
                text = s[left : right + 1]
                if (
                    res == ""
                    or len(res) > len(text)
                    or (len(res) == len(text) and res > text)
                ):
                    res = text

                if s[left] == "1":
                    acc -= 1
                left += 1

        return res


def test():
    params = [
        {
            "input": ["100011001", 3],
            "output": "11001",
        },
        {
            "input": ["1011", 2],
            "output": "11",
        },
        {
            "input": ["000", 1],
            "output": "",
        },
        {
            "input": ["1100100101011001001", 7],
            "output": "1100100101011",
        },
    ]
    solution = Solution()

    for param in params:
        s, k = param["input"]
        result = solution.shortestBeautifulSubstring(s, k)
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
