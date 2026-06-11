import heapq
from collections import defaultdict
from json import dumps
from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        connectByNode = defaultdict(int)
        for start, end in roads:
            connectByNode[start] += 1
            connectByNode[end] += 1

        connectByNode = sorted(connectByNode.items(), key=lambda x: -x[1])

        availVal = n
        # valByNode = {}
        res = 0

        for node, cnt in connectByNode:
            # valByNode[node] = availVal
            res += cnt * availVal
            availVal -= 1

        # for start, end in roads:
        #     res += valByNode[start] + valByNode[end]

        return res


def test():
    params = [
        {
            "input": [5, [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]],
            "output": 43,
        },
        {
            "input": [5, [[0, 3], [2, 4], [1, 3]]],
            "output": 20,
        },
    ]
    solution = Solution()

    for param in params:
        n, roads = param["input"]
        result = solution.maximumImportance(n, roads)
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
