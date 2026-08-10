from collections import deque
from functools import cache
from json import dumps
from typing import List


class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
        adjBoth = [[] for i in range(n)]
        adjDirect = [[] for i in range(n)]
        for s, e in invocations:
            adjBoth[s].append(e)
            adjBoth[e].append(s)

            adjDirect[s].append(e)

        colorsBoth = [-1] * n
        colorsDirect = [-1] * n

        def mark(node, adj, colors):
            acc = 1
            for nei in adj[node]:
                if colors[nei] != -1:
                    continue

                colors[nei] = 1
                acc += mark(nei, adj, colors)
            return acc

        colorsBoth[k] = 1
        bothCnt = mark(k, adjBoth, colorsBoth)
        colorsDirect[k] = 1
        directCnt = mark(k, adjDirect, colorsDirect)

        # print(bothCnt, directCnt)

        canRemove = bothCnt == directCnt

        # print(
        #     "colorsBoth",
        #     colorsBoth,
        #     "colorsDirect",
        #     colorsDirect,
        # )

        if not canRemove:
            return [i for i in range(n)]

        return [i for i in range(n) if colorsBoth[i] == -1]


def test():
    params = [
        {
            "input": [4, 1, [[1, 2], [0, 1], [3, 2]]],
            "output": [0, 1, 2, 3],
        },
        {
            "input": [5, 0, [[1, 2], [0, 2], [0, 1], [3, 4]]],
            "output": [3, 4],
        },
        {
            "input": [3, 2, [[1, 2], [0, 1], [2, 0]]],
            "output": [],
        },
        {
            "input": [5, 3, [[1, 0], [2, 1], [3, 2], [4, 3]]],
            "output": [0, 1, 2, 3, 4],
        },
    ]
    solution = Solution()

    for param in params:
        n, k, invocations = param["input"]
        result = solution.remainingMethods(n, k, invocations)
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
