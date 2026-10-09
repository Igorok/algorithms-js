import heapq
import json
from collections import defaultdict, deque
from functools import lru_cache
from typing import List

'''
a:
    a
b:
    a, b, ab
c:
    a, b, ab, c, ac, bc, abc
b:
    a, b, ab, c, ac, bc, abc, bb, abb, cb, acb, bcb, abcb
    duplicates: b, ab

curr = 1 + prev - duplicates
1 - current char
prev - previous combinations
duplicates - combinations ended by char

'''
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 +7
        ordA = ord('a')
        memo = [0]*26
        res = 0

        for char in s:
            id = ord(char) - ordA
            unique= res + 1 - memo[id]
            res = (res + unique) % MOD
            memo[id] = (memo[id] + unique) % MOD

        return res


def test():
    params = [
        {
            "input": "abc",
            "output": 7,
        },
        {
            "input": "aba",
            "output": 6,
        },
        {
            "input": "aaa",
            "output": 3,
        },
    ]
    solution = Solution()

    for param in params:
        s = param["input"]
        result = solution.distinctSubseqII(s)

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
