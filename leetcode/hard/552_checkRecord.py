import json
import math
from collections import Counter, defaultdict, deque

# from functools import cache
from linecache import cache
from typing import List

"""



I do not understand this line.
```
# 3. Choose 'A' (Absent)
# Can only append 'A' if total 'A' was 0. It resets consecutive 'L' to 0.
next_dp[1][0] = (next_dp[1][0] + dp[0][0] + dp[0][1] + dp[0][2]) % MOD
```
next_dp[1][0] - we already have A?
dp[0][0] + dp[0][1] + dp[0][2] - we add P, L, LL?

"""


class Solution_0:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        chars = ("A", "L", "P")
        memo = {}

        def rec(length, prev, absent):
            nonlocal n, MOD, chars

            key = f"{str(length)}_{prev}_{str(absent)}"

            if key in memo:
                return memo[key]

            if length == n:
                return 1

            res = 0
            for char in chars:
                a = absent + 1 if char == "A" else absent
                if a > 1:
                    continue

                curr = prev + char
                if curr == "LLL":
                    continue
                if len(curr) > 3:
                    curr = curr[1:]
                    if curr == "LLL":
                        continue

                r = rec(length + 1, curr, a)
                res = (res + r) % MOD

            memo[key] = res % MOD
            return memo[key]

        return rec(0, "", 0)


class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        # row - Absent
        # col - count of Late
        dp = [[0] * 3 for i in range(2)]
        # P
        dp[0][0] = 1

        for i in range(n):
            next_dp = [[0] * 3 for i in range(2)]
            # +P
            next_dp[0][0] = (dp[0][0] + dp[0][1] + dp[0][2]) % MOD
            next_dp[1][0] = (dp[1][0] + dp[1][1] + dp[1][2]) % MOD

            # +L
            next_dp[0][1] = dp[0][0]
            next_dp[1][1] = dp[1][0]

            # +LL
            next_dp[0][2] = dp[0][1]
            next_dp[1][2] = dp[1][1]

            # +A
            # I have a dp[0] for yesterday
            # and I have dp[0] combinations to put A there
            next_dp[1][0] = (next_dp[1][0] + dp[0][0] + dp[0][1] + dp[0][2]) % MOD

            dp = next_dp

        res = sum(sum(dp[i]) % MOD for i in range(2)) % MOD

        return res


def test():
    params = [
        {
            "input": 2,
            "output": 8,
        },
        {
            "input": 1,
            "output": 3,
        },
        # {
        #     "input": 10101,
        #     "output": 183236316,
        # },
        {
            "input": 100,
            "output": 985598218,
        },
    ]
    solution = Solution()

    for param in params:
        n = param["input"]
        result = solution.checkRecord(n)
        correct = json.dumps(result) == json.dumps(param["output"])

        msg = "SUCCESS" if correct else "ERROR"
        msg += "\n"
        if not correct:
            # msg += "input " + json.dumps(param["input"]) + "\n"
            msg += "output " + json.dumps(param["output"]) + "\n"
            msg += "result " + json.dumps(result) + "\n"

        print(msg)


if __name__ == "__main__":
    test()
