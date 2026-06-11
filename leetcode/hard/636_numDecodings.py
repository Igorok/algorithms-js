import heapq
from collections import defaultdict
from functools import cache
from json import dumps
from typing import List


class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        MOD = 10**9 + 7

        @cache
        def dfs(id):
            if id == N:
                return 1

            if s[id] == "0":
                return 0

            # len == 1
            r1 = 0
            if s[id] == "*":
                r1 = 9
                rDfs = dfs(id + 1)
                r1 *= rDfs
            else:
                r1 = dfs(id + 1)

            # len == 2
            r2 = 0
            if id < N - 1:
                # if int(s[id:id+2]) > 26
                if s[id] == "*" and s[id + 1] == "*":
                    # 11,12,13,14,15,16,17,18,19 + 21,22,23,24,25,26
                    r2 = 9 + 6
                    rDfs = dfs(id + 2)
                    r2 *= rDfs
                elif s[id] == "*":
                    rDfs = dfs(id + 2)
                    # 1
                    r2_1 = rDfs
                    # 2
                    r2_2 = 0 if int(s[id + 1]) > 6 else rDfs
                    r2 = r2_1 + r2_2

                elif s[id + 1] == "*":
                    rDfs = dfs(id + 2)
                    if s[id] == "1":
                        r2 = 9 * rDfs
                    elif s[id] == "2":
                        r2 = 6 * rDfs
                    else:
                        r2 = 0
                else:
                    rDfs = dfs(id + 2)
                    r2 = rDfs if int(s[id : id + 2]) < 27 else 0

            return (r1 % MOD + r2 % MOD) % MOD

        return dfs(0)


def test():
    params = [
        {
            "input": "*",
            "output": 9,
        },
        {
            "input": "1*",
            "output": 18,
        },
        {
            "input": "2*",
            "output": 15,
        },
        {
            "input": "*2",
            "output": 11,
        },
    ]
    solution = Solution()

    for param in params:
        s = param["input"]
        result = solution.numDecodings(s)
        print(
            "SUCCESS" if result == param["output"] else "ERROR",
            "input",
            param["input"],
            "output",
            param["output"],
            "result",
            result,
            "\n",
        )


if __name__ == "__main__":
    test()
