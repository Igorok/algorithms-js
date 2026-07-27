import heapq
import json
from collections import defaultdict, deque
from functools import cache
from typing import List

"""
Could you explain to the leetcode issue "526. Beautiful Arrangement"?
Input: n = 2
Output: 2
Explanation:
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1


[1,2]
1%1=0;1%1=0;
2%2=0;2%2=1;
okay

[2,1]
2%1=0;1%2=1;
1%2=1;2%1=0;
wtf?

"""


class Solution:
    def countArrangement(self, n: int) -> int:

        @cache
        def rec(id, acc):
            nonlocal n

            if id == n + 1:
                return 1

            res = 0
            for num in range(1, n + 1):
                if ((acc >> num) & 1) == 1:
                    continue

                if (num % id) != 0 and ((id % num) != 0):
                    continue

                newAcc = acc | (1 << num)

                res += rec(id + 1, newAcc)

            return res

        return rec(1, 0)


def test():
    params = [
        {
            "input": 2,
            "output": 2,
        },
        {
            "input": 1,
            "output": 1,
        },
        {
            "input": 4,
            "output": 8,
        },
        {
            "input": 15,
            "output": 24679,
        },
    ]
    solution = Solution()

    for param in params:
        n = param["input"]
        result = solution.countArrangement(n)

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
