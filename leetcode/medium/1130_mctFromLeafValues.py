import heapq
from collections import Counter, defaultdict
from functools import cache
from json import dumps
from typing import List

"""
what is a crap leetcode issue "1130. Minimum Cost Tree From Leaf Values"
i can not solve it by bruteforse

"""


class Solution_0:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        memo = {}

        def dfs(leafs):
            nonlocal memo

            memoKey = []
            for leaf in leafs:
                if len(leaf) == 1:
                    memoKey.append(f"({leaf[0]})")
                if len(leaf) == 2:
                    memoKey.append(f"({leaf[0]}_{leaf[1]})")

            memoKey = "_".join(memoKey)
            if memoKey in memo:
                return memo[memoKey]

            res = float("inf")
            N = len(leafs)
            if N == 1:
                return 0

            for i in range(1, N):
                right = leafs[i]
                left = leafs[i - 1]
                leaf = sorted(left + right, key=lambda x: -x)[:2]
                val = leaf[0] * leaf[1]
                newLeafs = leafs[: i - 1] + [leaf] + leafs[i + 1 :]
                r = dfs(newLeafs)
                res = min(r + val, res)

            memo[memoKey] = res

            return res

        res = dfs([[n] for n in arr])

        return res


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        @cache
        def dfs(left, right):
            nonlocal arr

            if left == right:
                return 0

            res = float("inf")

            for id in range(left, right):
                lVal = max(arr[left : id + 1])
                rVal = max(arr[id + 1 : right + 1])
                val = lVal * rVal

                resL = dfs(left, id)
                resR = dfs(id + 1, right)

                res = min(res, val + resL + resR)

            return res

        return dfs(0, len(arr) - 1)


def test():
    params = [
        {
            "input": [6, 2, 4],
            "output": 32,
        },
        {
            "input": [4, 11],
            "output": 44,
        },
        {
            "input": [6, 15, 5, 2],
            "output": 175,
        },
        {
            "input": [5, 1, 2, 3, 15, 7, 3, 2, 2, 5, 9, 1, 11, 9, 15, 14, 7, 1, 5],
            "output": 1166,
        },
    ]
    solution = Solution()

    for param in params:
        arr = param["input"]
        result = solution.mctFromLeafValues(arr)
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
