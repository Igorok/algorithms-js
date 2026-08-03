import heapq
import json
import math
from collections import defaultdict, deque
from functools import cache
from typing import Counter, List


class Solution:
    def minimumPushes(self, word: str) -> int:
        length = len(word)

        res = 0
        cnt = 1
        for i in range(length // 8):
            res += 8 * cnt
            cnt += 1

        rem = length % 8
        if rem != 0:
            res += rem * cnt

        return res


"""

"x" -> one push on key 2
"y" -> two pushes on key 2
"c" -> one push on key 3
"d" -> two pushes on key 3
"e" -> one push on key 4
"f" -> one push on key 5
"g" -> one push on key 6
"h" -> one push on key 7
"i" -> one push on key 8
"j" -> one push on key 9
Total cost is 1 + 2 + 1 + 2 + 1 + 1 + 1 + 1 + 1 + 1 = 12.
It can be shown that no other mapping can provide a lower cost.


"""


def test():
    params = [
        {
            "input": "abcde",
            "output": 5,
        },
        {
            "input": "xycdefghij",
            "output": 12,
        },
    ]
    solution = Solution()

    for param in params:
        word = param["input"]
        result = solution.minimumPushes(word)

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
