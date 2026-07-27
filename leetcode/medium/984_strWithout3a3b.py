import heapq
import json
from collections import defaultdict, deque
from functools import lru_cache
from typing import List


class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []
        count = [a, b]
        curr = 0 if a >= b else 1

        while count[0] > 0 or count[1] > 0:
            res.append(chr(ord("a") + curr))
            count[curr] -= 1

            if count[curr] >= count[(curr + 1) % 2] and count[curr] > 0:
                res.append(chr(ord("a") + curr))
                count[curr] -= 1

            curr = (curr + 1) % 2

        return "".join(res)


def test():
    params = [
        {
            "input": [1, 2],
            "output": "abb",
        },
        {
            "input": [4, 1],
            "output": "aabaa",
        },
    ]
    solution = Solution()

    for param in params:
        a, b = param["input"]
        result = solution.strWithout3a3b(a, b)

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
