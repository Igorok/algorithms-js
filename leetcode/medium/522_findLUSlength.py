import heapq
import json
from collections import defaultdict, deque
from functools import lru_cache
from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        unique = defaultdict(int)

        def rec(text, id, acc):
            nonlocal unique

            if id == len(text):
                unique[acc] += 1
                return

            rec(text, id + 1, acc)
            rec(text, id + 1, acc + text[id])

        for text in strs:
            rec(text, 0, "")

        res = ""
        for key, val in unique.items():
            if len(key) > len(res) and val == 1:
                res = key

        return -1 if res == "" else len(res)


def test():
    params = [
        {
            "input": ["aba", "cdc", "eae"],
            "output": 3,
        },
        {
            "input": ["aaa", "aaa", "aa"],
            "output": -1,
        },
        {
            "input": ["aaa", "aa"],
            "output": 3,
        },
        {
            "input": ["aabbcc", "aabbcc", "c"],
            "output": -1,
        },
        {
            "input": ["eabcd", "eabcf"],
            "output": 5,
        },
        {
            "input": ["aabbcc", "aabbcc", "cb", "abc"],
            "output": 2,
        },
    ]
    solution = Solution()

    for param in params:
        strs = param["input"]
        result = solution.findLUSlength(strs)

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
