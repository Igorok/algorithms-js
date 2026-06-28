import heapq
import math
from collections import Counter, defaultdict
from functools import cache
from json import dumps
from typing import List


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        visited = [0] * 10
        memo = [0] * 10

        def dfs(id):
            if visited[id] == 1:
                return -1
            if visited[id] == 2:
                return memo[id]

            visited[id] = 1

            res = change[id]
            r = dfs(change[id])

            visited[id] = 2

            memo[id] = max(res, r)

            return memo[id]

        for i in range(len(change)):
            dfs(i)

        # memo = [str(n) for n in memo]
        memo = [str(n) for n in change]

        N = len(num)

        for i in range(N):
            if num[i] >= memo[int(num[i])]:
                continue
            j = i
            part = []
            while j < N and memo[int(num[j])] >= num[j]:
                part.append(memo[int(num[j])])
                j += 1
            res = num[:i] + "".join(part) + num[j:]
            return res

        return num


def test():
    params = [
        {
            "input": ["132", [9, 8, 5, 0, 3, 6, 4, 2, 6, 8]],
            "output": "832",
        },
        {
            "input": ["021", [9, 4, 3, 5, 7, 2, 1, 9, 0, 6]],
            "output": "934",
        },
        {
            "input": ["5", [1, 4, 7, 5, 3, 2, 5, 6, 9, 4]],
            "output": "5",
        },
    ]
    solution = Solution()

    for param in params:
        num, change = param["input"]
        result = solution.maximumNumber(num, change)
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
